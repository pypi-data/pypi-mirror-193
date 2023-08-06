
from .command import QueueCommand
import busy


class EditCommand(QueueCommand):

    name = 'edit'
    key = 'e'

    @classmethod
    def set_parser(self, parser):
        super().set_parser(parser)
        self._add_criteria_arg(parser)

    def clean_args(self):
        super().clean_args()
        if self.is_omitted('criteria'):
            self._namespace.criteria = [1]


    # TODO: Methods to get indices and items as separate lists

    def call_method(self):
        if not self._indices:
            self.status = "Edited nothing"
        else:
            itemclass = self._queue.itemclass
            old = self._queue.items(*self._indices)
            new = self._ui.edit_items(itemclass, *old)
            self._queue.replace(self._indices, new)
            if len(new) == 1:
                status = f"Edited: {new[0].description}"
            else:
                status = f"Edited {str(len(new))} Items"
            self.status = status
