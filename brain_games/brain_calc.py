from random import randint, choice


def get_random_sign():
    return choice(['+', '-', '*'])


def get_right_answer(number1, number2, sign):
    if sign == "+":
        return number1 + number2
    elif sign == "-":
        return number1 - number2
    elif sign == "*":
        return number1 * number2


def get_right_answer_calc():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    sign = get_random_sign()
    print(f'Question: {number1} {sign} {number2}')
    return str(get_right_answer(number1, number2, sign))
