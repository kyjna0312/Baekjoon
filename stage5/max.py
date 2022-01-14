numList = []
max = 0

for i in range(9) :
    num = int(input())
    numList.append(num)
    
    if max < num :
        max = num
            
print(max)
print(numList.index(max)+1)