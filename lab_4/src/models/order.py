from src.models.employee import Employee
from src.models.student import Student
from src.models.book import Book


class Order:

    def __init__(self, employee: Employee, student: Student,
                 books: list[Book]):
        self._employee = employee
        self._student = student
        self._books = books

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )
