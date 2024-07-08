import random
from brain_games.cli import welcome_user

def generate_progression(start, step, length=10):
    return [start + step * i for i in range(length)]

def hide_element(progression, hidden_index):
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'
    return hidden_value, progression

def game_progression():
    name = welcome_user()
    print('What number is missing in the progression?')

    rounds = 3
    for _ in range(rounds):
        start = random.randint(1, 100)
        step = random.randint(1, 15)
        length = 10  

        progression = generate_progression(start, step, length)
        hidden_index = random.randint(0, length - 1)
        hidden_value, hidden_progression = hide_element(progression, hidden_index)

        print(f'Question: {" ".join(map(str, hidden_progression))}')
        answer = input('Your answer: ')

        if answer.isdigit() and int(answer) == hidden_value:
            print('Correct!')
        else:
            print(f'''\'{answer}\' is wrong answer ;(. Correct answer was \'{hidden_value}\'.
Let's try again, {name}!''')
            break
    else:
        print(f'Congratulations, {name}!')

if __name__ == "__main__":
    game_progression()

