from operator import itemgetter
n = int(input())
A = []
for i in range(n):
    var1 = input().split()
    A.append([var1[0],var1[1]])
print(sorted(A,key=itemgetter(1)))