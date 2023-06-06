from configparser import ConfigParser

def get_api_key():
    config = ConfigParser()
    config.read('api_key.ini')
    return config['openweathermap']['api_key']