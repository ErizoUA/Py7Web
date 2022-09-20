# exec(object, global, locals) - > None

test = 'global test'


def example_one():
    foo = 16
    loc = locals()
    print(f'Before: {loc}')
    exec('baz = foo + 10')  # , {}, loc
    print(f'After: {loc}')
    baz = loc['baz']
    print(baz)


def example_two():
    foo = 16
    baz = 10
    loc = locals()
    print(f'Before: {loc}')
    exec('foo = foo + 1')
    print(f'After: {loc}')
    print(foo)


def example_third():
    foo = 16
    baz = 10
    loc = {'foo': 11, 'baz': baz}
    print(f'Before: {loc}')
    exec('foo = foo + 1', globals(), loc)
    print(f'After: {loc}')
    foo = loc['foo']
    print(foo)


if __name__ == '__main__':
    print('Example #1')
    example_one()
    print('Example #2')
    example_two()
    print('Example #3')
    example_third()
