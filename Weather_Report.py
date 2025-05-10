import requests
import os 
from dotenv import load_dotenv
load_dotenv()

def fetch_weather(city,api_key):
    url =f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response=requests.get(url)
        if response.status_code == 200:
            data = response.json()

            main = data['main']
            weather = data['weather'][0] 
            temperature = main['temp']
            humidity = main ['humidity'] 
            description = weather['description']
            wind_speed = data['wind']['speed']

            print(f'Weather in {city.capitalize()}:')
            print(f'Temperature: {temperature}.C')
            print(f'Humidity: {humidity}%')
            print(f'Description: {description.capitalize()}')
            print(f'Wind Speed: {wind_speed}m/s')

        else:
            print("City not found or invalid API key.")
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    city=input('Enter city name: ')
    api_key=os.getenv('OPENWEATHER_API_KEY')
    fetch_weather(city,api_key)