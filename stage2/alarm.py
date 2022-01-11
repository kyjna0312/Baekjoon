hour, min = input().split()

hour = int(hour)
min = int(min)


if min >= 45 :
    print(hour, min-45)

elif min < 45 :
    if hour == 0 :
        hour = 24
    
    print(hour-1, min+15)