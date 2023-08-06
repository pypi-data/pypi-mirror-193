from unittest import TestCase
from unittest.mock import Mock

from busy.command.activate_command import ActivateCommand
from busy.model.task import Task

class TestCommandActivate(TestCase):

    def test_call(self):
        c = ActivateCommand()
        c._queue_ = Mock()
        c._queue.activate.return_value = []
        c._namespace = Mock()
        c._indices_ = [2]
        c.call_method()
        c._queue.activate.assert_called_with(2)


    def test_clean_args_today(self):
        c = ActivateCommand(None, Mock())
        c._namespace = Mock()
        c._namespace.criteria = []
        c._namespace.queue = None
        c._queue_ = Mock()
        c._queue_.plans.indices = Mock()
        c._queue_.plans.indices.return_value = [1, 3]
        c._strings_ = []
        c.clean_args()
        self.assertEqual(c._indices, [1, 3])

