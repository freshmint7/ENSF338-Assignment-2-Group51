import sys
import json
import matplotlib.pyplot as plt
from time import perf_counter

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

quicksort_dict = {}
with open("ex2.json") as json_file:
    data = json.load(json_file)

for i in range(0, len(data)):
    time_start = perf_counter()
    func1(data[i], 0, len(data[i])-1)
    time_stop = perf_counter()
    quicksort_dict[i] =  time_stop - time_start

quicksort_times = list(quicksort_dict.values())
quicksort_index = list(quicksort_dict.keys())

plt.bar(range(len(quicksort_dict)), quicksort_times, tick_label= quicksort_index)
plt.xlabel('nth Array in the ex2.json')
plt.ylabel('Time')
plt.title('Timed Results for QuickSort Function for ex2.json')
plt.show()

