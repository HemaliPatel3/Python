for i in range(int(input())):
    a,b,c = map(int,input().split())
    if (a+b)/2 > c:
        print('yes')
    else :
        print('no')



# using OOPs concepts

class GRE:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def cal(self):
        if (self.a+self.b)/2 >self.c:
            return 'yes'
        else :
            return 'no'
def main():
    for i in range(int(input)):
    a,b,c = map(int,input().self())
    gre = GRE(a,b,c)
    print(gre.cal())
if __name__ == '__main__':
    main()
