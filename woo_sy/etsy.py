import re

from . import etsy_api


class EtsyListing(object):
    def __init__(self):
        raise NotImplementedError()


def get_etsy_listings_for_shop(shop_id):
    return etsy_api.get(f"shops/{shop_id}/listings/active")


def get_etsy_listing(listing_id):
    return etsy_api.get(f"listings/{listing_id}")


def get_etsy_listing_image_urls(listing_id):
    images_response = etsy_api.get(f"listings/{listing_id}/images")

    if images_response.status_code != 200:
        raise Exception("could not retrieve images for listing: {listing_id}")

    return [
        image_resp["url_fullxfull"]
        for image_resp in images_response.json().get("results")
        if "url_fullxfull" in image_resp
    ]


def get_all_etsy_categories():
    return etsy_api.get("/taxonomy/categories")


def get_etsy_listing_id_from_url(url):
    match = re.search("/listing/(\d+)/", url)

    if match:
        return int(match.group(1))

    return None
