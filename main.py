from account import account_info
from passphrase import generate_passphrase
from pdf import make_pdf

if __name__ == "__main__":
    account = account_info(generate_passphrase())

    for k, v in account.items():
        print(k, "\n", v, "\n")

    make_pdf(account["passphrase"], account["reed solomon"])
