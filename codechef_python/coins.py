class Coins:
    def __init__(self,a,b):
        self.a = a
        self.b = b 
    def cal(self):
        c = self.a*self.b
        if c >= 100:
            return (c//100)
        else:
            return 0
def main():
    for i in range(int(input())):
        a,b = map(int,input().split())
        coin = Coins(a,b) 
        print(coin.cal())
if __name__ == '__main__':
    main()
