class Office:
    def __init__(self,a,b):
        self.a = a 
        self.b = b 
    def cal(self):
        return (self.a*4) + self.b 
def main():        
    for i in range(int(input())):
        a,b = map(int,input().split())
        Off = Office(a,b)
        print(Off.cal())
if __name__ == '__main__':
    main()
