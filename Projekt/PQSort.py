import sys

from Projekt import PQHeap

pq = []

for line in sys.stdin:

    PQHeap.insert(pq,int(line))

while len(pq) > 0:
    print(PQHeap.extractMin(pq))