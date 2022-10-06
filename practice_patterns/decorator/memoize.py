from functools import wraps

def memoize(fn):
    cache = dict()
    @wraps(fn)
    def memoizer(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return memoizer


