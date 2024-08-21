from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__) # makes app a Flask app

# Routes
@app.route('/') # home page
@app.route('/index') # alias for home page
def index(): # return something after each rotue
    return render_template('index.html') # render index.html template

@app.route('/weather')
def get_weather():
    city = request.args.get('city') # get city from user input
    weather_data = get_current_weather(city) # pass in city data to weather_data
    
    return render_template('weather.html',              # Template to fill
                           title=weather_data['name'],  # pass city name to template
                           status=weather_data['weather'][0]['description'].capitalize(), # get status
                           temp=f"{weather_data['main']['temp']:.1f}", # get temperature
                           feels_like = f"{weather_data['main']['feels_like']:.1f}" # get feels like temperature
                                   
    ) # send weather data to template

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000) # runs the app on localhost:5000
    serve(app, host='0.0.0.0', port=5000) # serves using waitress now
    
    