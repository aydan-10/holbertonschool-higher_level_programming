#!/usr/bin/python3
"""JSON, CSV və SQLite bazasından məlumat oxuyan Flask tətbiqi."""
import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file():
    """products.json faylını oxuyur."""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_file():
    """products.csv faylını oxuyur."""
    products = []
    try:
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except (FileNotFoundError, KeyError, ValueError):
        pass
    return products


def read_sql_data(product_id=None):
    """SQLite3 bazasından məhsulları oxuyur, lazım gəldikdə filterləyir."""
    products = []
    conn = None
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Sütun adları ilə oxumaq üçün
        cursor = conn.cursor()

        if product_id is not None:
            cursor.execute('SELECT id, name, category, price FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT id, name, category, price FROM Products')

        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row["id"],
                "name": row["name"],
                "category": row["category"],
                "price": row["price"]
            })
    except sqlite3.Error:
        pass
    finally:
        if conn:
            conn.close()
    return products


@app.route('/')
def home():
    """Əsas səhifə."""
    return render_template('index.html')


@app.route('/products')
def products_display():
    """Məhsulları mənbəyə (json, csv, sql) və ID-yə görə göstərir."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 1. Mənbə düzgünlüyünün yoxlanılması
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # SQL mənbəyi üçün xüsusi məntiq
    if source == 'sql':
        if product_id is not None:
            try:
                target_id = int(product_id)
                products = read_sql_data(target_id)
                if not products:
                    return render_template('product_display.html', error="Product not found")
            except ValueError:
                return render_template('product_display.html', error="Product not found")
        else:
            products = read_sql_data()
    else:
        # JSON və ya CSV mənbəyi
        if source == 'json':
            products = read_json_file()
        else:
            products = read_csv_file()

        # ID filterlənməsi (JSON və CSV üçün)
        if product_id is not None:
            try:
                target_id = int(product_id)
                filtered_products = [p for p in products if p.get('id') == target_id]
                if not filtered_products:
                    return render_template('product_display.html', error="Product not found")
                products = filtered_products
            except ValueError:
                return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
