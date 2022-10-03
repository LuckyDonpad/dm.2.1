import subsets
import permutations
from time import time
from math import factorial
import matplotlib as plt
from matplotlib import pyplot

plt.use('TkAgg')
for n in [5, 7, 9]:
    combs = []
    for k in range(n + 1):
        combinations = factorial(n) / (factorial(k) * factorial(n - k))
        combs.append(combinations)
    plt.pyplot.plot(combs)
    plt.pyplot.savefig("combinations n = " + str(n) + '.jpeg')

seq = []
subsets_time = []
for i in range(1, 26):
    seq.append(i)
    start_time = time()
    for _ in subsets.subsets_generator(seq):
        pass
    end_time = time()
    subsets_time.append(end_time - start_time)
    print(i, subsets_time[-1])
plt.pyplot.plot(subsets_time)
plt.pyplot.savefig("subsets time.jpeg")

permutations_time = []
for i in range(1, 12):
    start_time = time()
    for _ in permutations.permutation_generator(i):
        pass
    end_time = time()
    permutations_time.append(end_time - start_time)
    print(i, permutations_time[-1])
plt.pyplot.plot(permutations_time)
plt.pyplot.savefig("permutations time.jpeg")

n_placements = []
for n in [5, 7, 9]:
    for k in range(n + 1):
        placement = factorial(n) / factorial(n - k)
        n_placements.append(placement)
    plt.pyplot.plot(n_placements)
    plt.pyplot.savefig("n_placements n = " + str(n) + ".jpeg")
