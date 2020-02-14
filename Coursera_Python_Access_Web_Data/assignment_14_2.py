""" Assignment 14.2. of Coursera Python Web Access """


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
        service_url = "http://py4e-data.dr-chuck.net/json?"

        address = input("Enter address:")
        params = dict()
        params['address'] = address
        params['key'] = 42

        url = service_url + urllib.parse.urlencode(params)

        handler = urllib.request.urlopen(url, context=ctx)
        places_data = handler.read().decode()
        try:
            address_json = json.loads(places_data)
        except:
            address_json = None

        if not address_json or 'status' not in address_json or address_json['status'] != 'OK':
            print("Retrieval failed")
        else:
            print(address_json['results'][0]['place_id'])
    except:
        print(sys.exc_info())


main()
