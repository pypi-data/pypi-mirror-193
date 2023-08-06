# The UI to execute one command passed in through the shell. There will be
# limited interactivity, if the user omits an argument on the command line, but
# otherwise this is a run and done situation.
#
# The code for argparse lives at https://github.com/python/cpython/blob/main/Lib/argparse.py


from argparse import ArgumentParser
from io import StringIO

from ..ui.ui import TerminalUI


class ShellUI(TerminalUI):

    name = "shell"

    def output(self, intro=""):
        if intro:
            print(intro)

    def get_string(self, prompt='', default=""):
        full_prompt = self.full_prompt(prompt, default)
        value = input(full_prompt) or default
        return value

    def get_confirmation(self, verb):
        confirmed = input(f'{verb}? (Y/n) ').startswith('Y')
        return confirmed
