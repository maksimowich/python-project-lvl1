from random import randint


def get_right_answer_progression():
    start = randint(1, 200)
    step = randint(3, 25)
    amount = randint(5, 10)
    index_of_hidden_number = randint(0, amount - 1)
    print("Question:", end='')
    for i in range(amount):
        if i == index_of_hidden_number:
            print(' ..', end='')
        else:
            print(f' {start + step * i}', end='')
    print()
    return str(start + step * index_of_hidden_number)
