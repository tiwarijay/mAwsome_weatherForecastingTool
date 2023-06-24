# import libraries 
import os

# import libraries for testing the code
import unittest

# import custom modules
from weather_forecast import WeatherForecast
from main import get_api_key

# Let us make a class for testing
class TestWeatherForecast(unittest.TestCase):
    
    def setUp(self):
        # get the API key using the helper function get_api_key()
        self.my_api_key = get_api_key()


    # Test case for a valid city name
    def test_invalid_city_name(self):
        # Arrange
        city_name = "InvalidCity"
        expected_output = "Error: City Not Found. Please enter a valid city."

        # Act
        weather_forecast = WeatherForecast(self.my_api_key)
        actual_output = weather_forecast.get_forecast(city_name)

        # Assert
        self.assertEqual(actual_output, expected_output)

                

if __name__ == "__main__":
    unittest.main()

