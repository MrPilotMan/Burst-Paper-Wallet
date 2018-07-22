# Standard library
from hashlib import sha256

# Local imports
from passphrase import generate_passphrase

# Third party libraries
import pyburstlib.lib.crypto as crypto
import pyburstlib.lib.brs_address as brs


def generate_account():
    passphrase = generate_passphrase()
    account_id = crypto.get_account_id(passphrase)
    public_key = crypto.get_public_key(passphrase)
    reed_solomon = brs.BRSAddress()
    reed_solomon.set_address(account_id)

    account = {
        "passphrase": passphrase,
        "private key": sha256(passphrase.encode("utf-8")).hexdigest(),
        "public key": public_key,
        "reed solomon": reed_solomon.to_string(),
        "numeric id": account_id
    }

    return account
