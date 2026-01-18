from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Index Page</p>"

@app.route('/hello')
def hello_world():
    return "<p>Hello, World!</p>"

# As if saying, If someone runs this file directly, start the Flask server
# This block prevents the server from starting if this file is imported as a module
if __name__ == '__main__':
    app.run(debug=True)