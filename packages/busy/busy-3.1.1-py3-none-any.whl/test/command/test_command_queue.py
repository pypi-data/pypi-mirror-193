from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch
# from tempfile import TemporaryDirectory
# from pathlib import Path
# from io import StringIO
# from datetime import date as Date

from busy.command.command import QueueCommand

class TestCommandQueue(TestCase):

    @patch('busy.command.command.QueueCommand.is_omitted', lambda s, a: True)
    def test_omitted_args_default(self):
        c = QueueCommand()
        n = Mock()
        c._namespace = n
        c.clean_args()
        self.assertEqual(['tasks'], c._namespace.queue)

    @patch('busy.command.command.QueueCommand.is_omitted', lambda s, a: False)
    def test_omitted_args_not_default(self):
        c = QueueCommand()
        n = Mock()
        n.queue = ['g']
        c._namespace = n
        c.clean_args()
        self.assertEqual(['g'], c._namespace.queue)

    # These are more like integration tests

    # def test_get_from(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'a.txt')
    #         p.write_text('b\n')
    #         c = Handler(FilesystemRoot(t))
    #         o = c.handle('top','--queue','a')
    #         self.assertEqual(o, 'b')

    # def test_default_queue(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('b\n')
    #         c = Handler(FilesystemRoot(t))
    #         o = c.handle('get')
    #         self.assertEqual(o, 'b')

    # def test_add(self):
    #     with TemporaryDirectory() as t:
    #         c = Handler(FilesystemRoot(t))
    #         with mock.patch('sys.stdin', StringIO('g')):
    #             c.handle('add','--queue','j')
    #             x = Path(t, 'j.txt').read_text()
    #             self.assertEqual(x, 'g\n')

    # def test_drop(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'u.txt')
    #         p.write_text('a\nb\nc\nd')
    #         c = Handler(FilesystemRoot(t))
    #         c.handle('drop','2','4','--queue','u')
    #         o = p.read_text()
    #         self.assertEqual(o, 'a\nc\nb\nd\n')

    # def test_delete(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'w.txt')
    #         p.write_text('a\nb\nc\nd')
    #         c = Handler(FilesystemRoot(t))
    #         c.handle('delete','--yes','3-', '--queue', 'w')
    #         o = p.read_text()
    #         self.assertEqual(o, 'a\nb\n')

    # def test_manage(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'y.txt')
    #         p.write_text('a\n')
    #         with mock.patch('busy.editor', lambda x: 'b\n'):
    #             c = Handler(FilesystemRoot(t))
    #             c.handle('manage', '--queue', 'y')
    #             f = p.read_text()
    #             self.assertEqual(f, 'b\n')
