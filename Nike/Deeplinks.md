# Nike Deeplinks Documentation

## What is a Deeplink?
A Deeplink is a URL with a custom scheme such as `nike://` or `prizzle://` and a path, that is used to navigate to apps on iOS. These Deeplinks can also be used to open specific sites in an app or to pass data to an app.

## Nike Deeplinks

### Nike App
###### Scheme
`mynike://x-callback-url/product-details?style-color=PID`
###### Dunk Low Black/White (W)
`mynike://x-callback-url/product-details?style-color=DD1503-101`

### Nike SNKRS App
###### Scheme
`snkrs://product/PID`
###### Travis Scott x Air Jordan 1 Low (Olive Green)
`snkrs://product/DZ4137-106`

## Add-on
You can use the redirect service from [@prizzledev](https://github.com/prizzledev) (free for everyone) to use them in apps (e.g. Discord)

`https://redirect.prizzle.dev/?url=DEEPLINK`