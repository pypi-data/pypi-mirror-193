# Abstract classes for UIs. The idea here is to allow many different user
# interfaces (shell, curses, Slack, etc) to drive the same data model without
# the data model needing specific UI knowledge.
#
# The UI keeps a reference to the Handler. The Handler will bring a Command with
# it, and this is the main root command. In the case of a Shell-type UI, that is
# the command to be executed. In the case of an interactive UI, it's really just
# a placeholder; the UI will instantiate other commands as it proceeds. But the
# Handler won't know about those.
#
# Commands might call back to the UI for confirmations or arguments that are
# previously omitted, using the get_ methods.

#
# UI end classes must implement the following interface:
#
# __init__(handler): Takes the handler and hangs on to it. Implemented in the
# main base class.
#
# start(): No arguments. Actually performs the operation of the UI. It might be
# short running (in the case of a shell UI) or long-running (in the case of an
# interactive UI).
#
# output(intro=""): Output some multi-line text explaining an action, usually a
# list of items being acted upon.
#
# get_string(prompt, default=""): For arguments that are omitted, get a string
# from the user. The prompt is just a word (like "Description") telling the user
# what to input.
#
# get_confirmation(verb): For delete-oriented commands to
# confirm with the user before proceeding. Verb is what we're asking the user to
# confirm. Description can be multiple lines, as with get_string. Returns a
# boolean saying whether the action is confirmed.

import subprocess
from tempfile import NamedTemporaryFile
from pathlib import Path
import shutil
import os
import re
from io import StringIO

from busy.model.item import write_items
from busy.model.item import read_items
from busy.util.class_family import ClassFamily

class UI(ClassFamily):

    def __init__(self, handler=None):
        self.handler = handler
    
    def start(self):
        pass


# Terminal UIs include Shell and Curses, since both will rely on a
# terminal-based editor for the e.g. Manage command.

class TerminalUI(UI):

    # A convenience method to get a full textual prompt for a string input

    def full_prompt(self, prompt, default):
        if default:
            return f'{prompt} [{default}]: '
        else:
            return f'{prompt}: '


    def edit_items(self, itemclass, *items):
        commands = [['sensible-editor'], ['open', '-W']]
        with NamedTemporaryFile(mode="w+") as tempfile:
            write_items(tempfile, *items)
            tempfile.seek(0)
            command = [os.environ.get('EDITOR')]
            if not command[0] or not shutil.which(command[0]):
                iterator = (c for c in commands if shutil.which(c[0]))
                command = next(filter(None, iterator), None)
                if not command:
                    raise RuntimeError("A text editor at the $EDITOR environment variable is required")
            subprocess.run(command + [tempfile.name])
            tempfile.seek(0)
            new_items = read_items(tempfile, itemclass)
            return new_items
