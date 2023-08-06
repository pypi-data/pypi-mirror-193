# A Command class handles argparse stuff (ArgumentParser and Namespace) on
# behalf of a method somewhere in the model (i.e. on Queue) and returns text
# that can be used in a UI. A Command class rarely performs an actual operation.
#
# Command classes must have the following class-level properties:
#
# ui - Name of the UI associated with this Command. Default is 'shell', set in
# base class. Inside the command, self._ui refers to the UI object itself.
#
# name - Name of the command. Used in the original Shell UI and also as the name
# of the methods on the queue.
#
# Commands must implement the following methods:
#
# @classmethod set_parser(parser) - Receives an ArgumentParser (actually a
# subparser, but that's irrelevant here), adds arguments to it as appropriate
# for that command, and keeps a reference to it in self.parser.
#
# __init__(root, ui) - Receives the Root and UI; sets self._* for both.
# Implemented in the base class.
#
# execute(namespace) - Perform the command. It might use the namespace from the
# Handler, or it might accept a new Namespace, in the event of interactive UIs.
# The execute method is expected to set a property "status" with a one-line
# string description of what happened.
#
# A Command might implement the following methods:
#
# clean_args() - Examine the self._namespace and use the UI to request any
# args that are omitted. Tends to be command-specific.
#
# They might have the following class attributes:
#
# key - For the Curses UI. What key the user should press.
#
# TODO: Move the base class to __init__.py
# TODO: Make it an ABC

from busy.util.class_family import ClassFamily

class Command(ClassFamily):

    ui = 'shell'

    @classmethod
    def set_parser(self, parser):
        self.parser = parser

    # Convenience method to add an argument to flag for confirmation in the
    # command line itself.

    @classmethod
    def _add_confirmation_arg(self, parser):
        parser.add_argument('--yes', action='store_true')

    def __init__(self, root=None, ui=None):
        self._root = root
        self._ui = ui
        self.status = None

    # Hang onto the namespace that's passed in, for use by other execute
    # methods. Note this might be different from the Handler's Namespace. This
    # one is just the abstract; others should inherit, use super, and actually
    # do something.
    #
    # There is an uncomfortable pattern here. A property is being set in a
    # non-initializer method, which methods later in the lifecycle rely on.

    def execute(self, namespace):
        self._namespace = namespace
        self.clean_args()


    # The clean_args method serves 3 purposes.
    # 
    # (1) If any arguments are missing from the command, ask the user to provide
    # them through the UI. For example, when adding a new item to a queue, if a
    # description is not yet provided, ask the user to provide one.
    # 
    # (2) This is where defaulting happens. Defaults should generally not be
    # applied in the model, but rather here in the command layer, closer to the
    # user.
    #
    # (3) Call for confirmation from the user (using is_confirmed) if
    # appropriate.
    #
    # The default is to do nothing, as this is essentially an abstract method
    # ripe for override.

    def clean_args(self):
        pass


    # Convenience method to find out whether an argument was omitted when the
    # Command was created

    def is_omitted(self, argument):
        if hasattr(self._namespace, argument):
            return not getattr(self._namespace, argument)
        return True


# Abstract base command for commands that work with one queue. A QueueCommand
# knows the reference to the Queue, and takes care of loading and saving with
# the root. A QueueCommand subclass might implement:
#
# call_method() - Call the actual method on the queue. This allows for
# specialized arguments passed into the method. If omitted, the default is to
# pass the criteria from the Namespace.

class QueueCommand(Command):

    default_queue = 'tasks'

    @classmethod
    def set_parser(self, parser):
        super().set_parser(parser)
        parser.add_argument('--queue', nargs=1, dest="queue")

    # Convenience method used by some queue commands to add criteria as an
    # argument, to allow for the selection of items from the queue. Some queue
    # commands operate on the whole queue and don't require criteria.

    @classmethod
    def _add_criteria_arg(self, parser):
        parser.add_argument('criteria', action='store', nargs="*")

    # Set the queue if it isn't designated.

    def clean_args(self):
        super().clean_args()
        if self.is_omitted('queue'):
            self._namespace.queue = [self.default_queue]


    # Get the Queue object being acted on. Remember it the first time so it's
    # easy to get the next time.

    @property
    def _queue(self):
        if not hasattr(self, '_queue_'):
            queue_name = self._namespace.queue[0]
            self._queue_ = self._root.get_queue(queue_name)
        return self._queue_


    # Many commands take criteria to get items from a queue. Here are shortcuts
    # to look up the indices and the strings only once.

    @property
    def _indices(self):
        if not hasattr(self, '_indices_'):
            self._indices_ = self._queue.indices(*self._criteria)
        return self._indices_

    @property
    def _strings(self):
        if not hasattr(self, '_strings_'):
            self._strings_ = self._queue.strings(*self._indices)
        return self._strings_


    # Convenience method to figure out whether the command is confirmed, either
    # in the original command or from the UI. Assumes indices have been set
    # based on the criteria.

    def clean_confirmation(self, verb):
        if self.is_omitted('yes'):
            if self._indices:
                value = self._ui.get_confirmation(verb)
            else:
                value = None
        else:
            value = True
        self._namespace.yes = value


    # Queues contain methods with the same name as the commands, so we really
    # just need to get it and call it.

    def execute(self, namespace):
        super().execute(namespace)
        result = self.call_method()
        self._root.save()
        return result

    # The default, which works for many queue commands, is to pass the criteria
    # into the method. This never sets the status, so not useful?

    def call_method(self):
        method = getattr(self._queue, self.name)
        method(*self._namespace.criteria)


    # Convenience method to get the criteria from the namespace, including
    # handling the case when there is none provided

    @property
    def _criteria(self):
        if hasattr(self._namespace, 'criteria'):
            return self._namespace.criteria
        else:
            return []

# Commands that are specific to the task queue inherit here. Ideally we would
# verify that the queue being used is a TodoQueue, but we're going to rely on
# defaults and argparse for that now.

class TodoCommand(QueueCommand):


    # Make sure we're using the tasks queue. Think about whether the "default"
    # queue is the same as the "required" queue for todo operations.

    def clean_args(self):
        super().clean_args()
        if self._namespace.queue != [self.default_queue]:
            message = "Todo commands only operate on the "
            message += f"{self.default_queue} queue."
            raise RuntimeError(message)