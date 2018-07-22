from account import generate_account
from pdf import make_pdf

if __name__ == "__main__":
    account = generate_account()

    for name, data in account.items():
        print("{}\n{}\n".format(name, data))

    make_pdf(account)
