from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'


def generate_data():
    a, b = randint(1, 100), randint(1, 100)

    operations = ('+', '-', '*')
    operation = choice(operations)

    question = f'{a} {operation} {b}'

    expected_result = expected_result_from(a, b, operation)

    return question, expected_result


def expected_result_from(a, b: int, op: str):
    match op:
        case '+':
            return str(a + b)
        case '-':
            return str(a - b)
        case '*':
            return str(a * b)
