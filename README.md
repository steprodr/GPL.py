# GPL.py

python script to pull the Global Price list, US Availability from Cisco's website, and manipulate it to a usable size (~6M)

GPL version 4.0

Requires Selenium and GeckoDriver(Firefox driver)

due ot a backend change, version 4.0 is a rewrite of the module that gets the file, requests is no longer being used.

"credentials" is a python script with your CCO username and Password for obsfucation, stored in the same directory as this script

userid="CCO_Username"

passwd="CCO_password"


The script will check for a Cisco directory in the users home folder/path, if it does not exist
it will create it. 

gpl.py python 3 version (tested with 3.7)
