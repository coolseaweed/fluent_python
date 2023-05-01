"""
>>> avg = make_averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0
>>> avg.__code__.co_varnames
('new_value', 'total')
>>> avg.__code__.co_freevars
('series',)
>>> avg.__closure__  # doctest: +ELLIPSIS
(<cell at 0x...: list object at 0x...>,)
>>> avg.__closure__[0].cell_contents
[10, 11, 12]
"""

DEMO = """
>>> avg.__closure__
(<cell at 0x107a44f78: list object at 0x107a91a48>,)
"""


class Averager():
    """ Averager class """

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


def make_averager():
    """ make_averager function """
    # ---------- closure function ------------
    series = []  # free variable

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    # ---------------------------------------
    return averager


def new_make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total/count
    return averager


if __name__ == "__main__":
    avg_cls = Averager()
    avg_func = make_averager()
    new_avg_func = new_make_averager()
    print(avg_func(10), avg_cls(10), new_avg_func(10))
    print(avg_func(11), avg_cls(11), new_avg_func(11))
    print(avg_func(12), avg_cls(12), new_avg_func(12))

    # closure 1
    print(avg_func.__code__.co_varnames)
    print(avg_func.__code__.co_freevars)
    print(avg_func.__closure__)  # doctest: +ELLIPSIS
    print(avg_func.__closure__[0].cell_contents)

    # closure 2
    print('')
    print(new_avg_func.__code__.co_varnames)
    print(new_avg_func.__code__.co_freevars)
    print(new_avg_func.__closure__)  # doctest: +ELLIPSIS
    print(new_avg_func.__closure__[0].cell_contents,
          new_avg_func.__closure__[1].cell_contents)
