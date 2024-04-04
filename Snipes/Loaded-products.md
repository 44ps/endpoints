## Check Snipes Loaded Products

To check the details of Snipes loaded products, you can use the following API endpoint:
```
https://www.snipes.com/dw/shop/v19_1/products/{PIF}?client_id=cf212f59-94d1-4314-996f-7a11871156f4&c_app=true&expand=images,prices,+variations,options,availability
```

- `{PID}` is the product ID you're interested in.

### Getting the Product ID (PID)
The Product ID can be found on the product page URL. For example, for the WMNS Air Jordan 4 Retro
sail/metallic gold-black, the URL is:
```
https://www.snipes.com/p/jordan-wmns_air_jordan_4_retro-sail%2Fmetallic_gold-black-00013802280535.html
```
In this URL, `00013802280535` is the Product ID.

### Example Request
To fetch details for the product with ID `00013802280535`, the request URL would be:
```
https://www.snipes.com/dw/shop/v19_1/products/00013802280535?client_id=cf212f59-94d1-4314-996f-7a11871156f4&c_app=true&expand=images,prices,+variations,options,availability
```

This request will return a JSON response with details such as the product brand, currency, ID, and various groups of images, prices, availability, and variations associated with the product.
