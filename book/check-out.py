check_out(Book, borrower, return_date)
    # If the book is not alreayd borrowed...
    # Is this a valid borrower
    if (borrower is a Person who is_Borrower):
        Book.borrower = borrower
        # Make sure the return_date is in the future, but not too far into the future.
        # Default is not more than 180 days.
        if (return date is > 180 days):
            Print a message ... cannot borrow but for 180 days.
            Use the 180th day as the return date
        Book.return_date = return_date
    else (explain this person cannot borrow books)
