import hashlib


def main():
    print("Welcome to Python Password Cracking!")
    message = input("Enter a message to encode: ")

    # encode message to bytes with UTF-8
    message = message.encode()

    # hash with MD5
    print(f"MD5: {hashlib.md5(message).hexdigest()}")

    # hash with SHA-256
    print(f"SHA-256: {hashlib.sha256(message).hexdigest()}")

    # hash with SHA-512
    print(f"SHA-512: {hashlib.sha512(message).hexdigest()}")


main()
