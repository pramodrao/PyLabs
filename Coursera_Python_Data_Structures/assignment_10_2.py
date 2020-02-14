""" Assignment 10, Exercise 2 of Coursera_Python_Data_Structures."""


def main():
    """ Main Method """
    fname = input("Enter the file name: ")
    try:
        file = open(fname)
    except FileNotFoundError:
        print("File not found in the path: ", fname)

    hour_counts = dict()
    for line in file:
        words = line.split()
        if len(words) > 5 and words[0] == "From":
            time = words[5]
            (hour, minute, second) = time.split(":")
            hour_counts[hour] = hour_counts.get(hour, 0) + 1

    sorted_hour_counts = list()
    for (key, val) in hour_counts.items():
        sorted_hour_counts.append((key, val))

    sorted_hour_counts.sort()
    for (key, val) in sorted_hour_counts:
        print(key, val)


main()
