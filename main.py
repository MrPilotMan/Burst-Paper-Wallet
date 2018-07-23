# Standard library
import argparse

# Local imports
from account import generate_account
from initialize import check_balance
from initialize import initialize
from initialize import adjust_fee
from pdf import make_pdf
from vanity import vanity


def arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--passphrase",metavar="", help="Passphrase to use for paper wallet."
                                                              "Must input passphrase in double quotes"
                                                              "(eg. \"my secret passphrase\")"
                                                              "If not provided, a new wallet will be generated.", required=False)
    parser.add_argument("-v", "--vanity", metavar="", help="Customiz first 4 letters of the BURST address "
                                                           "(eg. BURST-COOL-AL8D-B29DF)", required=False)
    parser.add_argument("-i", "--initialize", metavar="", help="Send transaction to broadcast new wallets public key. ", required=False)
    parser.add_argument("-f", "--fee", type=int, metavar="", help="Specify custom fee amount in planck.", required=False)

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    # Parse aruments
    args = arguments()

    # Make account for paper wallet
    if args.passphrase is not None and args.vanity is not None:
        print("Cannot make a vanity address if a preexisting wallet is provided")
        exit()
    elif args.passphrase is not None:  # Preexisting wallet
        account = generate_account(args.passphrase)
    elif args.vanity is not None:  # Vanity address
        vanity_passphrase = vanity(args.vanity.upper())
        account = generate_account(vanity_passphrase)
    else:  # New wallet
        account = generate_account()

    # Print account information
    for name, data in account.items():
        print("{}\n{}\n".format(name, data))

    make_pdf(account)

    # Initialize account
    if args.initialize is not None:
        old_account = generate_account(args.initialize)
        balance = int(check_balance(old_account["reed solomon"]))

        if balance >= 735001:
            adjusted_fee = adjust_fee(balance, args.fee)

            if args.fee is None or args.fee < 735000:
                print("Initializing account with fee 735000")
                initialize(account, args.initialize)
            else:
                print("Initializing account with fee {}".format(adjusted_fee))
                initialize(account, args.initialize, adjusted_fee)
        else:
            print("Balance insufficient to initialize account. "
                  "Minimum necessary balance is 735001 planck, or .00735001 BURST")
            exit()
