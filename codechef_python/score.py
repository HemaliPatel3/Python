class Score:
    def __init__(self,a,b,c,d):
        self.a = a 
        self.b = b
        self.c = c 
        self.d = d 
    def cal(self):
        return 'POSSIBLE' if (self.a <= self.c and self.b <= self.d) else 'IMPOSSIBLE'
def main():
    for i in range(int(input())):
        a,b = map(int,input().split())
        c,d = map(int,input().split())
        score = Score(a,b,c,d)
        print(score.cal())
if __name__ == '__main__':
    main()
