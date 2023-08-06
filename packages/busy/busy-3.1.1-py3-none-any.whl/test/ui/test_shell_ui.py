from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock
from io import StringIO

from busy.ui.shell_ui import ShellUI

class TestShellUI(TestCase):

    def test_get_string(self):
        u = ShellUI()
        with patch('sys.stdin', StringIO('g')):
            v = u.get_string()
            self.assertEqual(v, 'g')

    @patch('sys.stdin', StringIO('Y'))
    def test_get_confirmation(self):
        u = ShellUI()
        o = StringIO()
        with patch('sys.stdout', o):
            v = u.get_confirmation('A')
            self.assertEqual(o.getvalue(), 'A? (Y/n) ')
