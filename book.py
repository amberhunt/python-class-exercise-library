class Book:
    def __init__(self, title, author, subject, pub_date, call_number):
        # if you are a librarian, you can do this
        self.title = title
        self.author = author
        self.publication_date = pub_date
        self.subject = subject
        self.call_number = call_number
        self.borrower = None
        self.return_date = None
        self.hold_for = None

    # parameters:
        # title: string
        # author: string
        # publication_date: date
        # call_number: string
        # subject: string
        # borrower: Person
        # return_date: date
        # hold_for: Person

    # methods:
        # check_in(Book)
        # hold(book, hold_for_person)
        # renew(book, new_return_date)
        # give_away(Book)

        # if person is a librarian:
        # title = input("Enter title")
        # author = input("Enter one or more authors")
        # subject = input("Enter one or more subjects")
        # pub_date = input(date)
        # call_number = input("Enter call number")
        # else:
        #     "Sorry, you can't add books."
