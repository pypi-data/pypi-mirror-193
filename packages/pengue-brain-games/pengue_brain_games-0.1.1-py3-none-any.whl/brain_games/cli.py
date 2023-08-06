#!/usr/bin/env python3
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_over(answer, right_answer, name):
    print(
        f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
    print(f"Let's try again, {name}!")


def lets_try_again(name):
    print(f"Let's try again, {name}!")
