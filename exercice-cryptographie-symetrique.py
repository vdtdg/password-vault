from cryptography.fernet import Fernet

"""
What’s a Fernet key ?

A Fernet key is a type of symmetric encryption key used in Python's cryptography library for the Fernet class to encrypt and decrypt data.

Fernet guarantees that data encrypted using it can't be manipulated or read without the key. It is URL-safe base64-encoded 32-byte key. This key must
 be kept secret.

It uses 256-bit AES (Advanced Encryption Standard) for encryption. It splits the given 32-byte key into two halves. The first half is used for AES-265
 CBC (Cipher Block Chaining) encryption and the second half is used for HMAC SHA256 signing. The combination provides a secure message that cannot be 
 read or altered.
"""

if __name__ == '__main__':
    key = Fernet.generate_key()
    print(f'Key: {key}')

    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(b"Text to encrypt")  # ou .encode('utf-8')
    plain_text = cipher_suite.decrypt(cipher_text)

    print(f'Cipher text: {cipher_text}')
    print(f'Plain text: {plain_text.decode()}')
