from unittest import TestCase
from unittest.mock import Mock
from unittest.mock import patch
from datetime import date as Date

from busy.command.finish_command import FinishCommand

class TestCommandFinish(TestCase):

    def test_call(self):
        c = FinishCommand()
        c._queue_ = Mock()
        c._queue_.finish.return_value = [[],[],[]]
        c._queue_.list.return_value = [(1,'x')]
        c._namespace = Mock()
        # c._namespace.criteria = []
        c._namespace.yes = True
        c._namespace.timing = "today"
        c._indices_ = [0]
        c.call_method()
        c._queue.finish.assert_called_once()

    def test_confirm_description(self):
        c = FinishCommand()
        c._queue_ = Mock()
        c._queue_.list.return_value = [(1,'x'),(3,'z')]
        c._namespace = Mock()
        c._namespace.yes = None
        c._namespace.queue = None
        c._namespace.criteria = [1,3]
        c._namespace.timing = None
        c._ui = Mock()
        c._ui.get_confirmation.return_value = True
        c._strings_ = []
        with patch('busy.util.date_util.today', lambda : Date(2019,2,11)):
            c.clean_args()
            c._ui.get_confirmation.assert_called_with('Finished on 2019-02-11')

    def test_status_one(self):
        c = FinishCommand()
        c._queue_ = Mock()
        t = Mock()
        t.description = 'foo'
        c._queue_.finish.return_value = [[t],[],[]]
        c._namespace = Mock()
        c._namespace.criteria = []
        c._namespace.yes = True
        c._namespace.timing = "today"
        c._indices_ = [0]
        c.call_method()
        self.assertEqual(c.status, "Finished: foo")

    def test_status_multiple(self):
        c = FinishCommand()
        c._queue_ = Mock()
        c._queue_.finish.return_value = [['',''],[''],['']]
        c._namespace = Mock()
        c._namespace.criteria = []
        c._namespace.yes = True
        c._namespace.timing = "today"
        c._indices_ = [0]
        c.call_method()
        self.assertEqual(c.status, "Finished 2 Items // Added 1 // Repeated 1")

    def test_status_unconfirmed(self):
        c = FinishCommand()
        c._queue_ = Mock()
        c._queue_.finish.return_value = [['',''],[''],['']]
        c._namespace = Mock()
        c._namespace.criteria = []
        c._namespace.yes = None
        c._indices_ = [0]
        c.call_method()
        self.assertEqual(c.status, "Finish operation unconfirmed")

    def test_status_none(self):
        c = FinishCommand()
        c._queue_ = Mock()
        c._queue_.finish.return_value = [[],[],[]]
        c._namespace = Mock()
        c._namespace.criteria = []
        c._namespace.yes = True
        c._indices_ = []
        c.call_method()
        self.assertEqual(c.status, "Finished nothing")


    def test_default_criteria_in_clean_args(self):
        u = Mock()
        u.get_string = lambda d: 'f'
        c = FinishCommand(None, u)
        c._queue_ = Mock()
        c._queue_.list.return_value = []
        c._namespace = Mock()
        c._namespace.criteria = []
        c._namespace.queue = None
        c._namespace.timing = "today"
        c._strings_ = []
        c.clean_args()
        self.assertEqual(c._namespace.criteria, [1])

    def test_default_today(self):
        u = Mock()
        # u.get_string = lambda d: 'f'
        c = FinishCommand(None, u)
        c._queue_ = Mock()
        c._queue_.list.return_value = []
        c._namespace = Mock()
        c._namespace.criteria = []
        c._namespace.queue = None
        c._namespace.timing = None
        c._strings_ = []
        with patch('busy.util.date_util.today', lambda : Date(2019,2,11)):
            c.clean_args()
            self.assertEqual(c._date, Date(2019, 2, 11))

