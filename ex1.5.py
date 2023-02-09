from time import perf_counter
import matplotlib.pyplot as plt

fib_dict = {}
mem_func_dict = {}
func_dict = {}
def mem_func(n):
    if n in fib_dict:
        return fib_dict[n]
    if n == 0 or n == 1:
        fib_num = n
    else:
        fib_num = mem_func(n-1) + mem_func(n-2)
    fib_dict[n] = fib_num
    return fib_num

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

for n in range(0,36):
    time_start = perf_counter()
    fib_value = func(n)
    time_stop = perf_counter()
    func_dict[n] = time_stop - time_start

for n in range(0,36):
    time_start = perf_counter()
    fib_value = mem_func(n)
    time_stop = perf_counter()
    mem_func_dict[n] = time_stop - time_start

mem_func_values = list(mem_func_dict.values())
mem_func_key = list(mem_func_dict.keys())

func_values = list(func_dict.values())
func_key = list(func_dict.keys())

plt.bar(range(len(mem_func_dict)), mem_func_values, tick_label= mem_func_key)
plt.xlabel('n')
plt.ylabel('Time (s*10^-6)')
plt.title('Timed Results for Improved Function')
plt.show()

plt.bar(range(len(func_dict)), func_values, tick_label= func_key)
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Timed Results for Original Function')
plt.show()