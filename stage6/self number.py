def generateNum (n) :
    num = n
    strNum = str(num)

    for i in strNum :
        num += int(i)

    return num

generateList = set([generateNum(i) for i in range(10001)])
numList = set([i for i in range(10001)])

selfNum = list(numList - generateList)
selfNum.sort()

for i in selfNum :
    if i <= 10000 :
        print(i)