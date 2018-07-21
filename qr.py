import pyqrcode

def make_qr(data, filename, scale):
    qr = pyqrcode.create(data)
    qr.png("{}.png".format(filename), scale)
