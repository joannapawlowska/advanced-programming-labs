from typing import TypeVar

TNum = TypeVar('TNum', int, float)


def greet(name: str, surname: str) -> str:
    return f'Hi, {name} {surname}!'


def multiply(a: int, b: int) -> int:
    return a * b


def is_even(number: int) -> bool:
    return number % 2 == 0


def is_less_than_sum(a: int, b: int, c: int) -> bool:
    return a + b >= c


def if_contains(numbers: list, number: int) -> bool:
    return number in numbers


def join_distinct_cube(list1: list[TNum], list2: list[TNum]) -> list[TNum]:
    return [n ** 3 for n in list(set(list1 + list2))]


# ex 1
greeting = greet('Name', 'Surname')
print(greeting)

# ex 2
print(multiply(4, 3))

# ex 3
is_even = is_even(2)
print('Even number' if is_even else 'Odd number')

# ex 4
print(is_less_than_sum(2, 4, 7))

# ex 5
print(if_contains([3], 4))
print(if_contains([1, 2], 1))

# ex 6
print(join_distinct_cube([1, 2, 3], [1, 2, 4]))
print(join_distinct_cube([1.2, 5.0, 2.0], [1.2, 5.0, 10.0]))
