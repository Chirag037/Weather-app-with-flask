from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "your api key"  # Get from https://openweathermap.org/api

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            weather = {
                'city': city.title(),
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].title(),
                'icon': data['weather'][0]['icon']
            }
        else:
            weather = 'not_found'
    return render_template('index.html', weather=weather)
    
if __name__ == '__main__':
    app.run(debug=True)
