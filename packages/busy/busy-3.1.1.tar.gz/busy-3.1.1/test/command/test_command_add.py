from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch

from busy.command.add_command import AddCommand


class TestCommandAdd(TestCase):

    def test_call_method(self):
        c = AddCommand()
        c._queue_ = Mock()
        c._namespace = Mock()
        c._namespace.description = 'd'
        c.call_method()
        c._queue.add.assert_called_with('d')

    def test_add_omitted_description(self):
        u = Mock()
        u.get_string = lambda d: 'f'
        c = AddCommand(None, u)
        c._namespace = Mock()
        c._namespace.description = None
        c.clean_args()
        self.assertEqual(c._namespace.description, 'f')