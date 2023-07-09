import string
import getpass
import sys


def check_password_strength(password):
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    # Rest of the code remains the same


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'y':
        password = getpass.getpass('Enter the password: ')
        check_password_strength(password)
    else:
        print('Exiting...')
        input()
