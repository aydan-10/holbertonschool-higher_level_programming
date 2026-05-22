#!/usr/bin/python3
"""URL sorğusundan X-Request-Id header dəyərini oxuyan skript."""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        # Header məlumatları içindən X-Request-Id-ni götürürük
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
