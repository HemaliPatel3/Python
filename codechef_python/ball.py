class Ball():
    def __init__(self,a,b,c,d):
        self.a = a 
        self.b = b 
        self.c= c 
        self.d = d 
        
    def cal(self):
        if self.a == 0 and self.b== 0 and self.c== 0 and self.d == 0:
            return('IN')
        else:
            return('out')
        
        
def main():
    for i in range(int(input())):
        a,b,c,d = map(int,input().split())
        ball = Ball(a,b,c,d)
        print(ball.cal())
if __name__ =='__main__':
    main()
