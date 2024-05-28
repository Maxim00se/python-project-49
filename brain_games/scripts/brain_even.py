import random
from brain_games.cli import welcome_user


def parity_check(number):
    return number % 2 == 0

def get_correct_answer(number):
    return 'yes' if parity_check(number) else 'no'

def game_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers_count = 0

    for i in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}') 
        answer = input('Your answer: ')
        if answer == get_correct_answer(number):
            correct_answers_count += 1
            print('Correct!')
            if correct_answers_count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f'''\'{answer}\' is wrong answer ;(. Correct answer '{get_correct_answer(number)}'.
Let's try again, {name}!''')
            break 

if __name__ == "__main__":
    game_even()

