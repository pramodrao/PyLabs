""" Test 12.1. of Coursera Python Web Access """


import socket
import sys


def main():
    """ Main method """
    try:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect(("data.pr4e.org", 80))
        cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
        mysock.send(cmd)

        count = 0
        alldata = ''
        while True:
            data = mysock.recv(512)
            if len(data) <  1:
                break
            count = count + len(data)
            print(len(data), count)
            alldata = alldata + data.decode()
        print(alldata)
        mysock.close()

    except:
        print(sys.exc_info())


main()
