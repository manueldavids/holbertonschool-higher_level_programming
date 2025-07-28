from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """
    Home route that renders the main index page
    """
    return render_template('index.html')

@app.route('/about')
def about():
    """
    About route that renders the about page
    """
    return render_template('about.html')

@app.route('/contact')
def contact():
    """
    Contact route that renders the contact page
    """
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
