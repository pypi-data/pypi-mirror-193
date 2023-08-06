import random


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_parity(number):
    if number % 2 == 0:
        return True
    return False


def compare_answer(parity):
    if parity is True:
        return 'yes'
    elif parity is False:
        return 'no'


def run():
    qustion = random.randint(1, 100)
    correct_answer = compare_answer(check_parity(qustion))
    return qustion, correct_answer
