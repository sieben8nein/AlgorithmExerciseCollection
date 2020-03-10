import math
import random
def mergesort(A, p, r):
    if(p<r):
        q = math.floor((p+r)/2)
        mergesort(A, p, q)
        mergesort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [] * (n1+1)
    for i in range(1, n1-1):
        L[i] = A[p+i-1]
    R = [] * (n2+1)
    for j in range(1, n2-1):
        R[j] = A[q+j]
    L.append(math.inf)
    R.append(math.inf)
    i = 0
    j = 0
    for k in range(p, r):
        print("p:", p, "r:", r)
        print(k)
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


nrList = random.sample(range(0, 100), 16)
print(nrList)
mergesort(nrList, 0, 15)
print(nrList)




