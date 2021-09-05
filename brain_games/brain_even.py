from random import randint


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def get_right_answer_even():
    number = randint(1, 50)
    right_answer = is_even(number)
    print(f'Question: {number}')
    return right_answer
