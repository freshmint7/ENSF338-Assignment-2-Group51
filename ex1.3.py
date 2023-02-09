fib_dict = {}

def func(n):
    if n in fib_dict:
        return fib_dict[n]
    if n == 0 or n == 1:
        fib_num = n
    else:
        fib_num = func(n-1) + func(n-2)
    fib_dict[n] = fib_num
    return fib_num