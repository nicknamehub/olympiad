from math import sqrt
a = int(input())
b = int(input())
c = int(input())
p = (float(a+b+c))/2
S = sqrt(p*(p-a)*(p-b)*(p-c))
print(S)
