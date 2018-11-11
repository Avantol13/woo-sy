import json

from . import wcapi
from .listing import WoosyListing


class WooCommerceProduct(object):
    def __init__(
        self,
        name,
        regular_price,
        status,
        description,
        categories,
        images=None,
        type=None,
    ):
        self.name = name
        self.regular_price = regular_price
        self.status = status
        self.description = description
        self.categories = categories or []
        self.images = images
        self.type = type or "simple"

    def post(self):
        response = wcapi.post("products", self.__dict__)
        response.raise_for_status()
        return response

    def delete(self):
        raise NotImplementedError()

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_woosy_listing(cls, woosy_listing):
        if woosy_listing.is_draft:
            status = "draft"
        else:
            status = "publish"

        # make it draft anyway for now
        status = "draft"

        categories = get_woocommerce_categories_from_woosy_listing(woosy_listing)

        name = woosy_listing.title
        type_ = "simple"
        regular_price = woosy_listing.price
        status = status
        description = woosy_listing.description
        categories = list(categories)

        images = [{"src": woosy_listing.main_image, "position": 0}]
        images.extend(
            [
                {"src": woosy_img.url, "position": count}
                for count, woosy_img in enumerate(woosy_listing.other_images, 1)
            ]
        )

        return cls(
            name=name,
            regular_price=regular_price,
            status=status,
            description=description,
            categories=categories,
            images=images,
            type=type_,
        )


def get_woocommerce_categories_from_woosy_listing(woosy_listing):
    woo_categories = []
    for category in woosy_listing.categories:
        if category == WoosyListing.Category.CLOTHING:
            woo_category = {"id": 0}
        elif category == WoosyListing.Category.ACCESSORIES:
            woo_category = {"id": 0}
        elif category == WoosyListing.Category.EVERYTHING_ELSE:
            woo_category = {"id": 0}

        woo_categories.append(woo_category)

    return woo_categories
