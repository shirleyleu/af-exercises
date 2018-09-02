#!/usr/bin/env python3

import requests

r = requests.get('https://www.google.com')
if r.status_code == requests.codes.ok:
    print("It looks like you're connected to the Internet")
else:
    print("No internet")
