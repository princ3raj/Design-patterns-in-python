

sum_cache = {0:0}
def number_sum(n):
    '''Returns sum of first n numbers'''
    assert (n >= 0), 'n must be >= 0'

    if n in sum_cache:
        return sum_cache[n]
    res = n + number_sum(n-1)
    sum_cache[n] = res
    return res


from timeit import Timer

if __name__ == "__main__":
    t = Timer('number_sum(300)', 'from __main__ import number_sum')
    print("Time: ", t.timeit())
