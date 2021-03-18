""" Flashcards"""

import random

INSTRUCTIONS = """INSTRUCTIONSSSSSSSSSS!
You will be given a question and asked for an answer.. 
It will then print the result of your answer.
This process of questions and answer will repeat until the answer field if left blank or you enter 'menu'.\n"""


def main():
    print_menu()
    response = input("Enter response: ").lower()
    question_list = get_questions()
    answer_list = get_answers()
    while response != "q":  # While loop for resposnes
        if response == "a":
            print("In progress")
            print_menu()
            response = input("Enter response: ").lower()
        elif response == "p":
            complete_question(question_list, answer_list)
            print_menu()
            response = input("Enter response: ").lower()
        elif response == "i":
            print(INSTRUCTIONS)
            print_menu()
            response = input("Enter response: ").lower()
        else:
            print("Invalid menu choice!")
            print_menu()
            response = str(input("Enter response: ")).lower()


def get_questions():  # Imports the text, and then for each line in the text, adds that to list and returns list.
    question_list = [line.strip("\n") for line in open("questions.txt", "r")]  # Strips \n from each line
    return question_list


def get_answers():  # Imports the text, and then for each line in the text, adds that to list and returns list.
    answer_list = [line.strip("\n") for line in open("answers.txt", "r")]  # Strips \n from each line
    return answer_list


def complete_question(question_list, answer_list):  # This is the function for completing the question.
    question, answer = generate_random_question(question_list, answer_list)  # Generates random question
    print(question)  # Prints the question from the question/answer list.
    response = str(input("Enter response here: ")).lower().capitalize()  # Gets the user answer to above question
    while not return_to_menu(response):
        print(answer)
        validate_response = validate_answer(response, answer)  # Checks if the answer is correct
        print(validate_response)  # Prints if the answer is correct or not
        question, answer = generate_random_question(question_list, answer_list)
        print(question)  # Prints the question
        response = str(input("Enter response here: ")).lower().capitalize()  # Gets the user answer to above question


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


def validate_answer(response, answer):
    if response != answer:
        return f"False! The correct answer is {answer}\n"
    return f"Correct! {answer}\n"


def generate_random_question(question_list, answer_list):  # Uses the len of the list to generate a random question
    number_items_in_list = len(question_list)
    number = random.randint(0, number_items_in_list - 1)
    question = question_list[number]
    answer = answer_list[number]
    return question, answer


main()
