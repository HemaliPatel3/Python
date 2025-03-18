class Profit():
    def __init__(self,a):
        self.a = a 
    def cal(self):
        c = 50*self.a 
        d = (c*20)//100
        e = (c*30)//100
        return c - ((2*d) + e)
def main():
    for i in range(int(input())):
        a = int(input())
        profit = Profit(a)
        print(profit.cal())
if __name__ =='__main__':
    main()
