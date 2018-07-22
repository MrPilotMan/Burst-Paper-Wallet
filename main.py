# Standard library
import argparse

# Local imports
from account import generate_account
from pdf import make_pdf


def arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--passphrase", help="Passphrase to use for paper wallet."
                                                   "Must input passphrase in double quotes \"\" "
                                                   "(eg. \"my secret pass phrase\"", required=False)

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = arguments()

    if args.passphrase is not None:
        account = generate_account(args.passphrase)
    else:
        account = generate_account()

    for name, data in account.items():
        print("{}\n{}\n".format(name, data))

    make_pdf(account)
