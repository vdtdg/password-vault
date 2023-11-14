# password-vault
A command-line password vault to secure your password in a local encrypted file.

## What does it do ?
Here are the basic functions the program performs

1. Storing a password for a service.
2. Retrieving a stored password.
3. Removing a stored password.

This program encrypts all the data in the vault using Fernet symmetric encryption. The key used for encryption is generated once you run the program for the first time and displayed. You should keep this key somewhere safe, as it will be needed to decrypt the data.

The user interacts with the program from the command-line, and it prompts for all the necessary information. The encrypted vault is stored in a file called `password_vault.db`. Remember, never shared the key or the vault file.

This example is fairly simple, and there's no error-checking. Also, it's very important to ensure that the key is stored in a secure manner, which is not covered here. You could generate it from a passphrase and store it in a secure password manager. Implementing these additional security protocols would be an excellent improvement to the project.


## How to use
- Install dependencies using `pip install -r requirements` 
- Before first run, generate a key using `python key_generator.py`
- Run using `python main_objet.py` for the Object Oriented approach
- Run using `python main_procedural.py` for the Procedural Oriented approach


## Notes pour les étudiants de B3 Cyber IA School
N'hésitez pas à pratiquer encore et encore.  
Essayer d'ajouter des features !