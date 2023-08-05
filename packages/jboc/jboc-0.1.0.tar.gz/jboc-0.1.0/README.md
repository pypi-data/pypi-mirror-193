## No dependencies, no paradigm - Just a Bunch Of Code

A small collection of some useful code that didn't fit into any package that I know of.

# Examples

Turn a generator function into a function that returns a list:

```python
from jboc import collect


@collect
def odd_numbers(n):
    for i in range(n):
        yield 2 * i + 1


# not a generator anymore
odd_numbers(3) == [1, 3, 5] 
```

Same as before, but gather the values into a different container, e.g. a dict:

```python
from jboc import composed


@composed(dict)
def vals_to_squares(values):
    for v in values:
        yield v, v ** 2


# the pairs are gathered in a dict
vals_to_squares([3, 2, 8]) == {3: 9, 2: 4, 8: 64}
```

# Install

```shell
pip install jboc
```
