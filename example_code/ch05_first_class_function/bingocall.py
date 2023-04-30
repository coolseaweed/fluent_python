"""
# BEGIN BINGO_DEMO

>>> bingo = BingoCage(range(3))
>>> bingo.pick()
1
>>> bingo()
0
>>> callable(bingo)
True

# END BINGO_DEMO

"""

# BEGIN BINGO

import random


class BingoCage:

    def __init__(self, items):
        self._items = list(items)  # <1>
        random.shuffle(self._items)  # <2>

    def pick(self) -> int:  # <3>
        """ pick a random item, removing it from the cage"""
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')  # <4>

    def __call__(self):  # <5>
        return self.pick()


# END BINGO
if __name__ == '__main__':
    bingo = BingoCage(range(3))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))
    print(bingo.pick.__annotations__)

    class C:
        pass
    obj = C()
    def func(): pass
    res = sorted(set(dir(func)) - set(dir(obj)))

    print(res)
    print(obj.__dir__())
