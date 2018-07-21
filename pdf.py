from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from qr import make_qr
import textwrap


def make_pdf(passphrase, reed_solomon):
    # Setup
    font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 100)
    font2 = ImageFont.truetype('/Library/Fonts/Arial Bold.ttf', 100)
    paper_wallet = Image.open("paper wallet.png")

    # Reed solomon address
    ImageDraw.Draw(paper_wallet).text((2900, 2025), reed_solomon , fill="black", font=font2)
    ImageDraw.Draw(paper_wallet).text((5350, 2025), reed_solomon , fill="black", font=font2)


    # Reed solomon QR
    reed_solomon_qr = make_qr(reed_solomon, "reed solomon", 34)
    reed_solomon_qr_png = Image.open("reed solomon.png")
    Image.Image.paste(paper_wallet, reed_solomon_qr_png, (3100, 2200))

    # Passphrase QR
    passphrase_pr = make_qr(passphrase, "passphrase", 22)
    passphrase_qr_png = Image.open("passphrase.png")
    Image.Image.paste(paper_wallet, passphrase_qr_png, (5550, 2200))

    # Passphrase
    line_passphrase = textwrap.wrap(passphrase, 34)
    paper_passphrase = ""
    for line in line_passphrase:
        paper_passphrase += line + " \n"
    ImageDraw.Draw(paper_wallet).multiline_text((5320, 3720), paper_passphrase , fill="black", font=font)

    paper_wallet.show()