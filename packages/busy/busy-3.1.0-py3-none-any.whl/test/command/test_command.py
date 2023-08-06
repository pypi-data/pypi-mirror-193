from unittest import TestCase
from unittest.mock import Mock

from busy.command.command import QueueCommand

class TestCommand(TestCase):

    def test_queue_command_execute(self):
        c = QueueCommand()
        c._root = Mock()
        c.call_method = lambda: 'a'
        n = Mock()
        n.queue = ['q']
        r = c.execute(n)
        self.assertEqual(r, 'a')