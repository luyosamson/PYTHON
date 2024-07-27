class Book:
    def __init__(s,title,author,pages):
        s.title=title
        s.author=author
        s.pages=pages
    def get_book_info(s):
        print(s.title,s.author,s.pages)

b1=Book("Python V1","Luyo Sam",100)
b1.get_book_info()

