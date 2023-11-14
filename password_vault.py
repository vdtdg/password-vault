import json
import os

from cryptography.fernet import Fernet


class CouldNotOpenVaultException(Exception):
    pass


class PasswordVault:
    def __init__(self, key):
        self.db_file_name = 'password_vault.db'
        self.key = key.encode()
        self.fernet = Fernet(self.key)
        self.vault = None

        if not os.path.isfile(self.db_file_name):
            self.create_vault()
        else:  # Let's check if the provided key is correct
            self.load_vault()

    def create_vault(self):
        self.vault = {}
        self.save_vault()

    def load_vault(self):
        with open(self.db_file_name, 'r') as db_file:
            encrypted_vault = db_file.read().encode()
            try:
                decrypted_vault = self.fernet.decrypt(encrypted_vault).decode()
                self.vault = json.loads(decrypted_vault)
            except Exception as e:
                print("Couldn't open vault. Key is incorrect.")
                raise CouldNotOpenVaultException from e

    def save_vault(self):
        with open(self.db_file_name, 'w') as db_file:
            vault_as_json = json.dumps(self.vault).encode()
            encrypted_vault = self.fernet.encrypt(vault_as_json).decode()
            db_file.write(encrypted_vault)

    def store_password(self, service, password):
        self.vault[service] = password
        self.save_vault()

    def retrieve_password(self, service):
        return self.vault.get(service)

    def remove_password(self, service):
        self.vault.pop(service, None)
        self.save_vault()
