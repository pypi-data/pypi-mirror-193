import base64

from Crypto import Random
from Crypto.Cipher import AES


class AESCipher(object):

    def __init__(self, key: str, iv: str = None, mode="CBC"):
        self.bs = 16
        self.key = key.encode()
        if not iv:
            self.iv = Random.new().read(AES.block_size)
        else:
            self.iv = iv.encode()
        self.mode = mode

    def encrypt(self, raw: str):
        raw = self._pad(raw)
        if self.mode == "CBC":
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        elif self.mode == "ECB":
            cipher = AES.new(self.key, AES.MODE_ECB)
        else:
            raise Exception("不支持的加密类型")
        return base64.b64encode(cipher.encrypt(raw.encode())).decode()

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        if self.mode == "CBC":
            cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        elif self.mode == "ECB":
            cipher = AES.new(self.key, AES.MODE_ECB)
        else:
            raise Exception("不支持的加密类型")
        return self._unpad(cipher.decrypt(enc)).decode('utf-8')

    def _pad(self, s) -> str:
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]


if __name__ == '__main__':
    aes = AESCipher("1234567890123456", "1234567890123456", mode="CBC")
    result = aes.encrypt("s")
    print(result)

    result = aes.decrypt(result)
    print(result)

__all__ = ["AESCipher"]
