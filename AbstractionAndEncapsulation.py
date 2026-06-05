#Abstraction And Encapsulation in Python

class Library:
      def __init__(self,books):
          self.books=books
          
      def list_books(self):
          print("Available Books")py
          for book in self.books:
              print(book)
      def borrow_book(self,borrow_book):
          if borrow_book in self.books:
              print("Get your book now")
              self.books.remove(borrow_book)
          else:
              print("book not available")
              
      def recevie_book(self,recevie_book):
          print("you have returned the book")
          self.book.append(recevie_book)
          
books=['c','c++','java']
o=Library(books)

msg = """
    1.Display Books
    2.Borrow Books
    3.Return Books
"""
while True:
    print(msg)
    ch=int(input("Enter the choice : "))
    if ch == 1:
        o.list_books()
    elif ch == 2:
        book =int(input("Enter book name to Borrow: "))
        o.borrow_book(book)
    elif ch == 3:
        book =int(input("Enter book name to Return: "))
        o.recevie_book(book)  
    else:
        print("Thank you come again")
        quit()        