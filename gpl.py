#!/usr/bin/env python3

import requests
import certifi
import csv
import os
import credentials as creds

version = 3.4

'''
The credentials stored in credentials.py are in the same directory
where this file is located.
'''


glus = os.path.expanduser("~/Cisco/glus.txt")
price = os.path.expanduser("~/Cisco/price.txt")
old = os.path.expanduser("~/Cisco/price_old.txt")


class web():
    url = 'https://prpub.cloudapps.cisco.com/lpc/'
    payload = 'priceList=1109&format=Ascii+Flat+File&typeSelected=PAS' +\
        '&commaSeparateInputsForUsageMatrix=' + \
        creds.userid + '%2C3%2C1-tier%2C'
    headers = {
        'Origin': "https://prpub.cloudapps.cisco.com",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) " +
        "AppleWebKit/537.36 (KHTML, like Gecko) " +
        "Chrome/55.0.2883.95 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "text/html,application/xhtml+xml," +
        "application/xml;q=0.9,*/*;q=0.8",
        'accept-language': "en-US,en;q=0.5",
        'accept-encoding': "gzip, deflate, br",
        'X-Requested-With': "XMLHttpRequest"
    }


# Request for the file, and authentication to the page

def main():
    try:
        s = requests.Session()
        s.auth = (creds.userid, creds.passwd)
        s.verify = certifi.where()
        print("Downloading the file")
        thatfile = s.post(web.url + 'servlet/DownloadEntirePL',
                          headers=web.headers, data=web.payload)
        with open(glus, 'wb') as file:
            file.write(thatfile.content)
            file.close()
    except (SystemExit):
        raise
    except (KeyboardInterrupt):
        raise
    try:
        manipulate()
    except (SystemExit):
        raise


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
    if not os.path.isdir('~/Cisco/'):
        try:
            os.makedirs('~/Cisco/')
        except (SystemExit):
            raise


if __name__ == '__main__':
    main()
