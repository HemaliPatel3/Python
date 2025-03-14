class water:
    def __init__(self,a,b,c):
        self.a = a 
        self.b = b 
        self.c = c
    def cal(self):
        x = [self.a,self.b,self.c].count(0)
        if x >= 2:
            return('Water filling time')
        else:
            return('Not now')
def main():
    for i in range(int(input())):
        a,b,c = map(int,input().split())
        wat = water(a,b,c)
        print(wat.cal())
if __name__ == '__main__':
    main()
