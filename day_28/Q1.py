# library management system 
class library:
    
    def __init__(self,book,student):
        self.books = book
        self.student = student

    def display(self):
        print(f"book name : {self.books} ")
        print(f"students name {self.student}")
        
        

    def add_book(self):
        book_name= input("enter the book")
        self.books.append(book_name)
        

    def status(self):
        book_name = input("enter the book name ")

        if book_name in self.books:
            print("Book is availble")
        else:
            print("book is not availble")

    def main(self):
        while True:
            print("\n===== library MANAGEMENT SYSTEM =====")
            print("1. Add book")
            print("2. Display book")
            print("3. Update status")
            print("4. Exit")

            choice = input("Enter Choice: ")

            if choice == '1':
                self.add_book()

            elif choice == '2':
                self.display()
            elif choice == '3':
                self.status()
                
            elif choice == '4':
                print("Thank You!")
                break

            else:
                print("Invalid Choice!")



obj = library(["python","c++"],"Aman")
obj.main()
# obj.status()
        
        
        