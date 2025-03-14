class sale:
    def __init__(self,a):
        self.a = a 
    def cal(self):
        if self.a <= 100:
            return(self.a)
        elif 100 < self.a <= 1000:
            return(self.a - 25)
        elif 1000 < self.a <= 5000:
            return(self.a - 100)
        else:
            return(self.a - 500)
def main():
    for i in range(int(input())):
        a = int(input())
        season = sale(a)
        print(season.cal())
if __name__ == '__main__':
    main()
            
