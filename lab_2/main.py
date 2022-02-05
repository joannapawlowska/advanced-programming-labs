from random import randrange


def print_names(names):
    [print(name) for name in names]


def get_multiplied_with_for(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers


def get_multiplied_with_list_comprehension(numbers):
    return [2*n for n in numbers]


def print_even():
    for i in [i + randrange(i+1) for i in range(10)]:
        if i % 2 == 0:
            print(i)


def print_every_second():
    tab = [i for i in range(10)]
    for i in range(len(tab)):
        if i % 2 == 1:
            print(i)


print('ex 2a')
print_names(['Jo', 'Tom', 'Ann', 'Name', 'Name2'])

print('ex 2b')
print(get_multiplied_with_for([2, 1, 3, 4, 5]))
print(get_multiplied_with_list_comprehension([2, 1, 3, 4, 5]))

print('ex 2c')
print_even()

print('ex 2d')
print_every_second()
