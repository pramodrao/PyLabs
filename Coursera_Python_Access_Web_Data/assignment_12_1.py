""" Assignment 12.1. of Coursera Python Web Access """


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

        url = input("Enter url:")
        html = urllib.request.urlopen(url, context=ctx).read()
        bsoup = BeautifulSoup(html, 'html.parser')

        tags = bsoup.findAll('span')
        sum_of_tags = 0
        for tag in tags:
            sum_of_tags = sum_of_tags + int(tag.contents[0])
        print(sum_of_tags)

    except:
        print(sys.exc_info())


main()
