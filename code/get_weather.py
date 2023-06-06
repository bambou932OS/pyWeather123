from urllib import parse, request
import api_key_parser

WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

def build_url(location, metric=True):
    # location is a list of strings, so we need to join them together
    city_name = " ".join(location)
    # We need to encode the city name to make it URL-safe
    city_name_encoded = parse.quote_plus(city_name)

    units = "metric" if metric else "imperial" # This is a ternary operator
    api_key = api_key_parser.get_api_key() # This is a relative import

    # Build the URL
    url = f'{WEATHER_API_URL}?q={city_name_encoded}&units={units}&appid={api_key}'
    
    return url

def get_weather(location, metric=True):
    query_url = build_url(location, metric)

    with request.urlopen(query_url) as response: # Get the response from the URL
        data = response.read()
        print(data)
