waste = input()
var1 = input().split()
var = [int(s) for s in var1]
delval = min(var)
var.remove(delval)
print(min(var))
