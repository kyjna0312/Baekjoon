count = int(input())

result = []
for i in range(count) :
    num1, num2 = input().split()
    
    num1 = int(num1)
    num2 = int(num2)

    result.append(num1+num2)

for i in result :
    print(i)