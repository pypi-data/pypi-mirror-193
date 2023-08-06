from base64 import b64decode, b64encode

import Crypto
# 计算加密解密
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
# 计算签名
from Crypto.Signature import PKCS1_v1_5


class RsaCipher(object):

    def sign_encrypt(self, message, private_key):
        """ RSA私钥加密 MD5withRSA """
        # digest = SHA.new()
        digest = MD5.new()
        digest.update(message.encode(encoding='utf8'))
        private_key = RSA.importKey(b64decode(private_key))
        signer = PKCS1_v1_5.new(private_key)
        sig = b64encode(signer.sign(digest))
        return sig.decode('utf8')

    def get_max_length(self, rsa_key, encrypt=True):
        """加密内容过长时 需要分段加密 换算每一段的长度.
            :param rsa_key: 钥匙.
            :param encrypt: 是否是加密.
        """
        blocksize = Crypto.Util.number.size(rsa_key.n) / 8
        reserve_size = 11  # 预留位为11
        if not encrypt:  # 解密时不需要考虑预留位
            reserve_size = 0
        maxlength = blocksize - reserve_size
        return maxlength

    def long_rsa_public_encrypt(self, msg: str, public_key: str):
        """ 分段使用公钥加密
        单次加密串的长度最大为(key_size / 8 - 11)
        加密的 plaintext 最大长度是 证书key位数 / 8 - 11, 例如1024 bit的证书，被加密的串最长 1024 / 8 - 11=117,
        解决办法是分块加密，然后分块解密就行了，
        因为 证书key固定的情况下，加密出来的串长度是固定的。
        """
        # base64加密后 再进行RSA加密，也可以选择直接进行RSA加密，这个看业务要求
        msg = msg.encode('utf-8')

        length = len(msg)
        public_key = RSA.importKey(b64decode(public_key))
        max_length = int(self.get_max_length(public_key))
        pub_obj = Cipher_pkcs1_v1_5.new(public_key)
        # 长度不用分段
        if length < max_length:
            return b64encode(pub_obj.encrypt(msg)).decode()
        # 需要分段
        offset = 0
        res = []
        while length - offset > 0:
            if length - offset > max_length:
                res.append(pub_obj.encrypt(msg[offset:offset + max_length]))
            else:
                res.append(pub_obj.encrypt(msg[offset:]))
            offset += max_length
        byte_data = b''.join(res)

        return b64encode(byte_data).decode()

    def long_decrypt_by_private_key(self, msg: str, private_key: str):
        """ 使用私钥分段解密 """
        msg = b64decode(msg)
        length = len(msg)
        private_key = RSA.importKey(b64decode(private_key))
        max_length = int(self.get_max_length(private_key, False))
        # 私钥解密
        private_obj = Cipher_pkcs1_v1_5.new(private_key)
        # 长度不用分段
        if length < max_length:
            return b''.join(private_obj.decrypt(msg, b'xyz'))
        # 需要分段
        offset = 0
        res = []
        while length - offset > 0:
            if length - offset > max_length:
                res.append(private_obj.decrypt(msg[offset:offset + max_length], b'xyz'))
            else:
                res.append(private_obj.decrypt(msg[offset:], b'xyz'))
            offset += max_length
        # RSA解密后再进行一次base64解密，也可以直接返回，这个看加密的数据有没有base64加密
        de_base_res = b''.join(res)
        return de_base_res.decode()


if __name__ == '__main__':
    decrypt_text = "1234567890"

    instance = RsaCipher()
    public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCdwMaoHyH1zzdgBUVb/ztZAX/bzv20m/KKCVAnJ0PTI7JJKT7p8MA90MGVvIVFmubBpJ/YCYIxx3uR8xAuX/mPZUni0ZN+beip1b/h9w7xfLJVFjqlXyayn3YQsKBQ5Fau7MQMTA7OVR/LAU/sqKpKzv5oHHG/6WkgPtuIcfNa/wIDAQAB"
    encrypt_text = instance.long_rsa_public_encrypt(decrypt_text, public_key)  # 加密
    print(encrypt_text)

    private_key = "MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAJ3AxqgfIfXPN2AFRVv/O1kBf9vO/bSb8ooJUCcnQ9MjskkpPunwwD3QwZW8hUWa5sGkn9gJgjHHe5HzEC5f+Y9lSeLRk35t6KnVv+H3DvF8slUWOqVfJrKfdhCwoFDkVq7sxAxMDs5VH8sBT+yoqkrO/mgccb/paSA+24hx81r/AgMBAAECgYEAg4aD2w5B8UD4SV17q61MXPQsFycoThoriL0lD8/j87jyX5887i2lCqTvkhlhAFybAl5wSt36p+hK9a+zEQdB+OYUbPSANfUY46bAk+jFQqYA3mNQ5zcYiSOlYBFZHowwQ4UUcfYWbfk+L09RXehbW5fgZQYHqvrcbrI/6bZkztkCQQDTO6UzXaU6vvl98gaWK8kqKvd0oYGmga7xhYGeeoZy3Eydg1Ll9QFa6gJNFPGjYPq6eOM//YD08etiZqJy8xwrAkEAvy+ZQAPdiDs9kYTlpYmmoKHQ7mxtSE5IPtRZ32DzS89+0lfD9hd1NS+Lplheielk+rrg3GnSS4XSTAVMg7zOfQJBAMIKeaBs9vq3MmNS8GAFCv90husZ7gqx+K4fcUnOzjE3VB4h5AYggkUs0D5U7gCidtDTehZvXoYksZEsLTChSQ8CQFkHGz/6DNEBdRwsXJwHS3aFo7tC9mizO2U2kVs51FG7H/1nLTONnODVcRxXDj7+Vi2DlG5PQMQ2XsVTulumMikCQAs+Y5lpS87/+NWOy9ewPjPg2rslJ2dJGEyItKe8LnkhnsrTvL3DApdD+xXekzQTptMzPgyMmqwuc3kXNlVSuDM="
    result = instance.long_decrypt_by_private_key(encrypt_text, private_key)
    print(result)

__all__ = ["RsaCipher"]
