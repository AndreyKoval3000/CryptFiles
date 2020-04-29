from Crypto.Cipher import AES
import base64
import sys


def pad(text):
    while len(text) % 16 != 0:
        text += b' '
    return text


folder = sys.argv[0]
file = sys.argv[1]
password = str(sys.argv[2]).encode("utf-8")

aes = AES.new(pad(password), AES.MODE_ECB)

# encrypt
a = open(file, "rb")
encrypted = base64.b64encode(aes.encrypt(pad(a.read())))
a.close()
a = open(folder + ":" + file, "wb")
a.write(encrypted)
a.close()
