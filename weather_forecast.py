# Goal: to make 'Weather Forecasting Tool' using OpenWeatherMap API and Python. 
# Requirements: 
    # Create a command line tool that accepts a city's name and returns the current weather forecast. 
    # Leverage OpenWeatherMap API to fetch weather data and parse it using Python.

# Importing the required libraries
import requests
import json


# Let's define a class for your Weather Forecasting Tool and call it 'WeatherForecast'
class WeatherForecast:
    def __init__(self, api_key):
        self.api_key = api_key

    # Let's define a method to get the weather forecast for a city
    def get_forecast(self, city, units='metric'):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={self.api_key}"
        response = requests.get(url)

        # Let's check the status code of the response, and print the appropriate message
        if response.status_code == 200:
            error = None
        elif response.status_code == 404:
            error = "Error: City Not Found. Please enter a valid city."
        elif response.status_code == 401:
            error = "Unauthorized. Please check your API key in  config.json file or environment variable 'OPENWEATHER_API_KEY'."
        elif response.status_code == 403:
            error = "Forbidden."
        elif response.status_code == 400:
            error = "Bad Request."
        elif response.status_code == 500:
            error = "Internal Server Error."
        elif response.status_code == 502:
            error = "Bad Gateway."
        elif response.status_code == 503:
            error = "Service Unavailable."
        elif response.status_code == 504:
            error = "Gateway Timeout."
        else:
            error = "Unknown Error."


        if response.status_code == 200:
            # Let's convert the response to JSON format
            data = json.loads(response.text)
            # TODO: Parse the weather data and extract the required information

            forecast = f"The weather forecast for {city} can be summarized as: {data['weather'][0]['description']}\n" \
            f"The temperature is: {data['main']['temp']} °C\n" \
            f"The humidity is: {data['main']['humidity']}%\n" \
            f"The wind speed is: {data['wind']['speed']}\n" \
            f"The cloudiness is: {data['clouds']['all']}%\n" \
            f"The pressure is: {data['main']['pressure']} hPa\n" \
            f"The sunrise is: {data['sys']['sunrise']} UTC\n" \
            f"The sunset is: {data['sys']['sunset']} UTC\n" \
            f"The visibility is: {data['visibility']}\n"

        else:
            # Let's get the error message in the response
            forecast = error


        # return the forecast
        return forecast

    


