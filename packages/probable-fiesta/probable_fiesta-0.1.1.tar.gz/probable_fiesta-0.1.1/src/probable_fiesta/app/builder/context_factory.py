"""Context Factory class."""
from .context import Context
from ...command.builder.command_queue import CommandQueue
from ...command.builder.command_factory import CommandFactory

class ContextFactory:
    @staticmethod
    def new_context(name=None, command_queue=None):
        return Context(name, command_queue)

    @staticmethod
    def new_context_one_new_command(context_name, command_name, function, *args):
        cq = CommandQueue.new(CommandFactory.new_command(command_name, function, *args))
        context = ContextFactory.new_context(context_name, cq)
        return context

    @staticmethod
    def new_context_one_command(context_name, command):
        cq = CommandQueue.new(command)
        context = ContextFactory.new_context(context_name, cq)
        return context