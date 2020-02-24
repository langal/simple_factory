import factory

handlers = ('rent', 'buy', 'rtk', 'return')

for name in handlers:
    assert(factory.get_handler(name))

print("TEST PASSED - did not get an import exception")
