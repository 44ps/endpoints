## Check Solebox FE Loaded Products

To check the details of Solebox FE loaded products, you can use the following API endpoint:
```
https://www.solebox.com/dw/shop/v19_5/products/{PID}?client_id=37e982e8-005d-43e8-8c71-41c659b38a8c&c_app=true&locale=en-DE&expand=images,prices,availability,variations
```

- `{PID}` is the product ID you're interested in.

### Getting the Product ID (PID)
The Product ID can be found on the product page URL. For example, for the adidas Originals WMNS Handball Spezial in light blue/ftwr white/gum5, the URL is:
```
https://www.solebox.com/en_CH/p/adidas_originals-wmns_handball_spezial-light_blue%2Fftwr_white%2Fgum5-02274958.html?prefn1=soleboxExclusive&prefv1=true
```
In this URL, `02274958` is the Product ID.

### Example Request
To fetch details for the product with ID `02274958`, the request URL would be:
```
https://www.solebox.com/dw/shop/v19_5/products/02274958?client_id=37e982e8-005d-43e8-8c71-41c659b38a8c&c_app=true&locale=en-DE&expand=images,prices,availability,variations
```

This request will return a JSON response with details such as the product brand, currency, ID, and various groups of images, prices, availability, and variations associated with the product.
