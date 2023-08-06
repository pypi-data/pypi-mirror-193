from ..command.command import Command


class QueuesCommand(Command):

    name = 'queues'

    def execute(self, namespace):
        names = sorted(self._root.queue_names)
        return '\n'.join(names)
