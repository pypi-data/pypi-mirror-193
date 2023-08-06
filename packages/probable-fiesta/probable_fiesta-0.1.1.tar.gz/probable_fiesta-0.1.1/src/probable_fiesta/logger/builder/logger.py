"""Logger class."""
import logging

class Logger:

    def __init__(self, name=None, level=None, fmt=None, directory=None):
        # properties
        self.name = name
        self.level = level
        self.fmt = fmt
        self.directory = directory
        # objects
        self.logger = None 
        self.file_handler = None

    def set_logger(self, logger):
        self.logger = logger
        return self.logger

    def get_logger(self, name=None, level=None, fmt=None, directory=None):
        if name is not None:
            self.name = name
        if self.name is None:
            print("Logger Name not set. Cannot create logger.")
            return None
        if level is not None:
            self.level = level
        if self.level is None:
            self.level = self.parse_level(self.level)
            print("Logger Level: ", self.level)
        if fmt is not None:
            self.fmt = fmt
        if directory is not None:
            self.directory = directory
        # create logger
        _logger = logging.getLogger(self.name)
        _logger.setLevel(self.level)
        if self.file_handler is None:
            self.create_file_handler()
        _logger.addHandler(self.file_handler)
        self.logger = _logger
        return self.logger

    def create_file_handler(self, name=None, level=None, fmt=None, directory=None):
        if name is None:
            name = self.name
            if not name:
                print("Logger name not set. Cannot create file handler.")
                return None
        if level is None:
            level = self.level
        if fmt is None:
            fmt = self.fmt
        if directory is None:
            directory = self.directory
            if not directory:
                directory = "./"  # default directory if not set
        # create file handler
        logger_directory = f"{directory}/{name}.log"
        _file_handler = logging.FileHandler(logger_directory)
        _file_handler.setLevel(self.parse_level(level))
        _file_handler.setFormatter(fmt)
        self.file_handler = _file_handler
        return self.file_handler

    @staticmethod
    def parse_level(level):  # defaults to info
        if level is None:
            return logging.INFO
        if level == "DEBUG":
            return logging.DEBUG
        if level == "INFO":
            return logging.INFO
        if level == "WARNING":
            return logging.WARNING
        if level == "ERROR":
            return logging.ERROR
        if level == "CRITICAL":
            return logging.CRITICAL
        return logging.INFO


    def __str__(self) -> str:
        return f"Logger: {self.__dict__}"

    @staticmethod
    def new(name=None, level=None, fmt=None, directory=None):
        return Logger(name, level, fmt, directory)

    @staticmethod
    def new_get_logger(name=None, level=None, fmt=None, directory=None):
        logger = Logger.new(name, level, fmt, directory)
        return logger.get_logger()


    class Factory():
        @staticmethod
        def new_logger(name=None, level=None, fmt=None, directory=None):
            return Logger.new(name, level, fmt, directory)

        @staticmethod
        def new_file_handler(name=None, level=None, fmt=None, directory=None) -> logging.FileHandler:
            logger = Logger.new(name, level, fmt, directory)
            return logger.create_file_handler()


    factory = Factory()



