# BurstPaperWallet
Cross platform paper wallet generator for Burstcoin.

---

### Required
* Python 3.7
* Pyburstlib
* Pyqrcodes
* pypng
* Pillow
* Requests

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
7. `pip3 install requests`
7. `python3 main.py`

### Usage
By default (no arguments) BurstPaperWallet will generate a new account for you. To do this, simply run the program.

BurstPaperWallet supports generating paper wallets for preexisting wallets. To do so, use the `-p` flag show below. 
If your password contains spaces (as all standard ones do), you will need to enter it surrounded by double quotes.

```-p "<your preexisitng passphrase>"```

example: `python3 main.py -p "my super secret passphrase"`

---

### 🚨🚨🚨 TEST NET ONLY 🚨🚨🚨
BurstPaperWallet allows you to specify an account to use for funds, in order to automatically broadcast the new wallets
public key.

 **THIS FEATURE IS EXPERIMENTAL AND CONSUMES BURST - ONLY USE ON THE TEST NET**
 
 To use this feature, you must provide the passphrase (wrapped in double quotes if there are spaces in the passphrase)
 of an account with sufficient balance to send a transaction (minimum is 735001 planck).
 
 Enter the passphrase after the `-i` flag, as shown below.
 
 ```-i "<passphrase of account to charge transaction fee>"```
 
 You can also specify a transaction fee yourself with the `-f` flag.
 
 If one is not provided, you specify a transaction fee less than 735000 planck, the program will default to 735000 planck.
 
 If you specify a transaction fee greater than your available balance minus 1 planck, 
 either the entire balance of the account will be consumed in the transaction fee, or if 
 
 
 ```-f <transaction fee in planck>```
 
 If you do not have enough burst in the provided account to make the minimum transaction cost, the program will simply exit after generating the paper wallet.
 Of course, the new wallet will then not have been initialized.
 
 #### Feedback or issues regarding this feature are greatly appreciated. 

---

### To do (in order)
* Vanity Addresses
* GUI
* Account Migration

### Known issues
* Non-standard passphrase lengths may not render the passphrase QR code the correct size.

### Credits

* @Gadrah - Paper wallet layout (originally from [PaperBurst](https://github.com/umbrellacorp03/PaperBurst))
* @Beatsbears - [pyburstlib](https://github.com/beatsbears/pyburstlib)