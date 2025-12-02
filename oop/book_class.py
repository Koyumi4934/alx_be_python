class Book:
    def __init__(self, title: str, author: str, year: int):
        """Initialize a Book instance with title, author and year."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        """Informal string representation (used by print())."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """Official representation — should recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor prints notice when the object is deleted."""
        print(f"Deleting {self.title}")
