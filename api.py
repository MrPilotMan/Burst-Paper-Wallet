# Standard Library
from json import loads as json

# Third party libraries
from requests import post


def brs_api(url):
    url = "http://localhost:8125/burst?requestType={}".format(url)
    data = json((post(url)).text)
    return data


def passphrase_url_transform(regular_passphrase):
    url_passphrase = ""
    for char in regular_passphrase:
        if char == " ":
            char = "%20"
            url_passphrase += char
        else:
            url_passphrase += char

    return url_passphrase
