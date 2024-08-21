from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__) # makes app a Flask app

# Routes
@app.route('/') # home page
@app.route('/index') # alias for home page
def index(): # return something after each rotue
    return "Hello, World!"

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000) # runs the app on localhost:5000
    serve(app, host='0.0.0.0', port=5000) # serves using waitress now
    
    