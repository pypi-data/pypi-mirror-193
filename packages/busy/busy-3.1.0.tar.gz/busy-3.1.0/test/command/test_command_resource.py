from unittest import TestCase
from unittest.mock import Mock
from io import StringIO
from datetime import date as Date

from busy.command.resource_command import ResourceCommand
from busy.queue.todo_queue import TodoQueue

class TestCommandResource(TestCase):

    def test_resource(self):
        q = TodoQueue(items=['a at g', 'b at h'])
        c = ResourceCommand()
        c._queue_ = q
        rx = c.call_method()
        self.assertEqual(rx, 'g')

    # def test_get_without_resource(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a at g\n')
    #         c = Handler(FilesystemRoot(t))
    #         o = c.handle('get-without-resource')
    #         self.assertEqual(o, 'a')
