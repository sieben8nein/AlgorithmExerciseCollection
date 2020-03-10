import random
import time

def insertionSort(Arr):
    j = 1
    for x in range(j, len(Arr)-1):
        key = Arr[x]
        i = x - 1
        while (i >= 0) and (Arr[i] > key):
            Arr[i + 1] = Arr[i]
            i = i - 1
        Arr[i + 1] = key

nrList = random.sample(range(0, 100), 16)
print(nrList)
pre = time.time_ns()
print(pre)
insertionSort(nrList)
print("this took:", time.time_ns(), pre)
print(nrList)
