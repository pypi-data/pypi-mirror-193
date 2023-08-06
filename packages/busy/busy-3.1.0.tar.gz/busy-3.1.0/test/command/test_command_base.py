from unittest import TestCase
from unittest.mock import Mock

from busy.command.base_command import BaseCommand
from busy.queue.todo_queue import TodoQueue

class TestBaseCommand(TestCase):

    def test_it(self):
        q = TodoQueue(items=['a #b at c --> d','e'])
        c = BaseCommand()
        c._namespace = Mock()
        c._namespace.criteria = []
        c._queue_ = q
        x = c.call_method()
        self.assertEqual(x, 'a')
