#!/usr/bin/python3
"""JSONPlaceholder API-dən məlumat çəkən və işləyən modul."""
import csv
import requests


def fetch_and_print_posts():
    """Postları API-dən çəkir, status kodunu və başlıqları çap edir."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print("Status Code: {}".format(response.status_code))
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Postları API-dən çəkir və posts.csv faylına yazır."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Datadan yalnız id, title və body hissələrini filterləyirik
        structured_data = [
            {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            }
            for post in posts
        ]
        
        # CSV faylına yazma hissəsi
        with open('posts.csv', mode='w', encoding='utf-8', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()  # Sütun adlarını yazır (id, title, body)
            writer.writerows(structured_data)  # Bütün sətirləri əlavə edir
