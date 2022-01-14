numList = []

for i in range(3) :
    num = int(input())
    numList.append(num)

num = numList[0] * numList[1] * numList[2]
num = str(num)

for i in range(10) :
    print(num.count(str(i)))