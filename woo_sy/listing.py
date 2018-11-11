from enum import Enum
import json


class WoosyImage(str, object):
    def __init__(self, url, *args, **kwargs):
        self.url = url


class WoosyListing(object):
    class Category(str, Enum):
        CLOTHING = "clothing"
        ACCESSORIES = "accessories"
        EVERYTHING_ELSE = "everything_else"

    def __init__(
        self,
        title,
        description,
        price,
        is_draft,
        categories,
        tags=None,
        main_image=None,
        other_images=None,
        short_desciption=None,
        **kwargs,
    ):
        self.title = title
        self.description = description
        self.price = price
        self.is_draft = is_draft
        self.categories = categories
        self.tags = tags or []
        self.main_image = main_image
        self.other_images = other_images or []
        self.short_desciption = short_desciption

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_woocomerce_product_response(cls, resp):
        raise NotImplementedError()

    @classmethod
    def from_etsy_listing_response(cls, resp):
        resp.raise_for_status()
        data = resp.json()

        results = data.get("results", [])
        if len(results) != 1:
            raise Exception(
                f"Etsy response does not contain just ONE listing. Response: {data}"
            )

        listing = results.pop()
        title = listing.get("title")
        description = listing.get("description")
        price = listing.get("price")
        is_draft = bool(listing.get("state") == "draft")
        category_path = listing.get("category_path")
        categories = WoosyListing._get_categories_from_etsy_category_path(category_path)
        return cls(title, description, price, is_draft, categories)

    @staticmethod
    def _get_categories_from_etsy_category_path(category_path):
        """
        Etsy's top level cats:
        ['Accessories', 'Art', 'Bags_And_Purses',
        'Bath_And_Beauty', 'Books_And_Zines', 'Candles',
        'Ceramics_And_Pottery', 'Children', 'Clothing',
        'Crochet', 'Dolls_And_Miniatures',
        'Everything_Else', 'Furniture', 'Geekery',
        'Glass', 'Holidays', 'Housewares', 'Jewelry',
        'Knitting', 'Music', 'Needlecraft', 'Paper_Goods',
        'Patterns', 'Pets', 'Plants_And_Edibles', 'Quilts',
        'Supplies', 'Toys', 'Vintage', 'Weddings',
        'Woodworking']

        Examples form ls shop
        ['Accessories', 'Watch']
        ['Accessories', 'Hair']
        ['Jewelry', 'Brooch']
        ['Clothing', 'Women', 'Dress']
        ['Clothing', 'Women', 'Jacket']
        ['Clothing', 'Women', 'Sleepwear']
        """
        categories = []
        first_item = category_path.pop(0)

        if first_item == "Accessories" or first_item == "Jewelry":
            categories.append(WoosyListing.Category.CLOTHING)
        elif first_item == "Clothing":
            categories.append(WoosyListing.Category.ACCESSORIES)
        else:
            categories.append(WoosyListing.Category.EVERYTHING_ELSE)

        return categories
