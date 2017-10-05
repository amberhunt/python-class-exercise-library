#def check_out(Book, borrower, return_date):
    # return_date = today + 180 days
    # Default is 180 days, but librarian can choose a different date
    # Is the book already checked out?
        # yes
        #   print message "Book cannot be checked out, it is already check out"
        # no
        #   # Is the person a borrower?
        #       yes
        #           Book.borrower = borrower
        #           Book.return_date = return_date
        #       no
        #           print message "Cannot checkout to non-borrower"
from book import Book
from person import Person
from datetime import date
from datetime import timedelta

def check_out(self, me, borrower, return_date):
    if me is Librarian :
        if borrower is Borrower :
            self.borrower = input("Enter borrower ")
            custom = input("Enter Y for default, N for custom ")
            if custom = "Y" :
                self.return_date = str(date.today() + timedelta (days=180))
            elif custom = "N" :
                self.return_date = date(input("Enter date: yyyy/mm/dd "))
        elif borrower is not Borrower :
            print("Unknown borrower, please create a Person before check out")
    elif me is not Librarian :
        print("Non-librarians may not check out")
