""" Flashcards"""

import random


def main():
    print_menu()
    response = input("Enter response: ").lower()
    while not validate_response(response):
        response = str(input("Enter response: ")).lower()
    question_list = get_questions()
    answer_list = get_answers()
    while response != "q":
        if response == "a":
            print("In progress")
            print_menu()
            response = input("Enter response: ").lower()
        if response == "p":
            complete_question(question_list, answer_list)
            print_menu()
            response = input("Enter response: ").lower()
        if response == "i":
            print_instructions()
            print_menu()
            response = input("Enter response: ").lower()


def get_questions():  # Imports the text, and then for each line in the text, adds that to list and returns list.
    question_list = list(open("questions.txt", "r"))
    return question_list


def get_answers():  # Imports the text, and then for each line in the text, adds that to list and returns list.
    answer_list = list(open("answers.txt", "r"))
    return answer_list


def complete_question(question_list, answer_list):  # This is the function for completing the question.
    question = generate_random_question(question_list, answer_list)
    print(question[0])  # Prints the question
    answer = str(input("Enter response here: ")).capitalize()  # Gets the user answer to above question
    while not return_to_menu(answer):
        check = validate_answer(answer, question)  # Checks if the answer is correct
        print(check)  # Prints if the answer is correct or not
        question = generate_random_question(question_list, answer_list)
        print(question[0])  # Prints the question
        answer = str(input("Enter response here: ")).capitalize()  # Gets the user answer to above question


def print_instructions():
    print("""INSTRUCTIONSSSSSSSSSS!
You will be given a question and asked for an answer.. 
It will then print the result of your answer.
This process of questions and answer will repeat until the answer field if left blank or you enter 'menu'.\n""")


def return_to_menu(item):
    item = item.lower()
    if item == "m" or item == "menu" or item == "" or item == " ":
        return True
    return False


def print_menu():
    print("""MENU
(P)lay
(I)nstructions
(A)ccuracy
(Q)uit\n""")


def validate_answer(answer, question):
    if answer != question[1]:
        return f"False! The correct answer is {question[1]}\n"
    return f"Correct! {answer}\n"


def validate_response(response):  # Checks if the response is in the list of responses
    while response != "p" and response != "i" and response != "q" and response != "a":
        return False
    return True


def generate_random_question(question_list, answer_list):  # Uses the len of the list to generate a random question
    number_items_in_list = len(question_list)
    number = random.randint(0, number_items_in_list - 1)
    question = question_list[number]
    answer = answer_list[number]
    return question, answer


main()
