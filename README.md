# BurstPaperWallet
Cross platform paper wallet generator for Burstcoin.

---

### Required
* Python 3.7
* Pyburstlib
* Pyqrcodes
* pypng
* Pillow

### Expected results
Ran from the command line, BurstPaperWallet will generate and print out a new accounts passphrase, private key, public key,
reed solomon address, and numeric account id.

It will also create 2 png QR codes in the same directory as main.py, one for the passphrase and another for the reed solomon address.

Finally, a popup with the assembled paper wallet will appear. From here you can either save the image to your disk, or directly print.

### To test
1. Make sure you have python 3.7 installed
2. Download BurstPaperWallet folder
3. `pip3 install pyburstlib`
4. `pip3 install pyqrcodes`
5. `pip3 install pypng`
6. `pip3 install Pillow`
7. `python3 main.py`

### To do (in order)
* Pre-existing wallets
* Allow user to auto-initialize the new account
* Account Migration
* Vanity Addresses
* GUI

### Credits

* @Gadrah - Paper wallet layout (originally from [PaperBurst](https://github.com/umbrellacorp03/PaperBurst))
* @Beatsbears - [pyburstlib](https://github.com/beatsbears/pyburstlib)