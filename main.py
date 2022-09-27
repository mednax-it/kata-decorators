from typing import Callable

from decorator import decorator


@decorator
def trace(func: Callable, enabled=False, *args, **kwargs) -> None:
    if enabled:
        print(f'🤖: function called')
    func(*args, **kwargs)
    if enabled:
        print(f'🤖: function returning')


@trace(enabled=True)
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
