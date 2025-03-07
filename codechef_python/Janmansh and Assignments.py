for i in range(int(input())):
    a = int(input())
    if 10-a>=3:
        print("YES")
    else:
        print("NO")



# using OOPS method 
class Ass:
    def __init__(self,a):
        self.a = a
    def cal(self):
        if 10 -self.a >=3:
            return 'YES'
        else:
            return 'NO'
def main():
    for i in range(int(input())):
        a = int(input())
        ass = Ass(a)
        print(ass.cal())
if __name__ == "__main__":
    main()
