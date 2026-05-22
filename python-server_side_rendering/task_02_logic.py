#!/usr/bin/python3
"""Dinamik dövr və şərt məntiqlərini icra edən Flask tətbiqi."""
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Əsas səhifəni render edir."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Haqqımızda səhifəsini render edir."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Əlaqə səhifəsini render edir."""
    return render_template('contact.html')


@app.route('/items')
def items_list():
    """JSON faylından məlumatları oxuyur və items.html şablonuna ötürür."""
    try:
        with open('items.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            # JSON obyektindən 'items' siyahısını götürürük
            items = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items = []

    return render_template('items.html', items=items)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
