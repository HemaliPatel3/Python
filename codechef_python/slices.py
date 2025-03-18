class Slices():
    def __init__(self,a,b):
        self.a =a 
        self.b = b 
    def cal(self):
        c= (self.a*self.b + 3)//4
        return c
def main():
    for i in range(int(input())):
        a,b = map(int,input().split())
        slice = Slices(a,b)
        print(slice.cal())
if __name__ == '__main__':
    main()
