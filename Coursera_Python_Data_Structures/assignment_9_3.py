""" Assignment 9, Exercise 3 of Coursera_Python_Data_Structures."""


def main():
    """ Main Method """
    fname = input("Enter the file name: ")
    try:
        file = open(fname)
    except FileNotFoundError:
        print("File not found in the path: ", fname)

    mail_count = dict()
    domain_name_count = dict()
    for line in file:
        words = line.split()
        if len(words) > 1 and words[0] == "From":
            mail_count[words[1]] = mail_count.get(words[1], 0) + 1
            domain_name = words[1].split("@")[1]
            new_count = domain_name_count.get(domain_name, 0) + 1
            domain_name_count[domain_name] = new_count

    print("Email Counts:")
    print(mail_count)
    print("\nDomain Name Counts:")
    print(domain_name_count)

    max_mail_person = None
    max_mail_count = 0
    for email in mail_count:
        if max_mail_person is None or max_mail_count < mail_count[email]:
            max_mail_person = email
            max_mail_count = mail_count[email]

    print("\nMax Emails", max_mail_count, " received by ", max_mail_person)


main()
