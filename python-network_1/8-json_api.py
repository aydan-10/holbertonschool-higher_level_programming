#!/usr/bin/python3
"""Hərf parametri ilə POST sorğusu göndərən və JSON cavabını işləyən skript."""
import sys
import requests


if __name__ == "__main__":
    # Əgər arqument verilməyibsə boş sətir təyin edirik
    if len(sys.argv) < 2:
        q_letter = ""
    else:
        q_letter = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q_letter}

    try:
        response = requests.post(url, data=payload)
        # Cavabı JSON obyektinə çevirməyə çalışırıq
        json_data = response.json()

        # JSON düzgündürsə, amma boş obyektdirsə ({})
        if not json_data:
            print("No result")
        else:
            # ID və Name dəyərlərini təhlükəsiz şəkildə oxuyub formatlayırıq
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))

    except ValueError:
        # JSON formatı tamamilə xətalı/invalid olduqda
        print("Not a valid JSON")
