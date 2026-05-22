#!/usr/bin/python3
"""GitHub API vasitəsilə istifadəçi ID-sini oxuyan skript."""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"

    # HTTP Basic Authentication ilə təhlükəsiz sorğu göndəririk
    response = requests.get(url, auth=(username, token))

    try:
        json_data = response.json()
        # JSON obyektindən 'id' dəyərini təhlükəsiz şəkildə oxuyuruq
        print(json_data.get('id'))
    except ValueError:
        print("None")
