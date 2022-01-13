import sys

count = sys.stdin.readline().rstrip()
result = []

for i in range(int(count)) :
    num1, num2 = sys.stdin.readline().rstrip().split()
    num1 = int(num1)
    num2 = int(num2)

    result.append(num1+num2)

for i in result :
    print(i)