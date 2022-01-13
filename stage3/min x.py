num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)

numList = list(map(int, input().split()))

for i in numList :
    if num2 > i :
        print(i, end=" ")