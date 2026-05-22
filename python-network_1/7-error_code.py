#!/usr/bin/python3
"""requests ilə URL sorğusu göndərən və HTTP xətalarını yoxlayan skript."""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
