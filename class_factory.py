import sys

import importlib
  
"""
This is our Factory method to get a "handler" object
that the caller can invoke.

Other implementations can have no parameters can read
the handler name from application configurations like
Django.settings.   Or it can be a combination.
"""
def get_handler(full_path):
    parts = full_path.split(".")
    class_name = parts.pop()
    module_name = ".".join(parts)
    module = importlib.import_module(module_name)
    _class = getattr(module, class_name)
    return _class()

# python class_factory.py handlers.buy.Buy
class_instance = get_handler(sys.argv[1])
class_instance.handle()
