class Faster:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def cal(self):
        return 'bike' if self.x < self.y else 'car' if self.x > self.y else 'same'
def main():
    for i in range(int(input())):
        x,y = map(int,input().split())
        fast = Faster(x,y)
        print(fast.cal())
if __name__ == '__main__':
    main()
