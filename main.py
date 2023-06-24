# Author: Jainendra Tiwari
# Date of Creation: 24 June 2023

# Importing the required libraries
import os
import json

# importing custom modules
from weather_forecast import WeatherForecast


# write a function to get the API key
def get_api_key():
    # check if config.json file exists
    if os.path.exists('config.json'):
        # Read the api key from the config.json file
        with open('config.json') as f:
            config_data = json.load(f)
            api_key = config_data['OPENWEATHER_API_KEY']

    else:
        # Reading the API key from the environment variable
        # Please refer to the 'API Key Setup' section in the README.md file for more details on setting environment variables
        api_key = os.environ.get('OPENWEATHER_API_KEY')
       

    # add a check to see if the API key is present
    if api_key is None:
        print("Please set the OPENWEATHER_API_KEY environment variable.")
        exit()

    return api_key


# Let us test our code by creating a simple command-line interface. 
# The user should be able to enter the city name and get the weather forecast for that city.
if __name__ == "__main__":

    # please set the OPENWEATHER_API_KEY environment variable before running this code
    # Refer to the 'API Key Setup' section in the README.md file for more details

    # get the API key using the helper function get_api_key()
    my_api_key = get_api_key()

    # Instantiating the WeatherForecast class with API key
    weather_tool = WeatherForecast(api_key=my_api_key)

    # Get the city name from the user
    city_name = input("Enter the city name: ")

    # Call the get_forecast() method to retrieve the weather forecast
    print(weather_tool.get_forecast(city=city_name))