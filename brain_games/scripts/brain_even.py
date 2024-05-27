import random

def is_even(number):
    return number % 2 == 0

def get_correct_answer(number):
    return 'yes' if is_even(number) else 'no'

def main():
    print("Welcome to the Brain Game!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    correct_answers_count = 0
    wrong_answers_count = 0

    while correct_answers_count < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()

        correct_answer = get_correct_answer(number)

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
            wrong_answers_count = 0  # Reset wrong answers count on correct answer
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            wrong_answers_count += 1

            if wrong_answers_count >= 3:
                print(f"Let's try again, {name}!")
                correct_answers_count = 0  # Reset the correct answers count
                wrong_answers_count = 0  # Reset the wrong answers count

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()

