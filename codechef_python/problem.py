class Problem():
    def __init__(self,a,b):
        self.a =a 
        self.b =b 
    def cal(self):
        if (self.b*100)/self.a >= 50:
            return('yes')
        else:
            return 'no'
        
        
def main():
    for i in range(int(input())):
        a,b = map(int,input().split())
        problem = Problem(a,b)
        print(problem.cal())
if __name__== '__main__':
    main()
