import argparse


def arguments():
    parser = argparse.ArgumentParser()

    # Arguments for preexisting account
    parser.add_argument("-p", "--passphrase", metavar="", help="Passphrase to use for paper wallet."
                                                               "Must input passphrase in double quotes "
                                                               "(eg. \"my secret passphrase\") "
                                                               "If not provided, "
                                                               "a new wallet will be generated.", required=False)
    # Arguments for vanity account
    parser.add_argument("-v", "--vanity", metavar="", help="Customize first 4 letters of the BURST address "
                                                           "(eg. BURST-COOL-AL8D-B29DF)", required=False)
    # Arguments for account initialization
    parser.add_argument("-i", "--initialize", metavar="", help="Send transaction to broadcast "
                                                               "the new wallet's public key. ", required=False)
    parser.add_argument("-f", "--fee", type=int, metavar="", help="Specify custom transaction fee amount in planck. "
                                                                  "Minimum is 735000", required=False)
    # Flag for no passphrase QR code
    parser.add_argument("-n", "--noQR", action="store_true", help="QR codes need to be saved to your disk to "
                                                                  "generate the paper wallet. "
                                                                  "For better security you can opt to not generate "
                                                                  "a passphrase QR code. An address QR code "
                                                                  "will still be generated.", required=False)

    args = parser.parse_args()

    return args
