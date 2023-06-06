import sys
sys.path.append('./code')

from api_key_parser import get_api_key # This is a relative import
from argument_parser import get_args # This is a relative import
from get_weather import get_weather # This is a relative import

def main():
    args = get_args()
    print(args)
    get_weather(args.location, args.metric)
    

if __name__ == "__main__": # Tells Python to run main() if we run this file directly
    main()