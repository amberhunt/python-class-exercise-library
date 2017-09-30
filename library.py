"""Uses Book and Person classes to implement a simple library."""
from book import Book


def main():
    """
    Library entry point summary line

    First line of a multi-line description.
    """
    print("Hello, Librarian!")
    hound = Book("Hound of the Baskervilles")
    print(hound.title)

    print("Imported function test:")
    hound.test()


main()
