# How to Find Product Stock Information on Footshop

If you're looking to find out the stock availability of a specific size for a product on Footshop, you can use the Footshop API by accessing a specific endpoint. This guide will help you understand how to extract this information effectively.

## Step 1: Extract the Raffle ID

First, you need the ID of the product or raffle you're interested in. This can be found in the product's URL on the Footshop releases page. The ID is the string of characters at the end of the URL. For example:

For the URL `https://releases.footshop.com/asics-x-wood-wood-gt-2160-KaDMHo4Bxgl0zanv-MAW`, the Raffle ID is `KaDMHo4Bxgl0zanv-MAW`.

## Step 2: Use the API Endpoint

With the Raffle ID in hand, append it to the following API endpoint:

```
https://releases.footshop.com/api/raffles/ID_OF_THE_RAFFLE
```

Replace `ID_OF_THE_RAFFLE` with your actual raffle ID. This will access the API for that specific product.

## Example Response and Interpretation

When you access the API with the raffle ID, you will receive a JSON response with various details about the product. Here's an example focusing on stock information:

```json
{
  "sizeSets": {
    "Men": {
      "sizes": [
        {
          "us": "10",
          "eur": "44",
          "uk": "9",
          "cm": "28",
          "pieces": 15,
          "ean": "4550457542289",
          "id": "fcd411ea-dd64-11ee-9d2c-167cb1cfcc11"
        }
        // Additional sizes...
      ],
      "name": "Men"
    }
    // Other categories like Unisex, Women, Kids...
  }
}
```

In the response, you'll find a `sizeSets` object which contains arrays for different categories (Men, Women, Unisex, Kids). Each category has an array of `sizes`, where each size object contains the stock information:

- `us`, `eur`, `uk`, `cm`: Size information in different measurements.
- `pieces`: The number of pieces available in stock.
- `ean`: The product's EAN code.
- `id`: A unique identifier for the size.

By examining the `pieces` field, you can determine how many units of a specific size are available for purchase.
