import random
from brain_games.cli import welcome_user


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_correct_answer(number):
    return 'yes' if is_prime(number) else 'no'


def game_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers_count = 0

    for _ in range(3):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = input('Your answer: ')
        correct_answer = get_correct_answer(number)

        if answer == correct_answer:
            correct_answers_count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print("Let's try again, {name}!")
            break

    if correct_answers_count == 3:
        print(f'Congratulations, {name}!')
