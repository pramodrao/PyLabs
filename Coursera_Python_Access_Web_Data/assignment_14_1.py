""" Assignment 14.1. of Coursera Python Web Access """


import urllib.request
import urllib.parse
import urllib.error
import sys
import ssl
import json


def main():
    """ Main method """
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url = input("Enter url:")
        print("Retrieving:", url)
        jsondata = urllib.request.urlopen(url, context=ctx).read().decode()
        comments = json.loads(jsondata)['comments']
        sum_of_counts = 0
        for comment in comments:
            sum_of_counts = sum_of_counts + comment['count']
        print(sum_of_counts)
    except:
        print(sys.exc_info())


main()
