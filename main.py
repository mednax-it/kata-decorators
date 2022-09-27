from typing import Callable


def trace(func: Callable) -> None:
    print(f'🤖: function called')
    func()
    print(f'🤖: function returning')


def hello() -> None:
    '''
    Says hello to the world.

    :returns: the greeting
    '''
    print(f"👋: Hello, world!")


trace(hello)
print('---')
print(f'Function name: {hello.__name__}')
print(f'Function docstring: {hello.__doc__}')
print(f'Function annotations: {hello.__annotations__}')
