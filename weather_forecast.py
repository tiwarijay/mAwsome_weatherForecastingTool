# Goal: to make 'Weather Forecasting Tool' using OpenWeatherMap API and Python. 
# Requirements: 
    # Create a command line tool that accepts a city's name and returns the current weather forecast. 
    # Leverage OpenWeatherMap API to fetch weather data and parse it using Python.

# Importing the required libraries
import requests
import json
import os


# Let's define a class for your Weather Forecasting Tool and call it 'WeatherForecast'
class WeatherForecast:
    def __init__(self, api_key):
        self.api_key = api_key

    # Let's define a method to get the weather forecast for a city
    def get_forecast(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        response = requests.get(url)

        # Let's check the status code of the response, and print the appropriate message
        if response.status_code == 200:
            print("Success!")
        elif response.status_code == 404:
            print("Not Found.")
        elif response.status_code == 401:
            print("Unauthorized.")
        elif response.status_code == 403:
            print("Forbidden.")
        elif response.status_code == 400:
            print("Bad Request.")
        elif response.status_code == 500:
            print("Internal Server Error.")
        elif response.status_code == 502:
            print("Bad Gateway.")
        elif response.status_code == 503:
            print("Service Unavailable.")
        elif response.status_code == 504:
            print("Gateway Timeout.")
        else:
            print("Unknown Error.")



        # Let's convert the response to JSON format
        data = json.loads(response.text)
        # TODO: Parse the weather data and extract the required information

        print('data:',data)

        # Let's print the weather forecast for the city
        print(f"The weather forecast for {city} is: {data['weather'][0]['description']}")
        print(f"The temperature is: {data['main']['temp']}")
        print(f"The humidity is: {data['main']['humidity']}")
        print(f"The wind speed is: {data['wind']['speed']}")
        print(f"The cloudiness is: {data['clouds']['all']}")
        print(f"The pressure is: {data['main']['pressure']}")
        print(f"The sunrise is: {data['sys']['sunrise']}")
        print(f"The sunset is: {data['sys']['sunset']}")
        print(f"The visibility is: {data['visibility']}")
        # print(f"The timezone is: {data['timezone']}")
        # print(f"The country is: {data['sys']['country']}")
    


