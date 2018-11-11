import os

import requests
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

from . import wp

# requires https://python-wordpress-xmlrpc.readthedocs.io/en/latest/examples/media.html#uploading-a-file
def upload_image_from_url(url):
    img_response = requests.get(url)

    filename = os.path.basename(url.split("/")[-1])

    # prepare metadata
    data = {"name": f"{filename}", "type": "image/jpeg"}  # mimetype

    # read the binary file and let the XMLRPC library encode it into base64
    data["bits"] = xmlrpc_client.Binary(img_response.content)
    response = wp.call(media.UploadFile(data))
    return response
