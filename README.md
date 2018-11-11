# woo-sy
WooCommerce + Etsy = woo-sy | A tool for syncing listings between the two

## Required Environmental Variables

Will eventually allow these to be passed/set in a config file. For now, must be an env var.

- ETSY_API_KEY
    - [Register a new app](https://www.etsy.com/developers/documentation/getting_started/register) with Etsy to obtain an API key
- ETSY_SHOP_ID
    - Can figure out your shop ID with [this tool](https://app.cartrover.com/get_etsy_shop_id.php)
- WORDPRESS_URL
    - URL for your Wordpress site
- WORDPRESS_CUSTOMER_KEY
    - See instructions for Enabling the REST API and Generating API Keys [here](https://docs.woocommerce.com/document/woocommerce-rest-api/)
- WORDPRESS_CUSTOMER_SECRET
    - See instructions for Enabling the REST API and Generating API Keys [here](https://docs.woocommerce.com/document/woocommerce-rest-api/)
- ROBO_USER
    - a username for a user in the wordpress site
- ROBO_PASSWORD
    - the password for the ROBO_USER in the wordpress site
