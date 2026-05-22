#!/usr/bin/python3
"""JSON və CSV fayllarından məlumat oxuyub göstərən Flask tətbiqi."""
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file():
    """products.json faylını oxuyur və siyahı kimi qaytarır."""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_file():
    """products.csv faylını oxuyur və lüğət siyahısı kimi qaytarır."""
    products = []
    try:
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # CSV-dən oxunan dataları düzgün tipə çeviririk
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except (FileNotFoundError, KeyError, ValueError):
        pass
    return products


@app.route('/')
def home():
    """Əsas səhifə."""
    return render_template('index.html')


@app.route('/products')
def products_display():
    """Məhsulları mənbə və ID-yə görə filterləyib göstərir."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 1. Source yoxlanışı (Yalnız json və ya csv ola bilər)
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # Mənbəyə uyğun faylı oxuyuruq
    if source == 'json':
        products = read_json_file()
    else:
        products = read_csv_file()

    # 2. Əgər ID parametri göndərilibsə, filterləyirik
    if product_id is not None:
        try:
            target_id = int(product_id)
            # Həmin ID-li məhsulu axtarırıq
            filtered_products = [p for p in products if p.get('id') == target_id]
            
            if not filtered_products:
                return render_template('product_display.html', error="Product not found")
            
            products = filtered_products
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
