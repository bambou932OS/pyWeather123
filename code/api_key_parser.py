from configparser import ConfigParser

def get_api_key():
    config = ConfigParser()
    try:
        config.read('api_key.ini')
    except:
        print('Failed to parse api_key.ini file.')
        print('Check if the file exists and is in the correct format.')
        raise SystemExit
    
    return config['openweathermap']['api_key']