num1, num2 = map(int, input().split())
result = []

while num1 != 0 and num2 != 0 :
    result.append(num1+num2)
    num1, num2 = map(int, input().split())

length = len(result)
i = 0
while i < length :
    print(result[i])
    i+=1