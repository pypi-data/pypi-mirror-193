from unittest import TestCase
from unittest.mock import Mock

from busy.command.list_command import ListCommand

class TestCommandList(TestCase):

    def test_list_calls(self):
        c = ListCommand()
        c._queue_ = Mock()
        c._queue.list.return_value = []
        c._queue.itemclass.listfmt = ""
        c._namespace = Mock()
        c._namespace.criteria = []
        c.call_method()
        c._queue.list.assert_called_once()

    def test_list_status_1(self):
        c = ListCommand()
        c._queue_ = Mock()
        i = Mock()
        c._queue.list.return_value = [(1,i)]
        c._queue.itemclass.listfmt = ""
        c._namespace = Mock()
        c._namespace.criteria = []
        c.call_method()
        self.assertEqual(c.status, "Listed 1 Item")

    def test_list_status_2(self):
        c = ListCommand()
        c._queue_ = Mock()
        c._queue.itemclass.listfmt = ""
        i = Mock()
        j = Mock()
        c._queue.list.return_value = [(1,i), (2,j)]
        c._namespace = Mock()
        c._namespace.criteria = []
        c.call_method()
        self.assertEqual(c.status, "Listed 2 Items")

    def test_list_status_0(self):
        c = ListCommand()
        c._queue_ = Mock()
        c._queue.itemclass.listfmt = ""
        c._queue.list.return_value = []
        c._namespace = Mock()
        c._namespace.criteria = []
        c.call_method()
        self.assertEqual(c.status, "Listed nothing")

    def test_list_result(self):
        c = ListCommand()
        c._queue_ = Mock()
        i = Mock()
        i.description = "i"
        j = Mock()
        j.description = "j"
        c._queue.list.return_value = [(1,i), (2,j)]
        c._queue.itemclass.listfmt = "{1.description}"
        c._namespace = Mock()
        c._namespace.criteria = []
        r = c.call_method()
        self.assertEqual(r, "     1  i\n     2  j")
