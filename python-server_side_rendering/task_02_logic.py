from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    """
    Route that reads items from JSON file and renders them dynamically
    """
    try:
        # Read items from JSON file
        with open('items.json', 'r') as file:
            data = json.load(file)
            items = data.get('items', [])
    except FileNotFoundError:
        # Handle case when file doesn't exist
        items = []
    except json.JSONDecodeError:
        # Handle case when JSON is invalid
        items = []
    
    # Pass items to template for rendering
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
