import importlib

"""
This is our Factory method to get a "handler" object
that the caller can invoke.

Other implementations can have no parameters can read
the handler name from application configurations like
Django.settings.   Or it can be a combination.
"""
def get_handler(name):
    default_module = 'rent'
    name = name if name else default_module

    try:
        module = importlib.import_module('handlers.'+name)
        return module
    except Exception:
        FactoryException().throw()



"""
This is just an Exception that implements a "throw" method
which maintains the "original" stack trace.  "raise" calls
wipe out the traceback information.
"""
import sys
class FactoryException(Exception):
    """
    This Exception class basically allows some Exception to be re-raised
    as another Exception type (eg. a business exception).

    Business-named exception would merely subclass this.
    """
    def __init__(self, exception=None):
        super(FactoryException, self).__init__()
        self.exc_info = sys.exc_info()
        self.exception = exception if exception else self.exc_info[1]

    def throw(self):
        if self.exc_info[0] and self.exc_info[1] and self.exc_info[2]:
            raise type(self), self.exception, self.exc_info[2]
        raise self
