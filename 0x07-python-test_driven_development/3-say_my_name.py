#!/usr/bin/python3
# 0-add_integer.py
# John Harrison U <ugochukwujohn2014@gmail.com>
"""Defines an integer addition function."""

def say_my_name(first_name, last_name=""):
    """ A function that prints My name is <first name> <last name>.
    Args:
        first_name: Stores the User First name
        last_name:  Stores the User Last name
    Raises:
        TypeError: If the first_name is not a string
        TypeError: If the last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
