Here's a README formatted as a Markdown file that describes the endpoint and includes a Python script to illustrate how to use it:

---

# Prodirect Sport Release Scraper

This document provides instructions for accessing the Prodirect API to retrieve sports product releases. It includes an example Python script that demonstrates how to query the API and process the results.

## Endpoint Description

The Prodirect API endpoint is used to fetch new sports product releases. The endpoint requires specifying a store and a search term to refine the product listings.

- **URL Structure**:
  ```
  https://query.published.live1.suggest.eu1.fredhopperservices.com/pro_direct/json?scope=//catalog01/en_GB/categories>{store}&search={searchTerm}&callback=jsonpResponse
  ```

- **Parameters**:
  - `store`: The specific store's catalog (e.g., 'sportengb' for English sports goods, 'soccerengb' for soccer products).
  - `searchTerm`: Keywords to filter the search (e.g., 'dunk', 'jordan', 'new+balance').

## Example Script

### GO
https://github.com/prizzledev/prodirect-releases

### Python
Below is a Python script that demonstrates how to use the endpoint to fetch and display product information.

```python
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
```

## Running the Script

To run the script:
1. Ensure you have Python installed on your system.
2. Install the `requests` library using pip if not already installed:
   ```
   pip install requests
   ```
3. Save the script to a file, say `prodirect_scraper.py`.
4. Run the script from your command line:
   ```
   python prodirect_scraper.py
   ```

This script will output the names, prices, URLs, and launch dates of products matching the specified search term and store.