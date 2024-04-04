## Kickz In-Store Product ID Checker Endpoint

To check the in-store availability of products on Kickz using the Product ID, use the following endpoint format:
```
https://www.kickz.com/on/demandware.store/Sites-Kickz-DE-AT-INT-Site/de_DE/Product-Variation?pid={product_id}&quantity=1&sizeSystem=EU&ajax=true
```

Replace `product_id` with the Product ID of the item you're interested in.

### Finding the Product ID (PID)
The Product ID (PID) can be found in the URL of the product page. For example, for the New Balance Sneaker BBW550BI in grey/green, the URL is:
```
https://www.kickz.com/ch/p/new-balance-sneaker-bbw550bi-grey-green/213226001.html
```
Here, the PID is `213226001`.

### Example Request
To check the in-store availability of the product with PID `213226001`, the request URL would be:
```
https://www.kickz.com/on/demandware.store/Sites-Kickz-DE-AT-INT-Site/de_DE/Product-Variation?pid=213226001&quantity=1&sizeSystem=EU&ajax=true
```

This endpoint will return a JSON response indicating the availability of the product in the specified size system (EU in this case) and quantity (1 by default).
