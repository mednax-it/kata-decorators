# Decorators Kata

This mini-kata explores Python decorators.

## Introduction

This project is super-simple. All code should happen in `main.py`.

- Initial setup: `poetry install`
- Running: `poetry run python main.py`

All the steps below have corresponding branches—`step1-implemented`, `step2-implemented`, etc.—that contain one possible implementation of that particular step. Feel free to use those branches or to create your own implementations. (And if you do create your own, may I suggest branches like `step1`, `step2`?)

Run the basic program once without any changes. What is the output? What does it show for the function metadata?

## Steps

1. Wrap the `hello()` function—without using the decorator syntax—in a `trace()` function so that you get the following output:
   ```
   🤖: function called
   👋: Hello, world!
   🤖: function returning
   ```
   What happened to the function metadata?
1. Use the [decorator syntax](https://peps.python.org/pep-0318/#current-syntax) to wrap `hello()` with `@trace`. Now what happened to the function metadata? _Hint: your `trace()` needs to use a nested function._
1. Modify `hello()` to accept a `name` string. Use that `name` in the greeting, so that `hello('John')` produces:
   ```
   🤖: function called
   👋: Hello, John!
   🤖: function returning
   ```
   _Hint: you can pass `*args, **kwargs` from the inner function through to the wrapped function._
1. Support passing an `enabled` keyword argument to the `@trace` decorator.
   - if `True`, `@trace` should print out the additional logging
   - if `False`, `@trace` should not print out the additional logging
   - `enabled` should be set to `False` by default
     _Hint: you'll need to add another layer of nested functions._
1. Use the [decorator](https://pypi.org/project/decorator/) `@decorator` to simplify the implementation. Note that you'll need to add this dependency first via `poetry add decorator`. When we use `@decorator`, what happens to our function metadata? _Hint: all nested functions collapse, including their arguments, into a single, un-nested function._

One final note: we could also use [the built-in @wraps decorator](https://docs.python.org/3/library/functools.html#functools.wraps) from the `functools` module to simplify our decorator. Like `@decorator`, `@wraps` preserves function metadata; however, it does not collapse the nested functions. It is for that reason that I still prefer `@decorator` for all your custom decorating needs.
