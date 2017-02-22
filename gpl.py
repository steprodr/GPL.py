#!/usr/bin/env python3

import requests, certifi, csv, credentials, os

version =2.0

#The credentials stored in credentials.py in the same directory as where this
#file is located the files we are going to read and write too

userid=credentials.username
passwd=credentials.password

in_file=os.path.normpath("/Cisco/glus.txt")
out_file=os.path.normpath("/Cisco/price.txt")
dest=open(out_file, "wt")

url='https://prpub.cloudapps.cisco.com/lpc/' 
payload='priceList=1109&format=Ascii+Flat+File&typeSelected=ProdOnly&commaSeparateInputsForUsageMatrix=' + userid + '%2C3%2C1-tier%2C'
headers= {
	'Origin':"https://prpub.cloudapps.cisco.com",
	'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
	'content-type': "application/x-www-form-urlencoded",
	'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	'accept-language': "en-US,en;q=0.5",
	'accept-encoding': "gzip, deflate, br",
	'X-Requested-With':"XMLHttpRequest"
}

#-----------------------------------------------------------------------------------------

# Request for the file, and authentication to the page

s = requests.Session()
s.auth = (userid, passwd)
s.verify = certifi.where()

print("Downloading the file")
thatfile=s.post(url  + 'servlet/DownloadEntirePL', headers=headers, data=payload)

with open(in_file, 'wb') as file:
	file.write(thatfile.content)
file.close()

#-----------------------------------------------------------------------------------------

print("Grooming the File")
with open(in_file, 'rt',)as groom:
	reader=csv.reader(groom, delimiter="|")
	writer=csv.writer(dest, delimiter="|")

	for row in reader:
		if "CORE" in row:
			writer.writerow((row[3], row[4], row[5]))

dest.close()
groom.close()
