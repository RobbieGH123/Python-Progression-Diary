#Big O recap:

import time

# O(1)
def constant_time(my_list):
    return my_list[0]  # always just one step

# O(n)
def linear_time(my_list):
    total = 0
    for item in my_list:
        total += item
    return total

# O(n^2)
def quadratic_time(my_list):
    count = 0
    for i in my_list:
        for j in my_list:
            count += i * j
    return count

def measure(func, n):
    my_list = list(range(n))
    start = time.perf_counter()
    func(my_list)
    end = time.perf_counter()
    return end - start

for n in [10, 100, 1000]:
    print(f"\nInput size: {n}")
    print("O(1):", measure(constant_time, n))
    print("O(n):", measure(linear_time, n))
    print("O(n^2):", measure(quadratic_time, n))


import matplotlib.pyplot as plt

ns = [10, 100, 1000]  # keep it small so O(n^2) doesn’t freeze your laptop
o1_times = [measure(constant_time, n) for n in ns]
on_times = [measure(linear_time, n) for n in ns]
on2_times = [measure(quadratic_time, n) for n in ns]

plt.plot(ns, o1_times, label="O(1)")
plt.plot(ns, on_times, label="O(n)")
plt.plot(ns, on2_times, label="O(n^2)")
plt.xlabel("Input size (n)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.show()

