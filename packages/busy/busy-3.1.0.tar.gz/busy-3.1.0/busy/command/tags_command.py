from ..command.command import QueueCommand


class TagsCommand(QueueCommand):

    name = 'tags'

    def call_method(self):
        return '\n'.join(sorted(self._queue.tags()))
