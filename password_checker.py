MIN_LEN = 10


def main():
    password = input("Enter password here: ")
    while not get_valid_password(password):
        print("Invalid paassword length! Must be at least 10 characters.")
        password = input("Enter password here: ")
    for l in password:
        print("*", end="")


def get_valid_password(password):
    if len(password) < MIN_LEN:
        return False
    return True


main()
