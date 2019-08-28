waste = input()
var1 = input().split()
var = [int(s) for s in var1]
deletevalue = min(var)
var.remove(deletevalue)
print(min(var))