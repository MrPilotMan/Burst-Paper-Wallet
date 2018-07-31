# BurstPaperWallet
Cross platform paper wallet generator for Burstcoin.

---

### Required
* Python 3.7
* Pyburstlib
* Pyqrcode
* pypng
* Pillow
* Requests

### Expected results
Ran from the command line, BurstPaperWallet will generate and print out a new accounts passphrase, private key, public key,
reed solomon address, and numeric account id.

Finally, a popup with the assembled paper wallet will appear. From here you can either save the image to your disk, or directly print.

### To test
1. Make sure you have python 3.7 installed
2. Download BurstPaperWallet folder
3. `pip3 install pyburstlib`
4. `pip3 install pyqrcode`
5. `pip3 install pypng`
6. `pip3 install Pillow`
7. `pip3 install requests`
7. `python3 main.py <your arguments>`

    1. On macOS you can also run `chmod +x main.py` to make the file executable
    2. Then run the app with `./main.py <your arguments>`

### Usage
By default (no arguments) BurstPaperWallet will generate a new account for you. To do this, simply run the program.

BurstPaperWallet supports generating paper wallets for preexisting wallets. To do so, use the `-p` flag. 

You can opt out of creating a QR code for your paper wallet with the `-n` flag. 
By default, a passphrase QR code **will** be generated.

Opting out of a QR code provides two main benefits, it is harder to steal your passphrase off the paper wallet,
and your passphrase will not ever be written to disk during the account generation. 

---

### 🚨🚨🚨 TEST NET ONLY 🚨🚨🚨
BurstPaperWallet allows you to specify an account to use for funds, in order to automatically broadcast the new wallets
public key.

 **THIS FEATURE IS EXPERIMENTAL AND CONSUMES BURST - ONLY USE ON THE TEST NET**
 
This feature can be used with the `-i` flag, you must then provide the passphrase of an account with sufficient balance to send a transaction 
(minimum is 735001 planck).
 
You can also specify a transaction fee yourself with the `-f` flag.

```-f <transaction fee in planck>```
 
If one is not provided, or you specify a transaction fee less than 735000 planck, the program will default to 735000 planck.
 
If you specify a transaction fee greater than your available balance minus 1 planck, 
either the entire balance of the account will be consumed in the transaction fee.
  
If you do not have enough burst in the provided account to make the minimum transaction cost, the program will simply exit after generating the paper wallet.
Of course, the new wallet will then not have been initialized.
 
#### Feedback or issues regarding this feature are greatly appreciated. 

---

### To do (in order)
* Multi-threading for vanity addresses
* GUI
* Account Migration

### Known issues
* Non-standard passphrase length and form may result in an incorrectly rendered passphrase QR code, and placement of the passphrase may be thrown off.

### Credits - Thank you all!

* @Gadrah - Paper wallet layout (originally from [PaperBurst](https://github.com/umbrellacorp03/PaperBurst))
* @Beatsbears - [pyburstlib](https://github.com/beatsbears/pyburstlib), inspiration/foundation for 
[vanity address generation](https://github.com/beatsbears/burst-vanity-generator), and code review.
* @Nixops - Testing.
