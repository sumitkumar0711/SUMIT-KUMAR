garbage = int(input())
var = input().split()
counter = 0
values = [int(s) for s in var]
for i in range(0,len(values)-2):
    if((values[i]<values[i+1]) and (values[i+1]<values[i+2])):
        counter += 1
print(counter)