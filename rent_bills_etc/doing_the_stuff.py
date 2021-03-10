import datetime


def main():
    print_menu()
    response = get_response()
    menu(response)


def menu(response):
    date = datetime.datetime.now().strftime("%c")
    if response == "S":
        setup_thingy()
        print("Setup complete!")
        main()

    elif response == "O":
        print_owed()
        main()

    elif response == "C":
        calucumalate(date)
        main()

    elif response == "P":
        pay_bills(date)
        main()
    elif response == "H":
        print_history()
        main()
    else:
        quit()


def print_menu():
    print("""Hello and welcome to my thingy.
(S)etup
(C)alucumalate
(O)wed
(P)ay
(H)istory
(Q)uit""")


def validate_response(response):
    if response != "S" and response != "C" and response != "Q" and response != "O" and response != "P" and \
            response != "H":
        return False
    return True


def print_owed():
    in_file = open("owed.txt", "r")
    print("\n")
    print(f"Money owed: ${in_file.readline()}")
    in_file.close()


def setup_thingy():
    out_file = open("name.txt", "w")
    name = str(input("Enter your name here: "))
    other_person = str(input("Enter name of other person: "))
    print(f"{name}", file=out_file)
    print(f"{other_person}", file=out_file)
    out_file.close()


def calucumalate(date):
    owed_file = open("owed.txt", "r")
    history = open("history.txt", "a")
    electricity = float(input("Electricity : $"))
    water = float(input("Water + Hot water : $"))
    gas = float(input("Enter gas : $"))
    internet = float(input("Enter Internet : $"))
    rent = float(input("Enter rent : $"))
    owed = float(owed_file.readline())
    total = ((electricity + water + gas + internet + rent) / 2) + owed
    owed_file.close()
    owed_file = open("owed.txt", "w")
    owed_file.flush()
    print(total, file=owed_file)
    owed_file.close()
    print("\n")
    print(f"On the {date}\n${total} was owed.")
    print(f"On the {date}\n${total} was owed.\n", file=history)
    history.close()


def pay_bills(date):
    owed_file = open("owed.txt", "r")
    owed = float(owed_file.readline())
    owed_file.close()
    paid = float(input("Enter amount paid: $"))
    total = owed - paid
    owed = total
    owed_file = open("owed.txt", "w")
    history = open("history.txt", "a")
    print("\n")
    print(f"{date}\n${paid} was paid, leaving ${owed} owed.")
    print(f"\n{date}\n${paid} was paid, leaving ${owed} owed.", file=history)
    history.close()
    owed_file.flush()
    print(total, file=owed_file)
    owed_file.close()


def print_history():
    history = open("history.txt", "r")
    for lines in history:
        print(lines)
    history.close()


def get_response():
    response = str(input(">>> ")).upper()
    while not validate_response(response):
        print("Invalid response!")
        response = str(input(">>> ")).upper()
    return response


def get_names():
    names = []
    in_file = open("name.txt", "r")
    for lines in in_file:
        names.append(lines)
    return names


main()
