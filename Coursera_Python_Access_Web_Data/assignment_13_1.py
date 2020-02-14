""" Assignment 13.1. of Coursera Python Web Access """


import urllib.request
import urllib.parse
import urllib.error
import sys
import ssl
import xml.etree.ElementTree as ET


def main():
    """ Main method """
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url = input("Enter url:")
        print("Retrieving:", url)
        xmldata = urllib.request.urlopen(url, context=ctx).read()
        tree = ET.fromstring(xmldata)
        counts = tree.findall('.//count')
        sum_of_counts = 0
        for count in counts:
            sum_of_counts = sum_of_counts + int(count.text)
        print(sum_of_counts)
    except:
        print(sys.exc_info())


main()
