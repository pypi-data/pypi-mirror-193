from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch

from busy.command.edit_command import EditCommand
from busy.queue.queue import Queue


class TestCommandEdit(TestCase):
    
    def test_manage_one_status(self):
        i = Mock()
        i.description = 'k'
        u = Mock()
        u.edit_items.return_value = [i]
        c = EditCommand(None, u)
        q = Queue(items=['a #b at c --> d','e'])
        c._namespace = Mock()
        c._namespace.criteria = [1]
        c._indices_ = [1]
        c._queue_ = q
        c.call_method()
        self.assertEqual(c.status, 'Edited: k')


    # def test_clean_args_gets_list(self):
    #     c = EditCommand(None, Mock())
    #     c._queue_ = Mock()
    #     c._queue_.list.return_value = [(1,'f')]
    #     c._namespace = Mock()
    #     c._namespace.criteria = None
    #     c.clean_args()
    #     self.assertEqual(c._indices, [0])

    # def test_clean_args_does_no_output(self):
    #     u = Mock()
    #     c = EditCommand(None, u)
    #     c._queue_ = Mock()
    #     c._queue_.list.return_value = [(1,'f')]
    #     c._namespace = Mock()
    #     c._namespace.criteria = None
    #     c.clean_args()
    #     u.output.assert_not_called()

    # def test_edit_text_called(self):
    #     u = Mock()
    #     c = EditCommand(None, u)
    #     c._queue_ = Mock()
    #     c._queue_.list.return_value = [(1,'f')]
    #     c._namespace = Mock()
    #     c._namespace.criteria = []
    #     c.call_method()
    #     u.edit_items.assert_called()


        # with TemporaryDirectory() as t:
        #     p = Path(t, 'tasks.txt')
        #     p.write_text('a\n')
        #     with mock.patch('busy.editor', lambda x: 'b\n'):
        #         c = Handler(FilesystemRoot(t))
        #         o = c.handle('manage')
        #         f = p.read_text()
        #         self.assertEqual(f, 'b\n')

    # def test_manage_includes_newline_at_end(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\n')
    #         m = Mock()
    #         m.return_value = 'b\n'
    #         with mock.patch('busy.editor', m):
    #             c = Handler(FilesystemRoot(t))
    #             o = c.handle('manage')
    #             m.assert_called_with('a\n')

    # def test_leave_tasks_in_place(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\n')
    #         with mock.patch('busy.editor', lambda x: 'a\n'):
    #             c = Handler(FilesystemRoot(t))
    #             o = c.handle('manage', '1')
    #             f = p.read_text()
    #             self.assertEqual(f, 'a\nb\n')

    # def test_last_record(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\n')
    #         with mock.patch('busy.editor', lambda x: 'c\n'):
    #             c = Handler(FilesystemRoot(t))
    #             o = c.handle('manage', '-')
    #             f = p.read_text()
    #             self.assertEqual(f, 'a\nc\n')
