#Difficulty:  504
import math
for i in range(int(input())):
    a,b = map(int,input().split())
    a =math.ceil(a/6)
    print(a*b)
    
# using OOPS concepts
import math
class Sub():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def cal(self):
        a = math.ceil(a/6)
        return a*b
def main():
    for i in range(int(input())):
        a,b = map(int,input().split())
        sub = Sub(a,b)
        print(sub.cal())
if __name__ == '__main__':
    main()
