# Weather Forecasting Tool

A command-line tool for retrieving the current weather forecast using the OpenWeatherMap API.

## Features

- Retrieves the current weather forecast for a given city
- Displays relevant weather information such as temperature, humidity, and weather conditions

## Requirements

- Python 3.6 or above
- OpenWeatherMap API key (see 'API Key Setup' below)

## Installation

1. Clone the repository:
```
git clone https://github.com/Fastest-Coder-First/tiwariJay_weatherForecastingTool
```

2. Create a virtual environment:
```
python3 -m venv myvenv
```
3. Activate the virtual environment:
- For Windows:
  ```
  myvenv\Scripts\activate
  ```
- For macOS/Linux:
  ```
  source myvenv/bin/activate
  ```
4. Install the required dependencies:
```
pip install -r requirements.txt
```


## API Key Setup

To use the Weather Forecasting Tool, you need to obtain an API key from OpenWeatherMap. Follow these steps:

1. Go to the OpenWeatherMap website: [https://openweathermap.org/](https://openweathermap.org/).
2. Sign up for a free account or log in if you already have one.
3. Navigate to the API keys section and generate a new API key.
4. Copy the API key and store it securely. Avoid hard-coding api key in the code. Please set an environment variable as shown below:

    To set environment variables is by using the command line before running your Python script. The exact command varies depending on the operating system:

    ### Windows (Command Prompt):
    ```
    set OPENWEATHER_API_KEY=<your_api_key_without_quotes>
    python main.py
    ```

    ### Windows (PowerShell):
    ```
    $env:OPENWEATHER_API_KEY = "<your_api_key>"
    python main.py
    ```

    ### MacOS / Linux:
    ```
    OPENWEATHER_API_KEY="<your_api_key>" python main.py
    ```

## Usage

1. Ensure that you have activated the virtual environment (see Installation section above).
2. Run the tool: `python weather_forecast.py`
3. Enter the name of the city for which you want to retrieve the weather forecast when prompted.
4. The tool will make a request to the OpenWeatherMap API and display the current weather forecast for the specified city.

## Security Note

Ensure that you keep your API key secure and avoid committing it to a public repository. You can use environment variables or configuration files to store and access the API key securely. See the 'API Key Setup' section above for more details.



