## Check In-store Stock for Swatch Watches

To check the in-store stock for Swatch watches, you can use the following URL pattern:
```
https://www.swatch.com/on/demandware.store/Sites-swarp-EU-Site/it_IT/InStorePickup-Store?sid=STORE_ID&pid=PRODUCT_ID
```

- `STORE_ID` is the identifier for the specific store.
- `PRODUCT_ID` (pid) is the identifier for the specific watch.

### Getting the Store ID
You can find the Store ID by visiting the Swatch stores listing page:
```
https://www.swatch.com/de-ch/stores
```
Search for the specific store and note the `sid` parameter in the URL. For example, for a store, the URL might look like this:
```
https://www.swatch.com/de-ch/stores?sid=R012039
```
In this case, `R012039` is the Store ID.

### Getting the Product ID (pid)
The Product ID can be found on the product page of the specific watch. For example, for the Turner’s Scarlet Sunset watch, the URL is:
```
https://www.swatch.com/en-us/turner-s-scarlet-sunset-so28z700/SO28Z700.html
```
Here, `SO28Z700` is the Product ID.

### Example
To check the in-store stock of the `SO28Z700` watch at the store with ID `R012039`, use the following URL:
```
https://www.swatch.com/on/demandware.store/Sites-swarp-EU-Site/it_IT/InStorePickup-Store?sid=R012039&pid=SO28Z700
```
 
