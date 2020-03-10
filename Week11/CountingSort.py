import math
import random


def counting_sort(A, B, k):
    C = [0] * (k+1)
    for j in range(0, len(A)-1):
        C[A[j]] = C[A[j]] + 1
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
    for i in range(len(A)-1, 0, -1):
        print(A[i])
        print(C[A[i]])
        B[C[A[i]]-1] = A[i]
        C[A[i]] = C[A[i]] - 1


k = 300
nrList = random.sample(range(1, k), 8)
print(nrList)
B = [0] * (len(nrList))
counting_sort(nrList, B, k)
print(B)
