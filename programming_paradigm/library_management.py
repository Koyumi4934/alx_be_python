# library_management.py
class Book:
    """A book with title, author and availability state."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out; return True if successful, False if already out."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """Return the book; return True if successful, False if it was not checked out."""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self):
        """True if book is available (not checked out)."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of Book instances."""
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        """Add a Book instance to the library."""
        if not isinstance(book, Book):
            raise TypeError("add_book expects a Book instance")
        self._books.append(book)

    def _find_book_by_title(self, title: str):
        """Helper: returns the first book with matching title, or None."""
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title: str):
        """Attempt to check out a book by title. Print action result and return boolean."""
        book = self._find_book_by_title(title)
        if book is None:
            print(f"Book titled '{title}' not found in library.")
            return False
        if book.check_out():
            print(f"Checked out: {book}")
            return True
        else:
            print(f"Cannot check out '{title}': already checked out.")
            return False

    def return_book(self, title: str):
        """Attempt to return a book by title. Print action result and return boolean."""
        book = self._find_book_by_title(title)
        if book is None:
            print(f"Book titled '{title}' not found in library.")
            return False
        if book.return_book():
            print(f"Returned: {book}")
            return True
        else:
            print(f"Cannot return '{title}': it was not checked out.")
            return False

    def list_available_books(self):
        """Print all available (not checked out) books."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books available.")
            return
        for book in available:
            print(str(book))
