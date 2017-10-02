# python-class-exercise-library
Exercise about objects & classes, using a library as an example

# User stories

## Add a book to the library

Bob, a librarian, wants to create a book & add it to the library.


## Renewal

Alice, a borrower, wants to renew a book so that she can continue to read it. She asks Bob, a librarian, to renew the book in the system.
* A book may be renewed indefinitely if no one is in the hold queue.
* The default renewal period is 60 days, but Bob can choose a different due date.
* A book may be renewed within 30 days before its due (if no one is in the hold queue).
* The renewal period starts from the day of the renewal request.

## Check Out

Alice, a borrower, wants to check out a book from the library. She asks Bob, a librarian, to check out the book to her her.
* Books may only be checked out by librarians.
* A book may only be checked out to one person at a time.
* A book may be checked out for 60 days.
