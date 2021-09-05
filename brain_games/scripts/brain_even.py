#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.brain_even import brain_even


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(r'Answer "yes" if the number is even, otherwise answer "no".')
    brain_even()
