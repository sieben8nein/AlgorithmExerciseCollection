
import random
import math
searchedNumber = 13
nrList = random.sample(range(0, 100), 16)
nrList.append(searchedNumber)
nrList.sort()
def binSearch(value, list, begin, end):
    midpoint = begin + math.floor((end - begin)/2)
    print("midpoint:", midpoint)
    print("value on midpoint:", list[midpoint])
    if begin <= end:
        if value == list[midpoint]:
            return midpoint
        elif value < list[midpoint]:
            return binSearch(value, list, begin, midpoint-1)
        elif value > list[midpoint]:
            return binSearch(value, list, midpoint+1, end)
    else:
        return -1
print(binSearch(searchedNumber, nrList, 0, len(nrList)))

