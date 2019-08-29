var = input().split()
n = len(var)
k = int(input())
for j in range(k):
    temp = var[0]
    for i in range(n-1):
        var[i] = var[i+1]
    var[n-1] = temp
print(var)