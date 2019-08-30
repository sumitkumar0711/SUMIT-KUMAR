import math
var = input().split()
value = [int(s) for s in var]
soln = math.factorial(value[0])//(math.factorial(value[1]) * (math.factorial(value[0]-value[1])))
print(soln*2)