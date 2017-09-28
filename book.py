class Book:
    # parameters:
        title: string
        author: string
        publication_date: date
        call_number: string
        subject: string
        borrower: Person
        return_date: date
        hold_for: Person

    # methods:

        check_in(Book)
        hold(book, hold_for_person)
        renew(book, new_return_date)


	#prompts to enter all the new book information
    def create(title, author, subject, pub_date, call_number)
        if person is a librarian:
        	title = input("Enter title")
        	author = input("Enter one or more authors")
        	subject = input("Enter one or more subjects")
        	pub_date = input(date)
        	call_number = input("Enter call number")
        else:
            "Sorry, you can't add books."

    give_away(Book)
