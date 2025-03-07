for i in range(int(input())):
    a,b,c = map(int,input().split())
    d = a*b
    if (c*100)/d > 50:
        print('yes')
    else :
        print('no')

# using OOPS method 
class Exams:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def cal(self):
        d = self.a * self.b
        if (self.c * 100) / d > 50:
            return "yes"
        else:
            return "no"
def main():
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        exam = Exams(a, b, c)
        print(exam.cal())  
if __name__ == "__main__":
    main()

