from unittest import TestCase
from unittest.mock import Mock

from busy.command.queues_command import QueuesCommand

class TestCommandQueues(TestCase):

    def test_queues(self):
        r = Mock()
        r.queue_names = ['a','b']
        c = QueuesCommand(r)
        x = c.execute(None)
        self.assertEqual(x, 'a\nb')
