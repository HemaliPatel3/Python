class Book():
    def __init__(self,a):
        self.a = a 
    def cal(self):
        return (self.a*10)
def main():
    for i in range(int(input())):
        a = int(input())
        book = Book(a)
        print(book.cal())
if __name__ =='__main__':
    main()    
