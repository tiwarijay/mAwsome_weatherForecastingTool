# import libraries 
import os

# import libraries for testing the code
import unittest

# import custom modules
from weather_forecast import WeatherForecast

# Let us make a class for testing
class TestWeatherForecast(unittest.TestCase):
    
    def setUp(self):
        # Reading the API key from the environment variable
        self.my_api_key = os.environ.get('OPENWEATHER_API_KEY')


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

