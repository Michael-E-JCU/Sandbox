def main():
    print_menu()
    response = get_response()
    if response == "S":
        setup_thingy()
        print("Setup complete!")
        main()

    elif response == "O":
        print_owed()
        main()

    elif response == "C":
        calucumalate()
        main()

    elif response == "P":
        pay_bills()
        main()
    else:
        quit()


def print_menu():
    print("""Hello and welcome to my thingy.
(S)etup
(C)alucumalate
(O)wed
(P)ay
(Q)uit""")


def validate_response(response):
    if response != "S" and response != "C" and response != "Q" and response != "O" and response != "P":
        return False
    return True


def print_owed():
    in_file = open("owed.txt", "r")
    print(f"Money owed: ${in_file.readline()}")
    in_file.close()


def setup_thingy():
    out_file = open("name.txt", "w")
    name = str(input("Enter your name here: "))
    other_person = str(input("Enter name of other person: "))
    print(f"{name}", file=out_file)
    print(f"{other_person}", file=out_file)
    out_file.close()


def calucumalate():
    owed_file = open("owed.txt", "r")
    history = open("history.txt", "r+")
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
    history.readlines(-1)
    owed_file.close()
    history.close()


def pay_bills():
    owed_file = open("owed.txt", "r")
    owed = float(owed_file.readline())
    owed_file.close()
    paid = float(input("Enter amount paid: $"))
    total = owed - paid
    owed_file = open("owed.txt", "w")
    owed_file.flush()
    print(total, file=owed_file)
    owed_file.close()


def get_response():
    response = str(input(">>> ")).upper()
    while not validate_response(response):
        print("Invalid response!")
        response = str(input(">>> ")).upper()
    return response


main()
