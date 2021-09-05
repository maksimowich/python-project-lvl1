#!/usr/bin/env python
from brain_games.cli import greet_and_welcome_user, play_game
from brain_games.brain_calc import get_right_answer_calc


def main():
    task = ('What is the result of the expression?')
    play_game(task, greet_and_welcome_user, get_right_answer_calc)


if __name__ == '__main__':
    main()
