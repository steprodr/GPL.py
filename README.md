# GPL.py

GPL version 3.2

python script to pull the Global Price list, US Availability from Cisco's website, and manipulate it to a usable size (~6M)
	**I am now requesitng the file from a different server. New location is actually kept up to date!

Script uses requests and certifi modules which need to be installed.
credentials is a python script with your CCO username and Password for obsfucation

userid="CCO_Username"

passwd="CCO_password"

glus= <---where you want to downlaod the file too
price= <---- location of the "groomed" file called by the search script
price_old <----backup of the price.txt for manipulation/evaluation by another script down the road


gpl.py python 3 version (tested with 3.6)
