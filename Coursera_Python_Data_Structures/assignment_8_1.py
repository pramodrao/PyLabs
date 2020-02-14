""" Assignment 8 of Coursera_Python_Data_Structures."""


def chop(a_list):
    """ Remove the head and tail of the given list."""
    del a_list[0]
    del a_list[len(a_list)-1]


def middle(a_list):
    """ Return the middle of the given list."""
    return a_list[1:len(a_list)-1]
