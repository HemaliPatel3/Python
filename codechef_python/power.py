class Power():
    def __init__(self,a,b,c,d):
        self.a = a 
        self.b = b 
        self.c = c 
        self.d = d
    def cal(self):
        if (self.a*self.b) <= (self.c*self.d):
            return 'yes'
        else:
            return 'no'
def main():
    for i in range(int(input())):
        a,b,c,d = map(int,input().split())
        power = Power(a,b,c,d)
        print(power.cal())
if __name__ == '__main__':
    main()
