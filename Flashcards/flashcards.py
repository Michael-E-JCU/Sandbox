""" Flashcards"""

import random


def main():
    print_menu()
    response = input("Enter response: ").lower()
    question_list = get_questions()
    answer_list = get_answers()
    while response != "q":
        if response == "a":
            print("In progress")
            print_menu()
            response = input("Enter response: ").lower()
        elif response == "p":
            complete_question(question_list, answer_list)
            print_menu()
            response = input("Enter response: ").lower()
        elif response == "i":
            print_instructions()
            print_menu()
            response = input("Enter response: ").lower()
        else:
            print("Invalid menu choice!")
            print_menu()
            response = str(input("Enter response: ")).lower()


def get_questions():  # Imports the text, and then for each line in the text, adds that to list and returns list.
    question_list = list(open("questions.txt", "r"))
    return question_list


def get_answers():  # Imports the text, and then for each line in the text, adds that to list and returns list.
    answer_list = list(open("answers.txt", "r"))
    return answer_list


def complete_question(question_list, answer_list):  # This is the function for completing the question.
    questions_answers_list = generate_random_question(question_list, answer_list)
    correct_answer = questions_answers_list[1]
    question = questions_answers_list[0]  # List has both answer and question in it.
    print(question)  # Prints the question from the question/answer list.
    response = str(input("Enter response here: ")).capitalize()  # Gets the user answer to above question
    while not return_to_menu(response):
        answer = validate_answer(response, correct_answer)  # Checks if the answer is correct
        print(answer)  # Prints if the answer is correct or not
        questions_answers_list = generate_random_question(question_list, answer_list)
        print(questions_answers_list[0])  # Prints the question
        response = str(input("Enter response here: ")).capitalize()  # Gets the user answer to above question


def print_instructions():
    print("""INSTRUCTIONSSSSSSSSSS!
You will be given a question and asked for an answer.. 
It will then print the result of your answer.
This process of questions and answer will repeat until the answer field if left blank or you enter 'menu'.\n""")


def return_to_menu(response):
    response = response.lower()
    if response == "m" or response == "menu" or response == "" or response == " ":
        return True
    return False


def print_menu():
    print("""MENU
(P)lay
(I)nstructions
(A)ccuracy
(Q)uit\n""")


def validate_answer(response, correct_answer):
    if response != correct_answer:
        return f"False! The correct answer is {correct_answer}\n"
    return f"Correct! {correct_answer}\n"


def generate_random_question(question_list, answer_list):  # Uses the len of the list to generate a random question
    number_items_in_list = len(question_list)
    number = random.randint(0, number_items_in_list - 1)
    question = question_list[number]
    answer = answer_list[number]
    return question, answer


main()
