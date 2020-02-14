""" Test 12.2. of Coursera Python Web Access """


import urllib.request
import urllib.parse
import urllib.error
import sys


def main():
    """ Main method """
    try:
        img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
        fhand = open("cover3.jpg", 'wb')
        fhand.write(img)
        fhand.close()
    except:
        print(sys.exc_info())


main()
