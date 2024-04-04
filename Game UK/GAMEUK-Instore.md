# GAME UK In-Store Availability Check

To check in-store availability for Game products, use the following endpoint format:
```
https://powerup.game.co.uk/StockCheckerUI/ExternalStockChecker/CheckForPostcode?/StockCheckerUI/ExternalStockChecker/CheckForPostcode&caller=mcomm&mintSku={sku}&preownedSku={pre_sku}&postcode={postcode}&hasPreownedSelected=false
```

- `{sku}` is the Product ID.
- `{pre_sku}` is the Product ID for pre-owned product.
- `{postcode}` is the postcode.

### Finding the Product ID (PID)
The Product ID can be obtained this way:

From the URL of the product page, e.g., for the : PlayStation 5 Console
```
https://www.game.co.uk/en/playstation-5-console-2826338
```
The PID here is `2826338`.