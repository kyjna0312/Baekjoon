caseNum = int(input())
resultList = []

for i in range(caseNum) :
    scoreList = list(map(int, input().split()))
    person = scoreList[0]
    average = 0
    count = 0

    for i in scoreList[1:] :
        average += i
    
    average = average/person

    for i in scoreList[1:] :
        if i > average :
            count += 1
    
    result = (count/person)*100
    resultList.append(result)

for i in resultList :
    print(i,"%", sep="")

