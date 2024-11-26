from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a key for encryption and saves it to a file.
    """
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)
    
def load_key():
    """
    Loads the encryption key from the file.
    Returns:
        bytes: The encryption key.
    """
    with open("key.key", "rb") as key_file:
        return key_file.read()
    
def add_password(account, password, password_data):
    """
    Encrypts and stores a password for an account.
    Args:
        account (str): The account name.
        password (str): The password.
        password_data (dict): The dictionary to store encrypted passwords.
    """
    key = load_key()
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode())
    password_data[account] = encrypted_password
    print(f"Password added for account: {account}")

def retrive_password(account, password_data):
    """
    Retrieves and decrypts a password for a given account.
    Args:
        account (str): The account name.
        password_data (dict): The dictionary of encrypted passwords.
    Returns:
        str: The decrypted password, or a message if the account doesn't exist.
    """
    key =load_key()
    cipher = Fernet(key)
    if account in password_data:
        encrypted_password = password_data[account]
        decrypted_password = cipher.decrypt(encrypted_password).decode()
        return decrypted_password
    else:
        return "Account not found."
    
#Main program
def main():
    """
    Main program to manage passwords.
    """
    passwords_data ={}
    print("Welcome to the Password Manager!")

    while True:
        print("\nChoose an optiop:")
        print("1. Add a password")
        print("2. Retrive a password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account = input ("Enter the account name: ")
            password = input("Enter the Password:")
            add_password( account, password, passwords_data)
        
        elif choice == "2":
            account = input("Enter the account name to retrieve: ")
            print("Password:", retrive_password(account, passwords_data))

        elif choice =="3":
            print("Exiting Password manager. Goodbye!")
            break

        else:
            print("Invalid choice . please try again.")

if __name__ == "__main__":
   
    try:
        with open("key.key", "rb"):
            pass
    except FileNotFoundError:
        generate_key()

    main()