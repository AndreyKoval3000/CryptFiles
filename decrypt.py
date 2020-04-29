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

# decrypt
a = open(folder + ":" + file, "rb")
decrypted = aes.decrypt(base64.b64decode(a.read().decode("utf-8").replace("\r\n", "").encode("utf-8")))
a.close()
a = open("decrypt_" + file, "wb")
a.write(decrypted)
a.close()
