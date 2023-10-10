from flask import Flask, render_template, request, flash, redirect, url_for
import requests
import os

secret_key = os.urandom(24)
print(secret_key.hex())

app = Flask(__name__)
app.secret_key = secret_key


API_key = "4a37e0bcb370eefc8346743b67625058"
API_URL = 'https://api.openweathermap.org/data/2.5/weather'
    # user_input = "Jauharabad"
    # weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
    # wea = Weather = weather_data.json()
    # print(wea)

@app.route("/jauharabad", methods=['GET'])
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        if location:
            params = {'q': location, 'appid': API_key, 'units': 'metric'}
            
    if request.method == 'GET': 
        location = "Jauharabad"
        params = {'q': location, 'appid': API_key, 'units': 'metric'}

    response = requests.get(API_URL, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        Weather = weather_data['weather'][0]['main']
        Temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        Min_temp = weather_data['main']['temp_min']
        Max_temp = weather_data['main']['temp_max']
        humidity = weather_data['main']['humidity']
        visibility = weather_data['visibility']
        wind_speed = weather_data['wind']['speed']
        sunrise = weather_data['sys']['sunrise']
        sunset = weather_data['sys']['sunset']
        latitude = weather_data['coord']['lat']
        longitude = weather_data['coord']['lon']
        pressure = weather_data['main']['pressure']
        return render_template("weather.html", Weather=Weather, Temp=Temp, feels_like=feels_like,
                    Min_temp=Min_temp, max_temp=Max_temp, humidity=humidity, visibility=visibility, 
                    wind_speed=wind_speed, sunrise=sunrise, sunset=sunset, lat=latitude, lon=longitude,
                    pressure=pressure, location=location)
    else:
        error_message = f"Error: {weather_data['message']}"    
        return render_template('weather.html', error_message=error_message)


if __name__ == "__main__":
    app.run(debug=True)