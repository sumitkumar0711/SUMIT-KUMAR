var1 = input()
sum = 0
l1 = []
for i in var1:
    if(i.isdigit()==True):
        l1.append(i)
    else:
        print(i,end="")
var2 = [int(s) for s in l1]
for j in var2:
    sum += j
print(sum)