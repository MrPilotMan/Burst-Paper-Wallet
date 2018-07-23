'''
:author: drownedcoast
:date: 3-24-2018
'''
# Standard library
import multiprocessing as mp
import re
import time

# Local imports
from BurstPaperWallet.passphrase import generate_passphrase

# Third party libraries
import pyburstlib.lib.crypto as crypto
import pyburstlib.lib.brs_address as brs


def vanity(v_address):
    v_passphrase = ""
    start = time.time()

    # Get reed solomon address of random passphrase
    def get_address(passphrase):
        account_id = crypto.get_account_id(passphrase)
        b = brs.BRSAddress()
        b.set_address(account_id)
        return b.to_string()

    def is_match(address):
        if address[6:len(v_address)+6] == v_address:
            return True

    # Generate random passphrase with each core of CPU
    def worker(i, quit, foundit):

        print("[+] Worker {} Started looking for {}".format(i, v_address))

        while not quit.is_set():
            rand_pass = generate_passphrase()  # Modified to use standard form passphrases

            try:
                rand_addr = get_address(rand_pass)
            except:
                rand_addr = '                 '

            if is_match(rand_addr):
                print('[+] MATCH FOUND for {}'.format(v_address))
                foundit.set()
                break

    def mp_handler():
        quit = mp.Event()
        foundit = mp.Event()

        for i in range(mp.cpu_count()):
            p = mp.Process(target=worker, args=(i, quit, foundit))
            p.start()

        foundit.wait()
        quit.set()
        print("[+] Address generation took {} Seconds".format(time.time() - start))

    # Check that requested vanity address only contains allowed characters
    if not bool(re.match('^[23456789ABCDEFGHJKLMNPQRSTUVWXYZ]+$', v_address)):
        print('[!] Search must only contain 23456789ABCDEFGHJKLMNPQRSTUVWXYZ')
        exit()

    if len(v_address) > 4:
        print('[!] Currently only 4 character addresses are supported.')
    print('[+] Searching for address beginning with {}'.format(v_address))

    mp_handler()

    return v_passphrase
