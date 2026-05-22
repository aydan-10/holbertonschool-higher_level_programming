#!/usr/bin/python3
"""Flask framework-ü ilə qurulmuş sadə RESTful API."""
from flask import Flask, jsonify, request

app = Flask(__name__)

# İstifadəçiləri yaddaşda saxlamaq üçün boş lüğət (dictionary)
users = {}


@app.route('/')
def home():
    """Kök endpoint üçün xoş gəldiniz mesajı qaytarır."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Sistemdə qeydiyyatdan keçmiş bütün istifadəçi adlarının siyahısını qaytarır."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """API-ın statusunu qaytarır."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Verilmiş istifadəçi adına uyğun obyekt məlumatlarını qaytarır."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """POST sorğusu vasitəsilə sistemə yeni istifadəçi əlavə edir."""
    # Daxil olan datanın etibarlı JSON olub-olmadığını yoxlayırıq
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    # username sahəsinin varlığını yoxlayırıq
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # İstifadəçinin unikal olub-olmadığını yoxlayırıq
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Yeni istifadəçini lüğətə əlavə edirik
    users[username] = data

    response_data = {
        "message": "User added",
        "user": data
    }
    return jsonify(response_data), 201


if __name__ == "__main__":
    app.run()
