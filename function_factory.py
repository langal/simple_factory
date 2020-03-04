import sys

import importlib
  
"""
This is our Factory method to get a "handler" function
that the caller can invoke.

Other implementations can have no parameters can read
the handler name from application configurations like
Django.settings.   Or it can be a combination.
"""
def get_handler(module_name, name):
    if not module_name:
        module = sys.modules[__name__]
    else:
        module = importlib.import_module(module_name)
    function = getattr(module, name, False)
    if function:
        return function
    else:
        raise Exception("Unable to find function {}".format(name))


# call the function
# python function_factory.py 'handlers.buy' post_handle
function = get_handler(sys.argv[1], sys.argv[2])
function()
