#!/usr/bin/env python
from brain_games.cli import greet_and_welcome_user, play_game
from brain_games.brain_gcd import get_right_answer_gcd


def main():
    name = greet_and_welcome_user()
    print('Find the greatest common divisor of given numbers.')
    play_game(name, get_right_answer_gcd)


if __name__ == '__main__':
    main()
