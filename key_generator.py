from cryptography.fernet import Fernet


# Pour que cet import fonctionne, faire pip install cryptography

def generate_key():
    return Fernet.generate_key().decode()


if __name__ == '__main__':
    key = generate_key()
    print(f"Store this Fernet key in a safe place: {key}")
