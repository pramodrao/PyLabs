""" Assignment 9, Exercise 2 of Coursera_Python_Data_Structures."""


def main():
    """ Main Method """
    fname = input("Enter the file name: ")
    try:
        file = open(fname)
    except FileNotFoundError:
        print("File not found in the path: ", fname)

    mail_days = dict()
    for line in file:
        words = line.split()
        if ( len(words) > 2 and words[0] == "From" ):
            if words[2] not in mail_days:
                mail_days[words[2]] = 1
            else:
                mail_days[words[2]] = mail_days[words[2]] + 1

    print(mail_days)


main()
