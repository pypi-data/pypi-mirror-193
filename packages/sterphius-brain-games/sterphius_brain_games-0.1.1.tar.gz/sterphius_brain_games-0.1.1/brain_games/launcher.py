import prompt

from brain_games import cli


def compare_results(actual, expected: str):
    return True if actual.lower() == expected else False


def run(game=None):

    user_name = cli.welcome_user()

    '''This check is for the game: brain_games
    where the game step is welcoming user only'''
    if game is not None:
        print(game.DESCRIPTION)
        play(game, user_name)
    else:
        return


def play(game, user_name: str):

    correct_answer_count = 0
    success_answers_count = 3

    while correct_answer_count < success_answers_count:
        game_data = game.generate_data()

        question_str = game_data[0]
        print(f'Question: {question_str}')

        answer = prompt.string('Your answer: ')
        result = compare_results(answer, game_data[1])

        wrong_msg = f"\'{answer}\' is wrong answer ;(. " \
            f"Correct answer was \'{game_data[1]}\'.\n "\
            f"Let\'s try again, {user_name}!"

        if result:
            print('Correct')
            correct_answer_count += 1
        else:
            print(wrong_msg)
            return

    print(f'Congratulations, {user_name}!')
