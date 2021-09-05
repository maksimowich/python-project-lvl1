import prompt


def welcome_user():
    name = prompt.string('May I ask your name? ')
    print(f'Hello, {name}!')
    return name


def greet_and_welcome_user():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    return name


def play_rounds(name, get_right_answer):
    for i in range(3):
        right_answer = get_right_answer()
        user_answer = prompt.string("Your answer: ")
        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(.', end='')
            print(f'Correct answer was {right_answer}')
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')


def play_game(task, greet_and_welcome_user, get_right_answer):
    name = greet_and_welcome_user()
    print(task)
    play_rounds(name, get_right_answer)
