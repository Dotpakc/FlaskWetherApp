from flask import Flask , render_template
import os
import requests
import json


app = Flask(__name__)

@app.route('/')
def index():
    api_key = 'API KEY'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&lang=ua&appid='+ api_key
    
    cities = ["Днепр",'Киев','Синельниково','Львов','Харьков']
    
    all_temp_data = []
    for city in cities:
        res = requests.get(url.format(city))
        
        res_dict = json.loads(res.text)
        print(res_dict['main']['temp'])
        
        temp_data = {
            'city': city,
            'temp': round(res_dict['main']['temp']),
            'humidity' : res_dict['main']['humidity'],
            'weather_description' : res_dict['weather'][0]['description'],
            'weather_icon' : res_dict['weather'][0]['icon'],
        }
        all_temp_data.append(temp_data)
    
    return render_template('index.html',all_temp_data=all_temp_data)



if __name__ == '__main__':
    app.run(debug = True)