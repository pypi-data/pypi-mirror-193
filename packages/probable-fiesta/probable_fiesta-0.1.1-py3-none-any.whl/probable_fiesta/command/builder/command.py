"""Command class."""
class Command:

    def __init__(self, name, function, *args):
        self.name = name
        self.function = function
        self.args = args

    def __str__(self):
        return f"Command: {self.__dict__}"

    def invoke(self):
        if self.function is not None and self.args is not None:
            if self.args[0] is not None:
                return self.function(*self.args)
            return self.function()
        #elif self.function is not None and self.args is None:
            #return self.function()
        return None

    class Factory():

        @staticmethod
        def new_command(name, function, *args):
            return Command(name, function, *args)
    
    factory = Factory()
