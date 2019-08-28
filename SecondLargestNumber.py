waste = input()
var1 = input().split()
var = [int(s) for s in var1]
deletevalue = min(var)
var.remove(deletevalue)
if(len(var) == 1):
    print("1")
else:
    print(min(var))
