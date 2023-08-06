from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_data():
    a, b = randint(1, 100), randint(1, 100)

    expected_result = str(gcd(a, b))
    question = f'{a} {b}'

    return question, expected_result
