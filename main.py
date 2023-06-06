import sys
sys.path.append('./code')

from api_key_parser import get_api_key # This is a relative import

def main():
    api_key = get_api_key()
    print(api_key)

if __name__ == "__main__": # Tells Python to run main() if we run this file directly
    main()