from unittest import TestCase
from unittest.mock import Mock

from busy.command.curses_command import CursesCommand

class TestCommandCurses(TestCase):

    def test_execute(self):
        u = Mock()
        c = CursesCommand(None, u)
        n = Mock()
        c.execute(n)
        u.start.assert_called_once_with()

