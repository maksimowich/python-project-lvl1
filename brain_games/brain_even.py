from random import randint
from prompt import string


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def brain_even():
    for i in range(3):
        question = randint(1, 50)
        right_answer = is_even(question)
        print(f'Question: {question}')
        user_answer = string("Your answer: ")
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {right_answer}.')
            print('Let\'s try again')
            return
    print("congratulations")
