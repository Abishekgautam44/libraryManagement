

class Library:
    def __init__(self, listOfBooks):
        self.books= listOfBooks
    def displayAvail(self):
        print("Books present in this library are: ")
        for book in self.books:    
            print("*"+ book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"you have been issued {bookName}. please return within 25 days./n Thank you")
            self.books.remove(bookName)
            return True
        else:
            print("This book has already been issued. wait for untill it is available.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print('thanks for returning .')


class Student:
    def requestBook(self,):
        self.book = input("Enter the name of book you want to borrow: ")
        return self.book

    def returnBook(self,):
        self.book = input("Enter the name of book you want to return: ")
        return self.book


if __name__ == "__main__":
    
    centralLibrary = Library(['dsa','python','Ml','AI','oop'])
     #centralLibrary.displayAvail()
    while(True):
        welcomemsg = """\n------WELCOME TO CENTRAL LIBRARY-------
        please choose an option:
        1. see all the book list
        2. borrow a book
        3. return a book
        4. exit the library """

        print(welcomemsg)

        a = int(input("Enter a choice:"))

        if a==1:
            centralLibrary.displayAvail()
        elif a==2:
            centralLibrary.borrowBook(Student.requestBook())
        elif a ==3:
            centralLibrary.returnBook(Student.returnBook())
        elif a ==4:
            print("Thaks for choosing central library.")
            exit()
        else:
            print("Invalid option.")