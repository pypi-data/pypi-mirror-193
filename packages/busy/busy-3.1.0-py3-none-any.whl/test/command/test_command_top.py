from unittest import TestCase
from unittest.mock import Mock

from busy.command.top_command import TopCommand
from busy.queue.queue import Queue

class TestCommandGet(TestCase):

    def test_call_method(self):
        c = TopCommand()
        c._queue_ = Mock()
        c._namespace = Mock()
        c.call_method()
        c._queue.top.assert_called_once_with()
        self.assertIsNone(c.status)

    def test_call_method_empty_queue(self):
        c = TopCommand()
        c._queue_ = Mock()
        c._queue.top = lambda: None
        c._namespace = Mock()
        c.call_method()
        self.assertTrue(len(c.status) > 10)
    
    def test_deep(self):
        q = Queue(items=['a #b at c --> repeat tomorrow', 'd #e at f'])
        c = TopCommand()
        c._queue_ = q
        x = c.call_method()
        self.assertEqual(x, 'a #b at c --> repeat tomorrow')