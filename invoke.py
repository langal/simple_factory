import factory
import sys

"""
"experiment_name" can be "version", "variation", etc.

It could reqdaily be obtained from some app configuration like Django settings
"""

experiment_name = sys.argv[1] if len(sys.argv) > 1 else None
handler = factory.get_handler(experiment_name)
handler.handle()
handler.post_handle()
