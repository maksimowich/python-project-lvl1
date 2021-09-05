from math import sqrt
from random import randint


def is_prime(number):
    if number == 1:
        return 'yes'
    elif number < 2:
        return 'no'
    i = 2
    while i <= sqrt(number):
        if number % i == 0:
            return 'no'
        i += 1
    return 'yes'


def get_right_answer_prime():
    number = randint(1, 500)
    print(f'Question: {number}')
    return is_prime(number)
