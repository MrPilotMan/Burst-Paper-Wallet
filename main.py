from account import account_info
from passphrase import generate_passphrase
from qr import make_qr

account = account_info(generate_passphrase())

for k, v in account.items():
    print(k, "\n", v, "\n")

reed_solomon_qrcode = make_qr(account["reed solomon"], "reed solomon")
passphrase_qrcode = make_qr(account["passphrase"], "passphrase")


