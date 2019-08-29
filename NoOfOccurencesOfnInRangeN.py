value1 = int(input())
rangeValue = int(input())
counter = 0
for i in range(rangeValue):
    calcvalue = i
    while(calcvalue != 0):
        r = calcvalue % 10
        if(r == value1):
            counter += 1
        calcvalue /= 10
print(counter)