from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_data():
    progression_length = 5

    k = randint(1, progression_length)
    diff = randint(1, 10)

    expected_result = None
    question = ''
    prev_value = randint(1, 100)

    if k == 1:
        question += '.. '
        expected_result = str(prev_value)
    else:
        question = str(prev_value) + ' '

    for x in range(2, progression_length + 1):

        current_value = prev_value + diff

        if x == k:
            question += '.. '
            expected_result = str(current_value)
        else:
            question += str(current_value) + ' '

        prev_value = current_value

    return question, expected_result
