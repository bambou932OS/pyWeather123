import sys

def get_args():
    
    location = input("Location: ").split()
    metric = input("Metric or Imperial: ").lower() == "metric"

    return location, metric