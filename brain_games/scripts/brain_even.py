#!/usr/bin/env python
from brain_games.cli import greet_and_welcome_user, play_game
from brain_games.brain_even import get_right_answer_even


def main():
    task = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'
    play_game(task, greet_and_welcome_user, get_right_answer_even)


if __name__ == '__main__':
    main()
