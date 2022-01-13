count = int(input())

resultList = []
num1List = []
num2List = []
for i in range(count) :
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)

    num1List.append(num1)
    num2List.append(num2)

    resultList.append(num1+num2)

for i in range(count) :
    print("Case #", i+1, ": ", num1List[i], " + ", num2List[i], " = ", resultList[i], sep="")