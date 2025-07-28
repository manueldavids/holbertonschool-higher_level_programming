from flask import Flask, render_template, request
import json
import csv

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

@app.route('/products')
def products():
    """
    Route that handles both JSON and CSV data sources with filtering
    """
    # Get query parameters
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    # Read data based on source
    if source == 'json':
        products_data = read_json_products()
    else:  # csv
        products_data = read_csv_products()
    
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
