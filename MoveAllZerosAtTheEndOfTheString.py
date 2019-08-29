var1 = input()
a = []
b = []
for i in range(len(var1)):
    if(var1[i] == '0'):
        a.append(var1[i])
    else:
        b.append(var1[i])
print(b+a)