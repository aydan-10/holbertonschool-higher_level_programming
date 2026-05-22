#!/usr/bin/python3
"""Jinja şablonları ilə işləyən əsas Flask tətbiqi."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Əsas səhifəni (index.html) render edir."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Haqqımızda səhifəsini (about.html) render edir."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Əlaqə səhifəsini (contact.html) render edir."""
    return render_template('contact.html')


if __name__ == '__main__':
    # Şərtdə tələb olunan port 5000 təyin edilir
    app.run(debug=True, port=5000)
