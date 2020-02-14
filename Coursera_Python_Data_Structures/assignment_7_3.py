import sys

fname = input("Enter a file name: ")
try:
    file = open(fname)
    numlines = 0
    for line in file:
        numlines = numlines + 1
    print("There were", numlines, "in", fname)
except FileNotFoundError:
    if ( fname == "na na boo boo"):
        print("NA NA BOO BOO TO YOU - You have been punk'd")
    else:
        print("File cannot be opened: ", fname)
except:
    print("Error processing", sys.exc_info()[0])
    raise
