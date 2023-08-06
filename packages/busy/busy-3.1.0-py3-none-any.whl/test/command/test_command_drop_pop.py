from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch

from busy.command.drop_and_pop_command import DropCommand
from busy.command.drop_and_pop_command import PopCommand

class TestCommandDropAndPop(TestCase):

    def test_drop(self):
        c = DropCommand()
        c._queue_ = Mock()
        c._queue.drop.return_value = []
        c._namespace = Mock()
        c._namespace.criteria = []
        c.call_method()
        c._queue.drop.assert_called_once_with()

    def test_drop_respond_nothing(self):
        c = DropCommand()
        c._queue_ = Mock()
        c._queue.drop.return_value = []
        c._namespace = Mock()
        c._namespace.criteria = []
        c.call_method()
        self.assertEqual(c.status, "Dropped nothing")

    def test_drop_respond_count(self):
        c = DropCommand()
        c._queue_ = Mock()
        c._queue.drop.return_value = [Mock(), Mock(), Mock()]
        c._namespace = Mock()
        c._namespace.criteria = []
        c.call_method()
        self.assertEqual(c.status, "Dropped 3 Items")

    def test_drop_respond_description(self):
        c = DropCommand()
        c._queue_ = Mock()
        i = Mock()
        i.description = 'd'
        c._queue.drop.return_value = [i]
        c._namespace = Mock()
        c._namespace.criteria = []
        c.call_method()
        self.assertEqual(c.status, "Dropped: d")


    def test_drop_with_criteria(self):
        c = DropCommand()
        c._queue_ = Mock()
        c._queue.drop.return_value = [Mock(), Mock(), Mock()]
        c._namespace = Mock()
        c._namespace.criteria = [2]
        c.call_method()
        c._queue.drop.assert_called_once_with(2)

    def test_pop(self):
        c = PopCommand()
        c._queue_ = Mock()
        c._queue.pop.return_value = []
        c._namespace = Mock()
        c._namespace.criteria = [2,12]
        c.call_method()
        c._queue.pop.assert_called_once_with(2, 12)





    # def test_output(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\n')
    #         c = Handler(FilesystemRoot(t))
    #         o = c.handle('drop','1')
    #         self.assertIsNone(o)
