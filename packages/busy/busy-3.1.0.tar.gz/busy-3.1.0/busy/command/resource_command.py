from ..command.command import TodoCommand


# Get the resource (a URL) for the top entry in a queue

class ResourceCommand(TodoCommand):

    name = "resource"

    def call_method(self):
        return str(self._queue.resource() or '')
