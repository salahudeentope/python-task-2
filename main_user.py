import random
import string


def user_details_container():
    users_container = dict()
    new_user = "yes"
    while new_user in ["yes", 'y']:
        email = input("Please enter your email: ")
        first = input("Please enter your first name: ")
        last = input('Please enter your last name: ')
        users_container[email] = {'email': email, 'first_name': first, 'last_name': last}

        letters = string.ascii_letters
        random_string = "".join(random.sample(letters, 5))
        password = first[0:2] + last[-2:] + random_string
        print(password)

        choice = input("Do you like this password? [y/n]: ")
        if choice.lower().replace(' ', '') in ['yes', 'y']: # the .replace to take care of accidental spaces
            print('congratulation your account has been opened successfully')
            users_container[email]['password'] = password

            new_user = input("Do you have a new user to input?[y/n]: ")
            new_user = new_user.lower()
            continue
        elif choice.lower() in ['no', 'n']:
            while True:
                new_choice = input("Kindly enter a password with 7 or more characters: ")
                if len(new_choice) >= 7:
                    users_container[email]['password'] = new_choice
                    print('congratulation your account has been opened successfully')

                    # print(f'This is your account details {users[email]}')s
                    break
                elif len(new_choice) < 7:
                    continue
        new_user = input("Do you have a new user to input?[y/n]: ")
        new_user = new_user.lower()
        continue
    return users_container


def users():
    users_dict = user_details_container()
    print()
    for i, user in enumerate(users_dict.values()):
        print(f'User {i + 1}')
        for k, v in user.items():
            print(f"{k}: {v}")
        print()


if __name__ == "__main__":
    users()
