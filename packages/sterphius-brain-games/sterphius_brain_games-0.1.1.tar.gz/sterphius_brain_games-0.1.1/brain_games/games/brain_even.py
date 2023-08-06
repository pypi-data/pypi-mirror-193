from random import randint

DESCRIPTION = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def generate_data():
    random_number = randint(1, 100)
    question = str(random_number)

    expected_result = None

    if random_number % 2 == 0:
        expected_result = 'yes'
    else:
        expected_result = 'no'

    return question, expected_result
