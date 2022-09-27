def hello() -> None:
    '''
    Says hello to the world.

    :returns: the greeting
    '''
    print(f"👋: Hello, world!")

hello()
print('---')
print(f'Function name: {hello.__name__}')
print(f'Function docstring: {hello.__doc__}')
print(f'Function annotations: {hello.__annotations__}')
