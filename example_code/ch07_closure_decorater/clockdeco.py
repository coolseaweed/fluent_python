# clockdeco.py

import time
import functools


def clock(func):
    def clocked(*args):
        t0 = time.time()
        result = func(*args)
        elapsed = time.time() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


def clock2(func):
    """ clock decorator """
    @functools.wraps(func)  # preserve the information of func (__doc__, __name__)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            temp = ', '.join(repr(arg) for arg in args)
            arg_lst.append(temp)
        if kwargs:
            pairs = [f"{k}={w}" for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    """ factorial function """
    return 1 if n < 2 else n*factorial(n-1)


@clock2
def snooze2(seconds):
    time.sleep(seconds)


@clock2
def factorial2(n, *arg, **kwargs):
    """ factorial function """
    return 1 if n < 2 else n*factorial(n-1)


if __name__ == '__main__':
    # clock DEMO
    print(f" --------- clock Demo ---------")
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
    print(f"name: {factorial.__name__}")
    print(f"doc: {factorial.__doc__}")
    print(factorial.__closure__)
    print(factorial.__closure__[0].cell_contents)

    # clock2 DEMO
    print(f" --------- clock2 Demo ---------")
    print(f"clock2.__name__: {clock2.__name__}")
    print('*' * 40, 'Calling snooze(.123)')
    snooze2(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial2(6, 1, 'a', 3, b=2))
    print(f"name: {factorial2.__name__}")
    print(f"doc: {factorial2.__doc__}")
    print(factorial2.__closure__)
    print(factorial2.__closure__[0].cell_contents)
