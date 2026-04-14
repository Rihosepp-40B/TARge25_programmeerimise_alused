"""Book store."""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author and price.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

    def __eq__(self, value):
        """Check if is same object."""
        if isinstance(value, Book):
            return self.author == value.author and self.title == value.title
        return False