import math 
class Candies:
    def __init__(self,a,b):
        self.a = a 
        self.b = b 
    def cal(self):
        if (self.a - self.b)>0:
            return math.ceil((self.a - self.b)/ 4)
        else:
            return 0
def main():
    for i in range(int(input())):
        a,b = map(int,input().split())
        candies = Candies(a,b)
        print(candies.cal())
        
if __name__ == "__main__":
    main()
