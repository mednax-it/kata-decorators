from typing import Callable


def trace(func: Callable) -> None:
    def inner(*args, **kwargs):
        print(f'🤖: function called')
        func(*args, **kwargs)
        print(f'🤖: function returning')
    return inner


@trace
def hello(name: str) -> None:
    '''
    Says hello to the world.

    :returns: the greeting
    '''
    print(f"👋: Hello, {name}!")


hello('John')
print('---')
print(f'Function name: {hello.__name__}')
print(f'Function docstring: {hello.__doc__}')
print(f'Function annotations: {hello.__annotations__}')
