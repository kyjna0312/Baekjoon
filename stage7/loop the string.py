caseCount = int(input())
loopDict = {}

for i in range(caseCount) :
    loopCount, sentence = input().split()
    loopDict[sentence] = int(loopCount)

for i in loopDict :
    loopCount = loopDict[i]
    
    for j in i :
        print(j * loopCount, end="")

    print()