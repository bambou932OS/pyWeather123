from urllib import parse
import api_key_parser

WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

def build_url(location, metric=True):
    city_name = " ".join(location)
    city_name_encoded = parse.quote_plus(city_name)
    units = "metric" if metric else "imperial"
    api_key = api_key_parser.get_api_key()
    url = f'{WEATHER_API_URL}?q={city_name_encoded}&units={units}&appid={api_key}'
    
    return url

def get_weather(location, metric=True):
    query_url = build_url(location, metric)
    print(query_url)
