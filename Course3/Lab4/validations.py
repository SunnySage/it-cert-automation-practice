#!/usr/bin/env python3
import re



def validate_user(username, min_length):

    # Check if the length of the username is at least min_length

    if len(username) < min_length:

        return False



    # Check if the username starts with an alphanumeric character

    if not username[0].isalnum():

        return False



    # Check if the username consists of only alphanumeric characters, underscores, and dots

    if not re.match("^[a-zA-Z0-9_.]+$", username):

        return False



    # Check if the username ends with an alphanumeric character

    if not username[-1].isalnum():

        return False



    return True



# Test cases

print(validate_user("blue.kale", 3))       # True

print(validate_user(".blue.kale", 3))      # False

print(validate_user("red_quinoa", 4))      # True

print(validate_user("_red_quinoa", 4))     # False


