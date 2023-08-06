from .command import TodoCommand


# Returns the top task from the queue, without tags, a resource, or followons.

class BaseCommand(TodoCommand):

    name = "base"

    def call_method(self):
        return self._queue.base()
