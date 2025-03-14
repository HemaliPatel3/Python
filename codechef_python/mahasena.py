class Mahasena:
    def __init__(self,a):
        self.a = list(a) 
    def cal(self):
        b = 0
        c = 0
        for i in self.a:
            if i % 2 == 0:
                b+=1
            else:
                c+=1
        if b > c:
            return 'READY FOR BATTLE'
        else:
            return 'NOT READY'
            
def main():
    n = int(input())
    a = map(int,input().split())
    mah = Mahasena(a)
    print(mah.cal())
if __name__ == '__main__':
    main()
                
