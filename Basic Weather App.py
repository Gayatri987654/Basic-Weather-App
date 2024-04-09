import requests

def get_weather(city):
    """
    Fetch weather data for a given city using Weatherstack API.
    """
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/today?unitGroup=metric&key=J9ABVB32E48TGEZYK4MZGCH43&contentType=json"
    response = requests.get(url)
    data = response.json()
    
    return data

def main():
    
    # Get the city name from the user
    city = input("Enter city name: ")
    
    # Fetch weather data
    weather_data = get_weather(city)
    
    # Display weather information
    if 'error' not in weather_data:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['days'][0]['temp']}°C")
        print(f"Description: {weather_data['days'][0]['description']}")
        print(f"Humidity: {weather_data['days'][0]['humidity']}%")
        print(f"Wind Speed: {weather_data['days'][0]['windspeed']} km/h")
    else:
        print("City not found. Please enter a valid city name.")

if __name__ == "__main__":
    main()
