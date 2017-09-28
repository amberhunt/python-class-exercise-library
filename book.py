"""Book class definition"""


class Book:
    """
    Each book in the library is an instance of Book class

    Methods:
        __init__: creates a new book in the library
        check_out: lends the book to a borrower
        check_in: records that the book was returned
        hold: places other potential borrowers in queue to borrow the book
            when it has been returned
        renew: allows the borrower to keep the book longer, if no one is in the
            hold queue
        __del__: gives away the book so that it is no longer in the library
    """
    # pylint: disable=too-many-instance-attributes
    # All are reasonable in this case.

    def __init__(self, title, author, subject, pub_date, call_number):
        """Creates a new book for the libary"""

        # if you are a librarian, you can do this
        self.title = title
        self.author = author
        self.publication_date = pub_date
        self.subject = subject
        self.call_number = call_number
        self.borrower = None
        self.return_date = None
        self.hold_for = None
        # if not a librarian, explain that only a librarian can create books
