num = int(input())
submissionList = []

for i in range(num) :
    submission = input()
    submissionList.append(submission)

for i in submissionList :
    score = 0
    result = 0

    for j in i :
        if j == 'O' :
            score += 1
        else :
            score = 0
        
        result += score
    
    print(result)