import random
import time
import math


sampSize = 16
cycleProb = [0] * sampSize
pre = time.time_ns()
loops = 100000
#print("counting cycles for an array of size", sampSize, and )
for y in range(loops):
    nrList = random.sample(range(0, sampSize), sampSize)
    usedList = []
    cycles = 0
    #print(nrList)
    for x in range(len(nrList)):
        #print("usedlist: ", usedList)
        if(x not in usedList):
            usedList.append(x)
            nextIndex = nrList[x]
            while(nextIndex != x):
                usedList.append(nextIndex)
                #print("from: ", nextIndex, "to: ", nrList[nextIndex])
                nextIndex = nrList[nextIndex]
                #print("next index: ", nextIndex)
            cycles += 1
    #print(cycles)
    cycleProb[cycles] = cycleProb[cycles] + 1

for x in range(len(cycleProb)):
    cycleProb[x] = (cycleProb[x]*100)/loops
print("cycle probability: ", cycleProb)
print(loops, "loops require", (time.time_ns()-pre)/math.pow(10, 9), "seconds")