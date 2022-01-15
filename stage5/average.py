subjectNum = int(input())
scoreList = list(map(int, input().split()))

scoreList.sort()
maxNum = scoreList[-1]

scoreList = [(i/maxNum)*100 for i in scoreList]
sumNum = 0

for i in scoreList :
    sumNum += i

print(sumNum/subjectNum)