from brain_games.cli import welcome_user
import random
import math


def game_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count_correct_answers = 0
    for i in range(3):
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        correct_answer = math.gcd(a, b)
        print(f"Question: {a} {b}")
        answer = input('Your answer: ')
        if int(answer) == correct_answer:
            count_correct_answers += 1
            print('Correct!')
        else:
            print(f'''\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.
Let's try again, {name}!''')
            break
        if count_correct_answers == 3:
            print(f"Congratulations, {name}")

if __name__ == "__main__":
    game_gcd()
