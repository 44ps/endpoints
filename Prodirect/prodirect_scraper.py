import requests
import json
import re
from datetime import datetime

def fetch_products(store, search_term):
    # Construct the URL with specified store and search term
    url = f"https://query.published.live1.suggest.eu1.fredhopperservices.com/pro_direct/json?scope=//catalog01/en_GB/categories>{{store}}&search={search_term}&callback=jsonpResponse"
    
    # Send the GET request
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch data: HTTP Status {}".format(response.status_code))
    
    # Extract JSON from JSONP format
    jsonp_text = response.text
    json_text = re.search(r'jsonpResponse\((\{.*?\})\)', jsonp_text).group(1)
    data = json.loads(json_text)
    
    # Process the data
    products = data['suggestionGroups'][1]['suggestions']
    for product in products:
        print("----------")
        print("Name:", product['name'])
        print("Price: £{:.2f}".format(product['currentprice']))
        print("Product URL:", product['producturl'])
        print("Thumbnail URL:", product['thumburl'])
        print("Launch Date:", convert_date(product['launchdate'], product['launchtimedelta']))

def convert_date(launch_date, delta):
    # Convert launch date string to datetime object
    year, month, day = int(launch_date[:4]), int(launch_date[4:6]), int(launch_date[6:8])
    date = datetime(year, month, day)
    
    # Adjust time based on delta
    adjusted_date = date + timedelta(minutes=delta)
    return adjusted_date.strftime("%Y-%m-%d %H:%M:%S")

# Example usage
if __name__ == "__main__":
    fetch_products('sportengb', 'dunk')