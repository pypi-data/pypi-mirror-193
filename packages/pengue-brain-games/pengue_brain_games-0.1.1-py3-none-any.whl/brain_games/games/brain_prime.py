import random
from brain_games.games.brain_even import compare_answer


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(a):
    if a % 2 == 0:
        return a == 2
    elif a == 1:
        return False
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a


def run():
    choice = [1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 17,
              18, 19, 21, 22, 23, 29, 31, 37, 38, 39, 40, 41,
              43, 47, 53, 59, 61, 62, 63, 64, 65, 66, 67, 68,
              69, 71, 72, 73, 74, 76, 78, 79, 83, 84, 85, 86,
              89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    question = random.choice(choice)
    correct_answer = compare_answer(is_prime(question))
    return question, correct_answer
