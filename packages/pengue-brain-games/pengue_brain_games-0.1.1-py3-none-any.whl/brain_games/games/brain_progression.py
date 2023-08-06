from random import randint


rules = 'What number is missing in the progression?'
length_progression = randint(5, 10)
start = randint(1, 10)
step = randint(1, 10)
secret_number = randint(0, length_progression - 1)


def run():
    question = ''
    i = 0
    while i < length_progression:
        if question:
            question += ' '
        if i != secret_number:
            question = question + str((start + (step * i)))
            i += 1
        else:
            question += '..'
            correct_answer = str(start + (step * i))
            i += 1
    return question, correct_answer
