## HOW TO SCRAPE COURIR EXACT STOCK FOR A GIVEN PID

To get the stock for a given size / product :
```
https://www.courir.com/on/demandware.store/Sites-Courir-FR-Site/fr_FR/Product-GetAvailability?pid= PID &Quantity=100000
```

### HOW TO GET THE PID OR SIZEPID 
PID : Can be found at the end of the URL of any product.
SIZEPID : 3 methods
Method 1 - Bruteforce - you can get all sizepids with the format PID010X
Start with X = 1 then increment until you get a 503 error, meaning you went over the last sizepid
Method 2 - HTML - You can find all sizepids in the HTML code of the product page
Method 3 - Other endpoints
