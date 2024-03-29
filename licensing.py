#!/usr/bin/env python3

import json
from urllib.request import urlopen


# Grab local license info
with open('license') as json_file:
    data = json.load(json_file)
    clientLicense = data["license"]
    clientID = data["id"]

# Grab license info from web
license_server_url = "https://raw.githubusercontent.com/jimender2/Licensing/master/licenses"
valid = False
for line in urlopen(license_server_url):
    data = json.loads(line)
    if clientLicense == data["license"]:
        if clientID == data["id"]:
            # need to check date too
            valid = True
            break

if valid:
    print("valid license")
    #start_program()

else:
    print("invalid license")
