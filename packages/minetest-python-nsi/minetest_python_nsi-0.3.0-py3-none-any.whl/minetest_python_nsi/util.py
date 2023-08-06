import collections
import math


def intFloor(*args):
    return [int(math.floor(x)) for x in flatten(args)]


def flatten(l):
    for e in l:
        if isinstance(e, collections.abc.Iterable) and not isinstance(e, str):
            for ee in flatten(e):
                yield ee
        else:
            yield e


def flatten_parameters_to_string(l):
    return ",".join(map(str, flatten(l)))
