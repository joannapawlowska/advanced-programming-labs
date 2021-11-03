class Student:

    def __init__(self, name: str, marks: int):
        self._name = name
        self._marks = marks

    def is_passed(self) -> bool:
        return self._marks > 50

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )
