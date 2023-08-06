from ..command.command import QueueCommand


class DeleteCommand(QueueCommand):

    name = 'delete'
    key = 'd'
    prompt = 'd)elete'

    @classmethod
    def set_parser(self, parser):
        super().set_parser(parser)
        parser.add_argument('--yes', action='store_true')
        self._add_criteria_arg(parser)


    # TODO: Move more of this into clean_confirmation
    # TODO: Make a convenience method to set the default

    def clean_args(self):
        super().clean_args()
        if self.is_omitted('criteria'):
            self._namespace.criteria = [1]
        self.clean_confirmation("Delete")

    # Assume the indices have been already set, before confirmation.

    def call_method(self):
        if self._namespace.yes:
            deleted = self._queue.delete(*self._indices)
            if len(deleted) == 1:
                item = deleted[0]
                self.status = f"Deleted: {item.description}"
            elif deleted:
                self.status = f"Deleted {len(deleted)} Items"
            else:
                self.status = "Deleted nothing"
        else:
            self.status = "Delete operation unconfirmed"

    def execute_on_queue(self, parsed, queue):
        itemlist = queue.list(*parsed.criteria or [1])
        indices = [i[0]-1 for i in itemlist]
        if self.confirmed(parsed, itemlist, 'Delete'):
            queue.delete_by_indices(*indices)
