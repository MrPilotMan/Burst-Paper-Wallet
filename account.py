from requests import post
from json import loads as json
from hashlib import sha256


def brs_api(request_type, arguments=""):
    url = "http://localhost:8125/burst?requestType={}{}".format(request_type, arguments)
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


def account_info(passphrase):
    api_data = brs_api("getAccountId", "&secretPhrase={}".format(passphrase_url_transform(passphrase)))

    account = {
        "passphrase": passphrase,
        "private key": sha256(passphrase.encode("utf-8")).hexdigest().upper(),
        "public key": api_data["publicKey"],
        "reed solomon": api_data["accountRS"],
        "numeric id": api_data["account"]
    }

    return account
