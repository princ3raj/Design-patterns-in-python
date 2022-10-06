cache_fib = {0:0, 1:1}


def fibonacci(n):
    '''Return the suite of fibonnaci numbers'''
    assert(n >= 0), "n must be >= 0"

    if n in cache_fib:
        return cache_fib[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    cache_fib[n] = res
    return res