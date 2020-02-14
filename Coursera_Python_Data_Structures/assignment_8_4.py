""" Assignment 8, Exercise 4 of Coursera_Python_Data_Structures."""


def main():
    """ Main Method """
    fname = input("Enter the file name: ")
    try:
        file = open(fname)
    except FileNotFoundError:
        print("File not found in the path: ", fname)

    word_list = []
    for line in file:
        words = line.split()
        for word in words:
            # print(word, word_list)
            if word not in word_list:
                word_list.append(word)

    word_list.sort()
    print(word_list)


main()
