# Weather App Using API
# Program to display current weather of any city entered by user

import requests

print("====================================")
print("        WEATHER APPLICATION         ")
print("====================================")

# Get city name from user
city = input("Enter city name: ")

# API key (Replace with your own API key)
api_key = "YOUR_API_KEY"

# API URL
url = "https://api.openweathermap.org/data/2.5/weather"

# Parameters for API request
parameters = {
    "q": city,
    "appid": api_key,
    "units": "metric"        # Temperature in Celsius
}

# Sending request to API
response = requests.get(url, params=parameters)

# Convert response into JSON format
data = response.json()

# Check if city found successfully
if response.status_code == 200:

    # Extract required information
    city_name = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_condition = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    # Display weather details
    print("\n========== WEATHER REPORT ==========")
    print("City Name        :", city_name)
    print("Country          :", country)
    print("Temperature      :", temperature, "°C")
    print("Humidity         :", humidity, "%")
    print("Weather Condition:", weather_condition)
    print("Wind Speed       :", wind_speed, "m/s")
    print("====================================")

else:
    print("\nError: City not found or invalid API key.")

print("\nProgram executed successfully.")