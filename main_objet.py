from getpass import getpass

from password_vault import PasswordVault

if __name__ == '__main__':
    key = getpass(prompt="Enter your key: ")
    vault = PasswordVault(key=key)

    while True:
        option = int(input("1. Store password\n2. Retrieve password\n3. Remove password\n4. Quit\n"))
        if option == 1:
            service = input("Enter the service name: ")
            password = getpass("Enter the password: ")
            vault.store_password(service, password)
        elif option == 2:
            service = input("Enter the service name: ")
            password = vault.retrieve_password(service)
            if password is not None:
                print("Password:", password)
            else:
                print(f"There are no password for service {service}")
        elif option == 3:
            service = input("Enter the service name: ")
            vault.remove_password(service)
        elif option == 4:
            break
        else:
            print("Invalid option.")
