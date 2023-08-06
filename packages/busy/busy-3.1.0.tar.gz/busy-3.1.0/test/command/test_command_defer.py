from unittest import TestCase
from unittest.mock import Mock

from busy.command.defer_command import DeferCommand

class TestCommandDefer(TestCase):

    def test_defer(self):
        c = DeferCommand()
        c._queue_ = Mock()
        i = Mock()        
        c._queue.defer.return_value = [i]
        c._namespace = Mock()
        c._namespace.criteria = []
        c._namespace.deferral = "tomorrow"
        c._indices_ = [1]
        c.call_method()
        c._queue.defer.assert_called_once()

    def test_defer_respond_nothing(self):
        c = DeferCommand()
        c._queue_ = Mock()
        c._queue.defer.return_value = []
        c._namespace = Mock()
        c._namespace.criteria = []
        c._namespace.deferral = "tomorrow"
        c._indices_ = []
        c.call_method()
        self.assertEqual(c.status, "Deferred nothing")

    def test_clean_args(self):
        c = DeferCommand(None, Mock())
        c._namespace = Mock()
        c._namespace.criteria = []
        c._namespace.deferral = "tomorrow"
        c._namespace.queue = None
        c._strings_ = []
        c.clean_args()

    def test_input_timing(self):
        u = Mock()
        u.get_string = lambda p, d: 'tomorrow'
        c = DeferCommand(None, u)
        c._namespace = Mock()
        c._namespace.criteria = []
        c._namespace.queue = None
        c._namespace.deferral = None
        c._strings_ = []
        c.clean_args()
        self.assertEqual(c._namespace.deferral, 'tomorrow')

    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\nc\nd')
    #         c = Handler(FilesystemRoot(t))
    #         c.handle('defer','2','--to','2019-09-06')
    #         o = p.read_text()
    #         self.assertEqual(o, 'a\nc\nd\n')
    #         o2 = Path(t, 'plans.txt').read_text()
    #         self.assertEqual(o2, '2019-09-06|b\n')

    # def test_defer_for(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\nc\nd')
    #         c = Handler(FilesystemRoot(t))
    #         c.handle('defer','2','--for','2019-09-06')
    #         o = p.read_text()
    #         self.assertEqual(o, 'a\nc\nd\n')
    #         o2 = Path(t, 'plans.txt').read_text()
    #         self.assertEqual(o2, '2019-09-06|b\n')

    # def test_defer_days(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\nc\nd')
    #         with mock.patch('busy.date_util.today', lambda : Date(2019,2,11)):
    #             c = Handler(FilesystemRoot(t))
    #             c.handle('defer','2','--for','1 day')
    #             o = p.read_text()
    #             self.assertEqual(o, 'a\nc\nd\n')
    #             o2 = Path(t, 'plans.txt').read_text()
    #             self.assertEqual(o2, '2019-02-12|b\n')

    # def test_defer_d(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\nc\nd')
    #         with mock.patch('busy.date_util.today', lambda : Date(2019,2,11)):
    #             c = Handler(FilesystemRoot(t))
    #             c.handle('defer','2','--for','5d')
    #             o = p.read_text()
    #             self.assertEqual(o, 'a\nc\nd\n')
    #             o2 = Path(t, 'plans.txt').read_text()
    #             self.assertEqual(o2, '2019-02-16|b\n')

    # def test_defer_with_input(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\n')
    #         c = Handler(FilesystemRoot(t))
    #         with mock.patch('sys.stdin', StringIO('2019-08-24')):
    #             c.handle('defer')
    #             o = p.read_text()
    #             self.assertEqual(o, 'b\n')
    #             o2 = Path(t, 'plans.txt').read_text()
    #             self.assertEqual(o2, '2019-08-24|a\n')

    # def test_default_tomorrow(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\n')
    #         c = Handler(FilesystemRoot(t))
    #         with mock.patch('busy.date_util.today', lambda : Date(2019,2,11)):
    #             with mock.patch('sys.stdin', StringIO(' ')):
    #                 c.handle('defer')
    #                 o2 = Path(t, 'plans.txt').read_text()
    #                 self.assertEqual(o2, '2019-02-12|a\n')

    # def test_tuesday(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\n')
    #         c = Handler(FilesystemRoot(t))
    #         with mock.patch('busy.date_util.today', lambda : Date(2019,2,14)):
    #             c.handle('defer','--to','tue')
    #             o2 = Path(t, 'plans.txt').read_text()
    #             self.assertEqual(o2, '2019-02-19|a\n')

    # def test_thursday(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\n')
    #         c = Handler(FilesystemRoot(t))
    #         with mock.patch('busy.date_util.today', lambda : Date(2019,2,14)):
    #             c.handle('defer','--to','thursday')
    #             o2 = Path(t, 'plans.txt').read_text()
    #             self.assertEqual(o2, '2019-02-21|a\n')

    # def test_capital_days(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a\nb\n')
    #         c = Handler(FilesystemRoot(t))
    #         with mock.patch('busy.date_util.today', lambda : Date(2019,2,14)):
    #             c.handle('defer','--to','THURS')
    #             o2 = Path(t, 'plans.txt').read_text()
    #             self.assertEqual(o2, '2019-02-21|a\n')

    # def test_slashes(self):
    #     with TemporaryDirectory() as t:
    #         p = Path(t, 'tasks.txt')
    #         p.write_text('a')
    #         c = Handler(FilesystemRoot(t))
    #         c.handle('defer','--to','2019/09/06')
    #         o2 = Path(t, 'plans.txt').read_text()
    #         self.assertEqual(o2, '2019-09-06|a\n')
