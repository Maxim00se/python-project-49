import random

def parity_check(number):
    return number % 2 == 0

def get_correct_answer(number):
    return 'yes' if is_even(number) else 'no'

def game():
    print("Welcome to the Brain Game!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".)

    correct_answers_count = 0

    for i in range(3):
        number = random.randint(1, 100)
        print(f'Questions: {number}') 
        answer = input('Your answer: ')
        if answer == get_correct_answer:
            correct_answers_count += 1
            print('Correct!')
            if correct_answer_count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f'''\'{answer}\' is wrong answer ;(. Correct answer '{get_correct_answer}'.
Let's try again, {name}!''') 

if __name__ == "__main__":
    game()

