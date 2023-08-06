from unittest import TestCase
from unittest.mock import Mock

from busy.command.delete_command import DeleteCommand

class TestCommandDelete(TestCase):

    # def test_delete(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\nc\nd')
    #         c = Handler(FilesystemRoot(t))
    #         c.setUI(ShellUI(c))
    #         c.handle('delete','--yes','3-')
    #         o = p.read_text()
    #         self.assertEqual(o, 'a\nb\n')

    def test_call_method(self):
        c = DeleteCommand()
        c._queue_ = Mock()
        c._queue.delete.return_value = []
        c._namespace = Mock()
        c._indices_ = []
        c._namespace.yes = True
        c.call_method()
        c._queue.delete.assert_called_once()

    def test_status(self):
        c = DeleteCommand()
        c._queue_ = Mock()
        c._queue.delete.return_value = [[''],['']]
        c._namespace = Mock()
        c._namespace.yes = True
        c._indices_ = [0, 1]
        c.call_method()
        self.assertEqual(c.status, "Deleted 2 Items")

    def test_obey_confirmation(self):
        c = DeleteCommand()
        c._queue_ = Mock()
        c._queue.delete.return_value = [[''],['']]
        c._namespace = Mock()
        c._namespace.yes = False
        c._indices_ = [0, 1]
        c.call_method()
        self.assertEqual(c.status, "Delete operation unconfirmed")

    def test_clean_args_confirms(self):
        u = Mock()
        c = DeleteCommand(None, u)
        c._queue_ = Mock()
        c._queue.list.return_value = [(1,'x')]
        c._namespace = Mock() 
        c._namespace.yes = None
        c._namespace.criteria = []
        c.clean_args()
        u.get_confirmation.assert_called_with("Delete")

    def test_clean_args_sets_yes(self):
        u = Mock()
        u.get_confirmation.return_value = True
        c = DeleteCommand(None, u)
        c._queue_ = Mock()
        c._queue.list.return_value = [(1,'x')]
        c._namespace = Mock()
        c._namespace.criteria = []
        c._namespace.yes = None
        c.clean_args()
        self.assertEqual(c._namespace.yes, True)


    # def test_delete_with_input_confirmation_yes(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\nc\nd')
    #         c = Handler(FilesystemRoot(t))
    #         c.setUI(ShellUI(c))
    #         with mock.patch('sys.stdin', StringIO('Y')):
    #             c.handle('delete','3-')
    #             o = p.read_text()
    #             self.assertEqual(o, 'a\nb\n')

    # def test_delete_with_input_confirmation_no(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\nc\nd')
    #         c = Handler(FilesystemRoot(t))
    #         c.setUI(ShellUI(c))
    #         with mock.patch('sys.stdin', StringIO('no')):
    #             c.handle('delete','3-')
    #             o = p.read_text()
    #             self.assertEqual(o.strip(), 'a\nb\nc\nd')

    # def test_delete_outputs_before_confirmation(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\n')
    #         c = Handler(FilesystemRoot(t))
    #         c.setUI(ShellUI(c))
    #         o = StringIO()
    #         with mock.patch('sys.stdin', StringIO('Y')):
    #             with mock.patch('sys.stdout', o):
    #                 c.handle('delete', '1')
    #                 self.assertEqual(o.getvalue(), 'a\nDelete? (Y/n) ')

    # def test_delete_defaults_to_first_task_only(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\n')
    #         c = Handler(FilesystemRoot(t))
    #         c.setUI(ShellUI(c))
    #         with mock.patch('sys.stdin', StringIO('Y')):
    #             c.handle('delete')
    #             o = p.read_text()
    #             self.assertEqual(o, 'b\n')
