# GPL.py

GPL version 3.4

python script to pull the Global Price list, US Availability from Cisco's website, and manipulate it to a usable size (~6M)

Script uses requests and certifi modules which need to be installed.

"credentials" is a python script with your CCO username and Password for obsfucation, stored in the same directory as this script

userid="CCO_Username"

passwd="CCO_password"

~~glus= <---where you want to download the file too~~

~~price= <---- location of the "groomed" file called by the search script~~

~~price_old <----backup of the price.txt for manipulation/evaluation by another script down the road~~

The script will check for a Cisco directory in the users home folder/path, if it does not exist
it will create it. Filenames have not changed.

gpl.py python 3 version (tested with 3.6, 3.7)
