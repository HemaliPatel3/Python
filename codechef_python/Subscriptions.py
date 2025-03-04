#Difficulty:  504
import math
for i in range(int(input())):
    a,b = map(int,input().split())
    a =math.ceil(a/6)
    print(a*b)
    
