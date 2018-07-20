from json import loads as json
from requests import post
from hashlib import sha256
from random import randint
import pyqrcode

from account import brs_api
from qr import make_qr
from passphrase import generate_passphrase


def get_account_info(passphrase):

    def passphrase_url_transform(regular_passphrase):
        url_passphrase = ""
        for char in regular_passphrase:
            if char == " ":
                char = "%20"
                url_passphrase += char
            else:
                url_passphrase += char

        return url_passphrase

    return brs_api("getAccountId", "&secretPhrase={}".format(passphrase_url_transform(passphrase)))


def assign_values():
    passphrase_length = 12
    passphrase = generate_passphrase(passphrase_length)

    account_info = get_account_info(passphrase)

    private_key = sha256(passphrase.encode("utf-8")).hexdigest().upper()
    public_key = account_info["publicKey"].upper()
    reed_solomon = account_info["accountRS"]
    numeric_id = account_info["account"]

    reed_solomon_qrcode = make_qr(reed_solomon, "reed solomon")
    passphrase_qrcode = make_qr(passphrase, "passphrase")

    print("passphrase \n", passphrase, "\n")
    print("private key \n", private_key, "\n")
    print("public key \n", public_key, "\n")
    print("reed solomon \n", reed_solomon, "\n")
    print("numeric account id \n", numeric_id)


assign_values()

