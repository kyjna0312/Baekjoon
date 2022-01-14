numList = []
count = 0

for i in range(10) :
    num = int(input())
    numList.append(num%42)

for i in range(42) :
    if numList.count(i) > 0 :
        count += 1

print(count)
