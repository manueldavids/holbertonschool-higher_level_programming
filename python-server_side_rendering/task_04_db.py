from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_products():
    """
    Read products from JSON file
    """
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv_products():
    """
    Read products from CSV file
    """
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append(row)
        return products
    except FileNotFoundError:
        return []

def read_sql_products():
    """
    Read products from SQLite database
    """
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        
        conn.close()
        return products
    except sqlite3.Error:
        return []

@app.route('/products')
def products():
    """
    Route that handles JSON, CSV, and SQL data sources with filtering
    """
    # Get query parameters
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")
    
    # Read data based on source
    if source == 'json':
        products_data = read_json_products()
    elif source == 'csv':
        products_data = read_csv_products()
    else:  # sql
        products_data = read_sql_products()
    
    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products_data if int(p.get('id', 0)) == product_id]
            if not filtered_products:
                return render_template('product_display.html', error="Product not found")
            products_data = filtered_products
        except ValueError:
            return render_template('product_display.html', error="Invalid ID format")
    
    return render_template('product_display.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
