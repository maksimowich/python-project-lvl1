#!/usr/bin/env python
from brain_games.cli import greet_and_welcome_user, play_game
from brain_games.brain_gcd import get_right_answer_gcd


def main():
    task = 'Find the greatest common divisor of given numbers.'
    play_game(task, greet_and_welcome_user, get_right_answer_gcd)


if __name__ == '__main__':
    main()
