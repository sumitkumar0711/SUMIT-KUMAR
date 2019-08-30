var = input().split()
inputs = [int(s) for s in var]
var2 = input().split()
values = [int(s) for s in var2]
B = []
for i in range(inputs[1],inputs[2]):
  B.append(values[i])
print(min(B))