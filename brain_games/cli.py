import prompt


def welcome_user():
    name = prompt.string('May I ask your name? ')
    print(f'Hello, {name}!')
