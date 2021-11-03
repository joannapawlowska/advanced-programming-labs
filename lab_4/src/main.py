from src.models.book import Book
from src.models.student import Student
from src.models.library import Library
from src.models.employee import Employee
from src.models.order import Order
from src.models.house import House
from src.models.flat import Flat

import datetime

# ex 1
s1 = Student('Kuba', 40)
s2 = Student('Anna', 80)

print(s1.is_passed())
print(s2.is_passed())

# ex 2
l1 = Library('Katowice', 'Miejska', '12-345', '8:00-17:00', '987654321')
l2 = Library('Katowice', 'Podmiejska', '12-345', '9:00-16:00', '123456321')

b1 = Book(l1, datetime.datetime(2020, 5, 17), 'Robert', 'Robert', 235)
b2 = Book(l2, datetime.datetime(2021, 6, 21), 'Anna', 'Anna', 511)
b3 = Book(l2, datetime.datetime(1997, 2, 11), 'Katarzyna', 'Robert', 200)
b4 = Book(l1, datetime.datetime(2006, 11, 23), 'Tomasz', 'Tomasz', 134)
b5 = Book(l1, datetime.datetime(2011, 7, 3), 'Magdalena', 'Magdalena', 476)

e1 = Employee('Robert', 'Robert', datetime.datetime(2020, 5, 17),
              datetime.datetime(1970, 1, 17), 'Katowice', 'Miejska',
              '12-345', '808707606')
e2 = Employee('Tomasz', 'Tomasz', datetime.datetime(2012, 8, 10),
              datetime.datetime(1983, 2, 22), 'Katowice', 'PodMiejska',
              '12-345', '333333333')
e3 = Employee('Robert', 'Robert', datetime.datetime(2021, 9, 1),
              datetime.datetime(1992, 12, 12), 'Katowice', 'Miejska',
              '12-345', '567432567')

s3 = Student('Kuba', 40)
s4 = Student('Julia', 60)
s5 = Student('Karolina', 50)

o1 = Order(e1, s3, [b1, b2])
o2 = Order(e2, s4, [b3, b4, b5])

print(o1)
print(o2)

h1 = House('150 m2', 10, 599000, 'Katowice 12-345, Miejska 43a', 6)
f1 = Flat('90 m2', 5, 271000, 'Katowice 12-345, Miejska 2b', 1)

print(h1)
print(f1)
