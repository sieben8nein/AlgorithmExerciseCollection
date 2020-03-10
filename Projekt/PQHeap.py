import random
import math

def insert(A, input):
    A.append(input)
    i = len(A) - 1
    while i >= 0 and A[parent(i)] > A[i]:
        x = A[parent(i)]
        A[parent(i)] = A[i]
        A[i] = x
        i = parent(i)



def extractMin(A):
    if len(A) < 1:
        return ("error")
    min = A.pop(0)
    build_min_heap(A)
    return min

def build_min_heap(A):
    length = len(A)
    for i in reversed(range(math.floor(length/2))):
        min_heapify(A, i)

def min_heapify(A, i):
    l = left(i)
    r = right(i)
    if(l <= len(A)-1 and A[l] < A[i]):
        lowest = l
    else:
        lowest = i
    if(r <= len(A)-1 and A[r] < A[lowest]):
        lowest = r
    if lowest != i:
        x = A[lowest]
        A[lowest] = A[i]
        A[i] = x
        min_heapify(A, lowest)

def parent(i):
    if i == 0:
        return 0
    return math.floor((i-1)/2)

def left(i):
    if(i == 0):
        return 1
    else:
        return (2*i) + 1

def right(i):
    if(i == 0):
        return 2
    else:
        return (2*i)+2

# A = random.sample(range(0, 60), 10)
# print(A)
# #B = [random.randrange(1, 101, 1) for _ in range(10)]
# pq = []
# for i in range(len(A)):
#     insert(pq, A[i])
#     print(pq)
#
# while len(pq) > 1:
#     print(extractMin(pq))
#     print(pq)
