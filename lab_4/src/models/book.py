from src.models.library import Library
import datetime


class Book:

    def __init__(self, library: Library, publication_date: datetime,
                 author_name: str, author_surname: str, number_of_pages: int):
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def __repr__(self):
        return self.__str__()
