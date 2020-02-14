""" Assignment 11.1. of Coursera Python Web Access """


import re
import sys


def main():
    """ Main method """
    fname = input("Please enter the file name:")
    try:
        file = open(fname)
        all_numbers = []
        for line in file:
            numbers = re.findall("[0-9]+", line.rstrip())
            if numbers:
                all_numbers.extend(numbers)
        all_numbers = list(map(int, all_numbers))
        print("Sum of all numbers is: ", sum(all_numbers))
    except FileNotFoundError:
        print("File not found.", fname)
    except:
        print(sys.exc_info())


main()
