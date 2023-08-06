from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_data():
    a = randint(1, 100)

    question = f'{a}'

    expected_result = 'yes'

    if (a == 1) or (a % 2 == 0):
        expected_result = 'no'
        return question, expected_result

    for i in range(2, a // 2):
        if (a % i) == 0:
            expected_result = 'no'
            break

    return question, expected_result
