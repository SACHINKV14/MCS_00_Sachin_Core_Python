from flask import Flask, render_template, request, redirect
import json
import urllib.request
import os, requests


app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def hello_world():
    if request.method == 'POST':
        city = request.form['id']

        api_key="4cf89cd43100161af6befd2d155c68f0"

        construct_url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=" + api_key
        response = requests.get(construct_url)
        list_of_data = response.json()

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                          + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)

        return render_template('index.html',data=data)


    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)