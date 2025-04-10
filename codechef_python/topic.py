class Topic:
    def __init__(self, a, b, c, d):
        self.a = a 
        self.b = b 
        self.c = c 
        self.d = d

    def cal(self):
        lst = [self.a, self.b, self.c]
        return 'yes' if self.d in lst else 'no'

def main():
    a, b, c, d = map(int, input().split())
    topic = Topic(a, b, c, d)
    print(topic.cal())

if __name__ == '__main__':
    main()
