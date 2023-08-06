from curses import echo, noecho
from busy.util import date_util

from ..command.command import TodoCommand


class DeferCommand(TodoCommand):

    name = 'defer'
    key = 'f'

    @classmethod
    def set_parser(self, parser):
        super().set_parser(parser)
        parser.add_argument('--deferral', '--to', '--for')
        self._add_criteria_arg(parser)


    def clean_args(self):
        super().clean_args()
        if self.is_omitted('criteria'):
            self._namespace.criteria = [1]
        self._ui.output('\n'.join(self._strings))
        if self.is_omitted('deferral'):
            deferral = self._ui.get_string("Deferral", "tomorrow")
            self._namespace.deferral = deferral
        self.clean_confirmation(f"Defer to {self._date}")

    @property
    def _date(self):
        if not hasattr(self, '_date_'):
            self._date_ = date_util.relative_date(self._namespace.deferral)
        return self._date_


    def call_method(self):
        if not self._indices:
            self.status = "Deferred nothing"
        elif not self._namespace.yes:
            self.status = "Defer operation unconfirmed"
        else:
            deferred = self._queue.defer(*self._indices, date=self._date)
            if len(deferred) == 1:
                item = deferred[0]
                self.status = f"Deferred: {item.description} // To: {item.date}"
            else:
                item = deferred[0]
                self.status = f"Deferred {str(len(deferred))} Items to {item.date}"
