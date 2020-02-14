""" Assignment 12.2. of Coursera Python Web Access """


import urllib.request
import urllib.parse
import urllib.error
import sys
import ssl
from bs4 import BeautifulSoup


def main():
    """ Main method """
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url = input("Enter start url:")
        count = int(input("Enter count:"))
        position = int(input("Enter position:")) - 1

        print("Retrieving:", url)
        html = urllib.request.urlopen(url, context=ctx).read()
        bsoup = BeautifulSoup(html, 'html.parser')

        parent_tag = bsoup('a')[position]
        count = count - 1
        while count > 0:
            count = count - 1
            url = parent_tag.get('href', None)
            print("Retrieving:", url)
            html = urllib.request.urlopen(url, context=ctx).read()
            bsoup = BeautifulSoup(html, 'html.parser')
            parent_tag = bsoup('a')[position]
        print(parent_tag.contents[0])

    except:
        print(sys.exc_info())


main()
