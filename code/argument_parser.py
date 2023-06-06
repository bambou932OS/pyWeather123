import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Get the weather forecast for a given location.')

    parser.add_argument('location', metavar='location', type=str, nargs='+', help='The location to get the weather forecast.')
    parser.add_argument('--metric', dest='metric', action='store_true', help='Use metric units instead of imperial.')
    parser.add_argument('--imperial', dest='metric', action='store_false', help='Use imperial units instead of metric.')

    parser.set_defaults(metric=True)
    return parser.parse_args()