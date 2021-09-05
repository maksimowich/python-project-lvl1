#!/usr/bin/env python
from brain_games.cli import greet_and_welcome_user, play_game
from brain_games.brain_prime import get_right_answer_prime


def main():
    task = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'
    play_game(task, greet_and_welcome_user, get_right_answer_prime)


if __name__ == '__main__':
    main()
