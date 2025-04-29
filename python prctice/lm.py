# library managmentsystem 

class library:                                  # we take 2 variaables nobooks and books 
    def __init__(self):                          #logic create a empty list and append the variable in it    
        self.nobooks = 0                        #which create a list of books and for no of books we simply used lenght of the list  
        self.books = []

    def addBook(self,book):
        self.books.append(book)
        self.nobooks = len(self.books)

    def show(self):
        print(f"no of books is{self.nobooks} andthe books are")
        for i in self.books:
            print(i)
    def check(self):
        if self.nobooks==len(self.books):
            print("number  is equal to length")
        else:
            print("false")


l1 = library()
l1.addBook('harrypotter')
l1.addBook('fundamental of Blockchain')
l1.addBook('Mathematics')
l1.addBook('fundamental of web technology')
l1.show()
l1.check()