k = int(input())
inp = input().split()
var = [int(s) for s in inp]
var.sort()
print(var[k-1])