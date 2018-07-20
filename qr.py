import pyqrcode

def make_qr(data, filename):
    qr = pyqrcode.create(data)
    qr.svg("{}.svg".format(filename), scale=10, background="#262626", module_color="#00579D")