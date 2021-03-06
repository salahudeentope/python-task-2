import random
import string
import re


def password_generator():
    """
    a function to collect user inputs i.e email, first_name and last_name.
    It then automatically generates a password from the inputs.
    """
    first = input("Please enter your first name: ")
    last = input('Please enter your last name: ')
    email = input("Please enter your email: ")
    while not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email):  # regex to validate email
        email = input('please enter a valid email address: ')

    # the code below is used to generate a random 5-character string from ascii letters
    letters = string.ascii_letters
    random_string = "".join(random.sample(letters, 5))
    password = first[0:2] + last[-2:] + random_string
    return email, first, last, password


def user_details_container():
    """
    1. Function to interactively collect and store users details in a container continously
    until terminated when the last user is inputed.

    2. Users names are stored in a Title Case format.

    3. accepted inputs from interactive questions are ['yes', 'y', 'no', 'n'].

    4. The users details are stored in a nested dictionary with the key as the users email.
       This is to ensure that there aren't duplicate values.

    """

    users_container = dict()  # The container that will be used to store all the users details.
    new_user = "yes"

    # A while loop to ensure new users are continuously added until explicitly terminated.
    while new_user in ["yes", 'y']:

        ## collecting and storing the user's details. ##
        email, first, last, password = password_generator()

        ### checking if an email already exists in the container. ###
        while email in users_container:
            email = input('This email has been taken, please input a unique email: ')
        users_container[email] = {'email': email, 'first_name': first.title(), 'last_name': last.title()}

        print(password)
        choice = input("Do you like this password? [y/n]: ")

        # checking to confirm that a valid selection is made.
        while not choice.lower().replace(' ', '') in ['yes', 'y', 'no', 'n']:
            choice = input("please input a valid selection [y/n]: ")

        if choice.lower().replace(' ', '') in ['yes', 'y']:  # the .replace to take care of accidental spaces
            print('congratulation your details have been update successfully')
            users_container[email]['password'] = password
            # if the user likes the password, the program for that user terminates here.

            ### requesting if another user is available and validating the selection###
            new_user = input("Do you have another user to input? [y/n]: ")
            while not new_user.lower().replace(' ', '') in ['yes', 'y', 'no', 'n']:
                new_user = input("please input a valid selection [y/n]: ")
            new_user = new_user.lower().replace(' ', '')
            continue

        ### When the user doesn't like the password and would want to input theirs# ##
        elif choice.lower().replace(' ', '') in ['no', 'n']:
            new_choice = input("Kindly enter a password with 7 or more characters: ")

            while len(new_choice) < 7:  # to validate that the length is 7 or more.
                new_choice = input("password length must be 7 or more characters: ")
                continue
            print('congratulation your details have been updated successfully')
            users_container[email]['password'] = new_choice

            ### requesting if another user is available and validating the selection###
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
    print("Welcome to the HNG employees onboarding program")
    users()
