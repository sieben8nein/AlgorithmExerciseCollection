import random

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q +1 , r)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r-1):
        if A[j] <= x:
            i = i+1
            y = A[i]
            A[i] = A[j]
            A[j] = y
    z = A[i+1]
    A[i+1] = A[r]
    A[r] = z
    return i+1


nrList = random.sample(range(0, 100), 8)
print(nrList)
quicksort(nrList, 0, len(nrList)-1)
print(nrList)