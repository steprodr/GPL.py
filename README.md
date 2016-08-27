# GPL.py
CURRENTLY BORKED

python script to pull the Cisco global price list (320M), and manipulate it to a usable size (~6M)

uses the requsts and csv modules

"credentials" is a python script with your CCO username and Password for obsfucation

username="CCO_Username"
password="CCO_password"

in_file="/Cisco/glus.txt" <---where you want to downlaod the ~300M file too
out_file="/Cisco/price.txt" <---- location of the "groomed" file


gpl.py python 3 version (tested with 3.5.2)
