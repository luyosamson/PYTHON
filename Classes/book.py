class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def get_book_info(self):
        print(self.title,self.author,self.pages)

b1=Book("Python V1","Luyo Sam",100)
b1.get_book_info()