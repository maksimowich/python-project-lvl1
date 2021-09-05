#!/usr/bin/env python
from brain_games.cli import greet_and_welcome_user, play_game
from brain_games.brain_progression import get_right_answer_progression


def main():
    task = 'What number is missing in the progression?'
    play_game(task, greet_and_welcome_user, get_right_answer_progression)


if __name__ == '__main__':
    main()
