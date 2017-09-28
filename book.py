"""Book class definition"""

class Book:
    """
    Book class represents one book in the library

    Attributes:
        title: string
        author: string
        publication_date: date
        call_number: string
        subject: string
        borrower: Person
        return_date: date
        hold_for: Person
    Methods:
        __init__: creates the book
        check_in(Book)
        hold(book, hold_for_person)
        renew(book, new_return_date)
        __del__(self): gives away the book & deletes the object
    """
    def __init__(self, title, author, subject, pub_date, call_number):
        """Book constructor"""
        # if you are a librarian, you can do this
        self.title = title
        self.author = author
        self.publication_date = pub_date
        self.subject = subject
        self.call_number = call_number
        self.borrower = None
        self.return_date = None
        self.hold_for = None
