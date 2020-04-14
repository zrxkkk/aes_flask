from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')

# encrypt
def encrypt(text):
    key = '9999999999999999'.encode('utf-8')
    mode = AES.MODE_ECB
    text = add_to_16(text)
    cryptos = AES.new(key, mode)

    cipher_text = cryptos.encrypt(text)
    return str(b2a_hex(cipher_text), encoding='utf-8')


# decrypt
def decrypt(text):
    key = '9999999999999999'.encode('utf-8')
    mode = AES.MODE_ECB
    cryptor = AES.new(key, mode)
    plain_text = cryptor.decrypt(a2b_hex(text))
    return bytes.decode(plain_text).rstrip('\0')


if __name__ == '__main__':
    e = encrypt("hello world")  # 加密
    d = decrypt(e)  # 解密
    print("encrypt:", e)
    print("decrypt:", d)
