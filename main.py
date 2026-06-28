from ciphers import caesar, vigenere

def main():
    print("Classical Cipher Toolkit")
    print("1. Caesar Cipher")
    print("2. Vigenere Cipher")

    choice = input("Choose cipher: ")
    mode = input("Encrypt or decrypt? ").lower()
    message = input("Enter message: ")

    if choice == "1":
        shift = int(input("Enter shift: "))

        if mode == "encrypt":
            print(caesar.encrypt(message, shift))
        else:
            print(caesar.decrypt(message, shift))

    elif choice == "2":
        key = input("Enter key: ")

        if mode == "encrypt":
            print(vigenere.encrypt(message, key))
        else:
            print(vigenere.decrypt(message, key))

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()