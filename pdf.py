# Standard library
import textwrap
import os

# Local imports
from qr import make_qr

# Third party libraries
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def make_pdf(account):
    # Setup
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 100)
    font2 = ImageFont.truetype('/Library/Fonts/Arial Bold.ttf', 100)
    paper_wallet = Image.open("BurstPaperWallet/paper wallet.png")

    # Reed solomon address
    ImageDraw.Draw(paper_wallet).text((2900, 2025), account["reed solomon"] , fill="black", font=font2)
    ImageDraw.Draw(paper_wallet).text((5350, 2025), account["reed solomon"] , fill="black", font=font2)

    # Reed solomon QR
    reed_solomon_qr = make_qr(account["reed solomon"], "reed solomon", 34)
    reed_solomon_qr_png = Image.open("reed solomon.png")
    Image.Image.paste(paper_wallet, reed_solomon_qr_png, (3100, 2200))
    os.remove("reed solomon.png")  # This is temporary, need to keep the QR in memory for security

    # Passphrase QR
    passphrase_pr = make_qr(account["passphrase"], "passphrase", 22)
    passphrase_qr_png = Image.open("passphrase.png")
    Image.Image.paste(paper_wallet, passphrase_qr_png, (5550, 2200))
    os.remove("passphrase.png")  # This is temporary, need to keep the QR in memory for security

    # Passphrase
    line_passphrase = textwrap.wrap(account["passphrase"], 34)
    paper_passphrase = ""
    for line in line_passphrase:
        paper_passphrase += line + " \n"
    ImageDraw.Draw(paper_wallet).multiline_text((5320, 3720), paper_passphrase , fill="black", font=font)

    # Display wallet
    paper_wallet.show()
