#!/usr/bin/env python3

import requests
import certifi
import csv
import os
import credentials as creds
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
req_log = logging.getLogger('urllib3')
req_log.setLevel(logging.DEBUG)
req_log.propagate = True

version = 3.4

'''
The credentials stored in credentials.py are in the same directory
where this file is located.
'''


base = os.path.expanduser("~/Cisco")
glus = os.path.expanduser("~/Cisco/glus.txt")
price = os.path.expanduser("~/Cisco/price.txt")


class web():
    auth_url = 'https://prpub.cloudapps.cisco.com/lpc/currentPL.faces?flow=nextgen'
    url = 'https://prpub.cloudapps.cisco.com/lpc/servlet/DownloadEntirePL'
    payload = 'priceList=1109&format=Ascii+Flat+File&typeSelected=PAS' +\
        '&commaSeparateInputsForUsageMatrix=' + \
        creds.userid + '%2C3%2C1-tier%2C' + \
        '&selectedColFrom=%2C%2C%2C7%2C11%2C12%2C14%2C15%2C16%2C17%2C19%2C20' +\
        '&selectedColTo='
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': "https://prpub.cloudapps.cisco.com",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) " +
            "AppleWebKit/537.36 (KHTML, like Gecko) " +
            "Chrome/74.0.3729.169 Safari/537.36",
        'X-Requested-With': "XMLHttpRequest"
    }


# Request for the file, and authentication to the page
def get_file():
    s = requests.Session()
    s.auth = (creds.userid, creds.passwd)
    s.verify = certifi.where()
    s.post(web.auth_url, headers=web.headers)
    print("Downloading the file")
    thatfile = s.post(web.url,
                      headers=web.headers, data=web.payload)
    with open(glus, 'wb') as file:
        file.write(thatfile.content)
        file.close()


def manipulate():
    print("Grooming the File")
    dest = open(price, "wt")
    with open(glus, 'rt',)as groom:
        reader = csv.reader(groom, delimiter="|")
        writer = csv.writer(dest, delimiter="|")

        for row in reader:
            if "CORE" in row:
                writer.writerow((row[3], row[4], row[6]))
        dest.close()
        groom.close()


def path_exists():
    if not os.path.isdir(base):
        try:
            os.makedirs(base)
        except (SystemExit):
            raise


def main():
    try:
        from http.client import HTTPConnection
    except ImportError:
        from httplib import HTTPConnection
    HTTPConnection.debuglevel = 1
    path_exists()
    get_file()
    manipulate()


if __name__ == '__main__':
    main()
