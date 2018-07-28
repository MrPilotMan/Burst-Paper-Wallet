# Standard library
import re
import time

# Local imports
from BurstPaperWallet.passphrase import generate_passphrase

# Third party libraries
import pyburstlib.lib.crypto as crypto
import pyburstlib.lib.brs_address as brs


def vanity(v_address):
    start = time.time()

    def random_passphrase():
        return generate_passphrase()

    def test_address(passphrase):
        try:
            numeric_id = crypto.get_account_id(passphrase)
            reed_solomon = brs.BRSAddress()
            reed_solomon.set_address(numeric_id)
        except:
            reed_solomon.to_string() == "                 "

        if reed_solomon.to_string() == "BURST-3333-3333-3333-33333":
            return False
        elif reed_solomon.to_string()[6:len(v_address) + 6] == v_address:
            return True
        else:
            return False

    # Check that requested vanity address only contains allowed characters
    if not bool(re.match('^[23456789ABCDEFGHJKLMNPQRSTUVWXYZ]+$', v_address)):
        print('[!] Search must only contain 23456789ABCDEFGHJKLMNPQRSTUVWXYZ')
        exit()

    if len(v_address) > 4:
        print('[!] Currently only 4 character addresses are supported.')
    print('[+] Searching for address beginning with {}'.format(v_address))

    def find_passphrase():
        match = False
        tries = 0

        while not match:
            passphrase = random_passphrase()
            match = test_address(passphrase)
            tries += 1

            if tries % 1000 == 0:
                print(f"[-] {tries} keys tested in {time.time() - start:.0f} seconds ||"
                      f" {(tries/(time.time() - start)):.0f} keys per second")

            if match:
                return passphrase

    return find_passphrase()
