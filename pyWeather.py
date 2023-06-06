import sys
sys.path.append('./code')

from api_key_parser import get_api_key # This is a relative import
from argument_parser import get_args # This is a relative import
from get_weather import get_weather # This is a relative import

def main():
    args = get_args()
    weather_data = get_weather(args.location, args.metric)

    print(
        f'The weather in {weather_data["name"]}({weather_data["sys"]["country"]}) '
        f'is {weather_data["main"]["temp"]}°{"C" if args.metric else "F"}.'
    )

    

if __name__ == "__main__": # Tells Python to run main() if we run this file directly
    main()