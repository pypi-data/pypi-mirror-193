from functools import wraps

__all__ = 'composed', 'collect', 'squeeze'

from typing import Callable, Sequence


def composed(*func_and_args, **kwargs):
    """
    Decorate a function to create a composition.
    Returns a function that applies the decorated function and then the decorator's argument in a sequence.

    >>> @composed(list)
    ... def squares(n):
    ...     for i in range(n):
    ...         yield i ** 2
    >>> squares(4) # not a generator anymore
    [0, 1, 4, 9]
    >>> @composed(dict)
    ... def vals_to_squares(values):
    ...     for v in values:
    ...         yield v, v ** 2
    >>> vals_to_squares([3, 2, 8]) # the pairs are gathered in a dict
    {3: 9, 2: 4, 8: 64}
    >>> @composed(numpy.stack, axis=-1)  # pass additional arguments
    ... def animate_noise(n_frames):
    ...     for i in range(n_frames):
    ...         noise = numpy.random.uniform if i % 2 else numpy.random.normal
    ...         yield noise(size=(10, 10))
    >>> animate_noise(7).shape # stacked along the last axis (axis=-1)
    (10, 10, 7)
    """

    if not func_and_args:
        raise TypeError('func argument is required')
    func, *args = func_and_args

    def decorator(decorated: Callable):
        @wraps(decorated)
        def wrapper(*args_, **kwargs_):
            return func(decorated(*args_, **kwargs_), *args, **kwargs)

        return wrapper

    return decorator


def collect(func):
    """
    Decorate a generator and return a function, that returns a list instead.

    Examples
    --------
    >>> @collect
    ... def odd_numbers(n):
    ...     for i in range(n):
    ...         yield 2 * i + 1
    >>> odd_numbers(3) # not a generator anymore
    [1, 3, 5]
    """
    return composed(list)(func)


def squeeze(values: Sequence):
    """ Remove the first dimension in case it is singleton. """
    if len(values) == 1:
        values = values[0]
    return values
