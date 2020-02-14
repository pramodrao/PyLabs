#file = fopen("/Users/pramod.rao/Desktop/Personal/Learn/Python/Coursera_Python_Data_Structures/mbox-short.txt")

fname = input("Enter a file name: ")
try:
    file = open(fname)
    for line in file:
        print(line.upper())
except:
    print("Invalid File Path.")
