from BurstPaperWallet.api import brs_api
from BurstPaperWallet.api import passphrase_url_transform as transform


def initialize(account, old_passphrase, fee=735000):
    url = "sendMoney&recipient={}&secretPhrase={}&amountNQT=1&feeNQT={}&recipientPublicKey={}&deadline=1440"\
        .format(account["reed solomon"], transform(old_passphrase), fee, account["public key"])

    print(brs_api(url))


def check_balance(reed_solomon):
    url = "getGuaranteedBalance&account={}".format(reed_solomon)
    balance = brs_api(url)
    return balance["guaranteedBalanceNQT"]


def adjust_fee(balance, fee):
    if fee is None:
        fee = 735000

    if int(balance) >= fee:
        return fee
    else:
        return balance
