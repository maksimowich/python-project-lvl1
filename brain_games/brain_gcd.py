from random import randint


def gcd(a, b):
    if a > b:
        return gcd(a - b, b)
    elif a < b:
        return gcd(b - a, a)
    else:
        return a


def get_right_answer_gcd():
    number1 = randint(5, 200)
    number2 = randint(5, 200)
    print(f'Question: {number1} {number2}')
    return str(gcd(number1, number2))
