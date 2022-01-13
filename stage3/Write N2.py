num = int(input())

idxList = list(range(1,num+1))

for i in range(len(idxList)) :
    idxList[i] = idxList[i]*-1

numList = list(range(1,num+1))
for i in idxList :
    print(numList[i])