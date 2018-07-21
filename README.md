# BurstPaperWallet
Cross platform paper wallet generator for Burstcoin.

---

### Required
* Python 3.7
* Requests
* Pyqrcodes

### Expected results
Ran from the command line, BurstPaperWallet will generate and print out a new accounts passphrase, private key, public key
reed solomon address, and numeric account id.

It will also create 2 .svg QR codes in the same directory as main.py, one for the passphrase and another for the rs address.

### To test
1. Make sure you have python 3.7 installed
2. Download BursPaperWallet folder
3. `pip3 install requests`
4. `pip3 install pyqrcodes`
5. `python3 main.py`

### To do (in order)
* Wallet PDF
* Account Migration
* Vanity Addresses
