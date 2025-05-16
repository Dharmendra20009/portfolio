from flask import Flask, render_template

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
    app.run(debug=True, port=8080)
