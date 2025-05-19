from flask import Flask, render_template
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.after_request
def add_header(response):
    response.cache_control.max_age = 3600  # Cache for 1 hour
    return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Use PORT env var if available (Render), else 10000
    app.run(host='0.0.0.0', port=port)
