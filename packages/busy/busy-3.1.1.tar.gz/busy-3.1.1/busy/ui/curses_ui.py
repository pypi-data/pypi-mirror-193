# A terminal-based UI uses Curses, which offers one-key access to most common
# operations.
#
# The terminal has 3 regions, implemented as curses window objects. The regions
# are organized top-to-bottom with a 1-row gap between them. There is also a
# 1-row/1-column gap around the outside of the main terminal window containing
# the regions.
#
# Status region (_statuswin) - 6 lines at the top. Current queue name, current
# task, some blank space, status of the most recent operation, and input prompt
# for the main command.
#
# List region (_listwin) - Takes up the space between the other two regions.
# Shows mostly lists of tasks for confirmation and/or management.
#
# Edit region (_editwin) - 2 lines at the bottom. Used for editing of individual
# task descriptions, such as when adding a new task to the queue.


import curses
from argparse import Namespace
from string import capwords

from ..ui.ui import TerminalUI

class CursesCancelError(Exception):
    pass

class CursesUI(TerminalUI):  # pragma: nocover

    name = "curses"

    def start(self):
        self._mode = "WORK"
        keynames = self.handler.get_command_values('key', 'name')
        keynames.add(('q', 'quit'))
        skeynames = sorted(keynames, key=lambda kn: kn[0])
        self._main_prompt = skeynames
        curses.wrapper(self.term_loop)

    def output(self, intro=""):
        self._descwin.clear()
        self._descwin.addstr(intro)
        self._descwin.refresh()


    # TODO: Use a better editing component

    def get_string(self, prompt, default=""):
        self._update_status(self.full_prompt(prompt, default))
        curses.echo()
        try:
            string = self._statuswin.getstr()
        except KeyboardInterrupt:
            raise CursesCancelError
        value = string.decode() or default
        curses.noecho()
        return value

    # In Curses, confirm with a single keystroke
    #
    # TODO: Handle the case where the description is too long for the panel

    def get_confirmation(self, verb):
        prompt = f"{verb}? (y/n) --> "
        self._update_status(prompt)
        key = self._get_key()
        confirmed = (key == 'y')
        return confirmed
    
    def term_loop(self, fullwin):
        root = self.handler.root
        self._queue_name = "tasks"
        curses.init_color(curses.COLOR_BLACK, 200, 200, 200)
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        h, w = fullwin.getmaxyx()
        self._statuswin = curses.newwin(5, w-2, 1, 1)
        self._descwin = curses.newwin(h-8, w-2, 7, 1)
        self._editwin = curses.newwin(1, w-2, h-2, 1)
        self._status = "Welcome to Busy!"
        list = ""
        cursor = 0
        while True:
            self.output()
            self._update_status(self._main_prompt)
            try:
                key = self._get_key()
            except CommandCanceledError:
                break
            if key == "q":
                break
            command = self.handler.get_command('key', key, self)
            if not command:
                self._status = f"Invalid command {key}"
                continue
            command_name = capwords(command.name)
            self._status = f"{command_name} in progress"
            self._update_status("")
            namespace = Namespace()
            try:
                result = command.execute(namespace)
            except CursesCancelError:
                self._status = f"{command_name} command canceled"
                continue
            self._status = command.status or ""

    def _update_status(self, prompt):
        queue = self.handler.root.get_queue(self._queue_name)
        self._statuswin.clear()
        self._statuswin.move(0, 0)
        self._statuswin.addstr("Queue: ", curses.color_pair(1))
        self._statuswin.addstr(capwords(self._queue_name), curses.A_BOLD)
        self._statuswin.move(1, 0)
        self._statuswin.addstr("Top:   ", curses.color_pair(1))
        self._statuswin.addstr(str(queue.top()) or '', curses.A_BOLD)
        self._statuswin.move(3, 0)
        self._statuswin.addstr(self._status, curses.color_pair(2))
        self._statuswin.move(4, 0)
        if type(prompt) == str:
            self._statuswin.addstr(prompt, curses.color_pair(3))
        elif type(prompt) == list:
            for key, name in prompt:
                pre, it, post = name.partition(key)
                self._statuswin.addstr(pre, curses.color_pair(3))
                self._statuswin.addstr(it, curses.A_UNDERLINE + curses.color_pair(3))
                self._statuswin.addstr(post + " ", curses.color_pair(3))
            self._statuswin.addstr("--> ", curses.color_pair(3))
        cursor = self._statuswin.getyx()
        self._statuswin.refresh()
        self._statuswin.move(*cursor)

    # Convenience method to get one keystroke from the user.
    #     
    def _get_key(self):
        try:
            key = self._statuswin.getkey()
        except KeyboardInterrupt:
            raise CursesCancelError
        self._statuswin.addstr(key)
        return key


    # def listmode(self):
    #     length = len(list.splitlines())
    #     if length:
    #         listpad = curses.newpad(length, curses.COLS)
    #         listpad.addstr(list)
    #         self.listmode = True
    #         listpad.move(cursor, 0)
    #         listpad.addstr(">")
    #         listpad.refresh(0, 0, 5, 0, curses.LINES - 5, curses.COLS)
    #     if self.listmode:
    #         if key == "KEY_UP" and cursor > 0:
    #             cursor = cursor - 1
    #         if key == "KEY_DOWN" and cursor < length:
    #             cursor = cursor + 1
