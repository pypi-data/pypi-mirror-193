from hashlib import sha256, md5


def hash_sha256(text: str):
    return sha256(text.encode()).hexdigest()


def hash_md5(text: str):
    m = md5()
    m.update(text.encode())
    return m.hexdigest()


if __name__ == '__main__':
    result = hash_sha256("1234567890")
    print(result)

    result = hash_md5("1234567890")
    print(result)

__all__ = ["hash_sha256", "hash_md5"]
