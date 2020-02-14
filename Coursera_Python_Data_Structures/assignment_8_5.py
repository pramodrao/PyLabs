""" Assignment 8.5 of Coursera_Python_Data_Structures."""


def main():
    """ Main Method """
    fname = input("Enter the file name: ")
    try:
        file = open(fname)
    except FileNotFoundError:
        print("File not found in the path: ", fname)

    count = 0
    for line in file:
        words = line.split()
        if len(words) > 1 and words[0] == "From":
            print(words[1])
            count = count + 1

    print("There were", count, "lines in the file with From as the forst word")


main()

# def main():
#     """ Main Method """
#     fname = input("Enter the file name: ")
#     try:
#         file = open(fname)
#     except FileNotFoundError:
#         print("File not found in the path: ", fname)
#
#     mails_from = []
#     count = 0
#     for line in file:
#         words = line.split()
#         if ( len(words) > 2 and words[0] == "From" ):
#             if words[1] not in mails_from:
#                 mails_from.append(words[1])
#
#     mails_from.sort()
#     print(mails_from)
#
#
# main()
