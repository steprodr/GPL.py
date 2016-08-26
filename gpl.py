#!/usr/bin/env python3

import requests, csv, credentials

#The credentials stored in credentials.py in the same directory as where this
#file is located the files we are going to read and write too

userid=credentials.username
passwd=credentials.password

in_file="/Cisco/glus.txt"
out_file="/Cisco/price.txt"
dest=open(out_file, "wt", encoding='utf-8')

url='http://www.cisco.com/web/lpc/ascii/glus.web'

#-----------------------------------------------------------------------------------------

# Request for the file, and authentication to the page

s = requests.Session()
s.auth = (userid, passwd)
s.verify = False
s.headers.update({'x-test': 'true'})

print("Downloading the file")
thatfile = s.get(url, headers={'x-test': 'true'})

with open(in_file, 'wt') as file:
	file.write(str(thatfile.content))
file.close()

#-----------------------------------------------------------------------------------------

print("Grooming the File")
with open(in_file, 'rt')as groom:
	reader=csv.reader(groom, delimiter="|")
	writer=csv.writer(dest, delimiter="|")

	for row in reader:
		if "Product" in row:
			writer.writerow((row[3], row[4], row[6]))

dest.close()
groom.close()
