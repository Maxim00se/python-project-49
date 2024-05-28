import random
from brain_games.cli import welcome_user


def game_calc():
    name = welcome_user()
    
    number_1 = random.randint(1, 50)
    number_2 = random.randint(1, 50)
    operator = random.choice([+, -, *])
    example = f'{number_1} {operator} {number_2}'
    count_current_answer = 0
    print(f'Question: {example}')
    answer = input(f'Your answer: ')
    
    for i in range(3):
        if answer == int(example):
            count_current_answer += 1
            print('Correct')
            if count_current_answer == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f'''\'{answer}\' is wrong answer ;(. Correct answer was \'{int(example)}\'.
Let's try again, {name}!''')
            return

if __name__ == "__main__":
    game_calc()

