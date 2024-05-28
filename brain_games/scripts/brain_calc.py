import random
from brain_games.cli import welcome_user


def calculate(operator, number_1, number_2):
    if operator == '+':
        return number_1 + number_2
    elif operator == '-':
        return number_1 - number_2
    elif operator == '*':
        return number_1 * number_2


def game_calc():
    name = welcome_user()
    print('What is the result of the expression?')

    operators = ["+", "-", "*"]
    count_correct_answer = 0

    for i in range(3):
        number_1 = random.randint(1, 50)
        number_2 = random.randint(1, 50)
        operator_choice = random.choice(operators)
        example = f'{number_1} {operator_choice} {number_2}'
        correct_answer = calculate(operator_choice, number_1, number_2)

        print(f'Question: {example}')
        answer = input('Your answer: ')

        if int(answer) == correct_answer:
            count_correct_answer += 1
            print('Correct!')
        else:
            print(f'''\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.
Let's try again, {name}!''')
            break
    if count_correct_answer == 3:
        print(f'Congratulations, {name}!')

if __name__ == "__main__":
    game_calc()

