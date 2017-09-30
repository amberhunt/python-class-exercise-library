"""Assemble Book class into a package."""


class Book:
    """Each book in the library is an instance of Book class.
    Methods:
        __init__: creates a new book in the library
        check_out: lends the book to a borrower
        check_in: records that the book was returned
        hold: places other potential borrowers in queue to borrow the book
            when it has been returned
        renew: allows the borrower to keep the book longer, if no one is in
            the hold queue
        __del__: gives away the book so that it is no longer in the library
    """
    # pylint: disable=too-many-instance-attributes
    # All are reasonable in this case.

    def __init__(self, title):
        # if you are a librarian, you can do this
        self.__title = title
        # self.author = author
        # self.publication_date = pub_date
        # self.subject = subject
        # self.call_number = call_number
        # self.borrower = None
        # self.return_date = None
        # self.hold_for = None
        # if not a librarian, explain that only a librarian can create books

    @property
    def title(self):
        """Returns book title to any caller."""
        return self.__title

    @title.setter
    def title(self, new_title):
        """Change book title. Only for librarians."""
        # if you are a librarian, you can change the title of an existing book
        self.__title = new_title
        print("Assumed you are a librarian. Title changed to: ", self.title)
        # else print an error message

    # import book.check-in
    # import book.check-out
    # import book.give-away
    # import book.hold
    # import book.renew
    from book.test import test
