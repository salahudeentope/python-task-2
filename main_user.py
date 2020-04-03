import random
import string
import re


def password_generator():
    """
    a function to collect user inputs i.e email, first_name and last_name.
    It then automatically generates a password from the inputs.
    """
    email = input("Please enter your email: ")
    while not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email): # regex to validate email
        email = input('please enter a valid email address: ')
    first = input("Please enter your first name: ")
    last = input('Please enter your last name: ')

    # the code below is used to generate a random 5-character string from ascii letters
    letters = string.ascii_letters
    random_string = "".join(random.sample(letters, 5))
    password = first[0:2] + last[-2:] + random_string
    return email, first, last, password


def user_details_container():
    """
    Function to interactively collect and store users details in a container continously
    until terminated when the last user is inputed.
    Users names are stored in a Title Case format.

    accepted inputs from interactive questions are ['yes', 'y', 'no', 'n'].

    """
    users_container = dict()
    new_user = "yes"

    while new_user in ["yes", 'y']:
        email, first, last, password = password_generator()

        while email in users_container:
            email = input('This email has been taken, please input a unique email: ')

        users_container[email] = {'email': email, 'first_name': first.title(), 'last_name': last.title()}
        print(password)
        choice = input("Do you like this password? [y/n]: ")
        while not choice.lower().replace(' ', '') in ['yes', 'y', 'no', 'n']:
            choice = input("please input a valid selection [y/n]: ")
        if choice.lower().replace(' ', '') in ['yes', 'y']:  # the .replace to take care of accidental spaces
            print('congratulation your details have been update successfully')
            users_container[email]['password'] = password

            new_user = input("Do you have another user to input? [y/n]: ")

            while not new_user.lower().replace(' ', '') in ['yes', 'y', 'no', 'n']:
                new_user = input("please input a valid selection [y/n]: ")
            new_user = new_user.lower().replace(' ', '')
            continue
        elif choice.lower().replace(' ', '') in ['no', 'n']:
            new_choice = input("Kindly enter a password with 7 or more characters: ")
            while len(new_choice) < 7:
                new_choice = input("password length must be 7 or more characters: ")
                continue
            print('congratulation your details have been updated successfully')
            users_container[email]['password'] = new_choice

            new_user = input("Do you have another user to input?[y/n]: ")
            while not new_user.lower().replace(' ', '') in ['yes', 'y', 'no', 'n']:
                new_user = input("please input a valid selection [y/n]: ")
            new_user = new_user.lower().replace(' ', '')
            continue

    return users_container


def users():
    """
    The function prints the users details after the last user is inputted.
    It prints the users details nicely without mixing up any of the values.
    """

    users_dict = user_details_container()
    print()
    for i, user in enumerate(users_dict.values()):
        print(f'User {i + 1}')
        for k, v in user.items():
            print(f"{k}: {v}")
        print()


if __name__ == "__main__":
    users()
