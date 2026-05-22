#!/usr/bin/python3
"""requests paketi ilə URL-dən X-Request-Id header-ini oxuyan skript."""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
