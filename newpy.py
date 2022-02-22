import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Protocol.KDF import PBKDF2
import os
 
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
 

key = b'q\xcdB\xe4A\x18\x82\x0c\xbd`\x944}&\xa6\xc0\x8bo\x91\xe4\x0f\x1e\xdap\xb7\xfd\xad~\xef\x1a\xa6\xbb'
 
 
def encrypt(raw):
    private_key = key
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))
 
 
def decrypt(enc):
    private_key = key
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))

def encrypt_files():
    with open('pass.json', 'r') as fo:
            ciphertext = fo.read()
    enc = encrypt(ciphertext)
    with open('pass.json' + ".enc", 'wb') as fo:
            fo.write(enc)
def decrypt_files():
    with open('pass.json.enc','r') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext)
    with open('pass.json','wb') as fo:
        fo.write(dec)
    return dec

def encrypt_new(plaintext):
    enc = encrypt(plaintext)
    with open('pass.json'+".enc",'wb') as fo:
        fo.write(enc)

def decrypt_new():
    with open('pass.json.enc', 'rb') as fo:
            ciphertext = fo.read()
    dec = decrypt(ciphertext)
    print(dec)
    return dec
    

 