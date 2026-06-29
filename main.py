"""
Classical Cipher Toolkit
Author: Theo Gerber

A Python command-line application that implements five classical
encryption algorithms:
- Caesar Cipher
- Vigenère Cipher
- Atbash Cipher
- Affine Cipher
- Rail Fence Cipher
"""

from ciphers.caesar import caesar_encrypt, caesar_decrypt
from ciphers.vigenere import vigenere_encrypt, vigenere_decrypt
from ciphers.atbash import atbash
from ciphers.affine import affine_encrypt, affine_decrypt
from ciphers.rail_fence import rail_fence_encrypt, rail_fence_decrypt

# Main program loop
def main():
    # Display the menu until the user chooses to quit
    while True:
        # Display available ciphers
        print("\nChoose a cipher")
        print("1. Caesar")
        print("2. Vigenere")
        print("3. Atbash")
        print("4. Affine")
        print("5. Rail Fence")
        print("6. Quit")     
        choice = input("Choose cipher: ")    
        # Exit the program
        if choice == "6":
            print("Goodbye!")
            break    
        # Caesar Cipher
        if choice == "1":
            mode = input("Encrypt or decrypt? ").lower()
            message = input("Enter message: ")
            shift = int(input("Enter shift: "))

            if mode == "encrypt":
                print("\nResult:", caesar_encrypt(message, shift))
            elif mode == "decrypt":
                print("\nResult:", caesar_decrypt(message, shift))
            else:
                print("Invalid mode.")   
        # Vigenere Cipher
        elif choice == "2":
            mode = input("Encrypt or decrypt? ").lower()
            message = input("Enter message: ")
            key = input("Enter key: ")

            if mode == "encrypt":
                print("\nResult:", vigenere_encrypt(message, key))
            elif mode == "decrypt":
                print("\nResult:", vigenere_decrypt(message, key))
            else:
                print("Invalid mode.") 
        # Atbash Cipher
        elif choice == "3":
            message = input("Enter message: ")
            print("\nResult:", atbash(message))    
        # Affine Cipher
        elif choice == "4":
            mode = input("Encrypt or decrypt? ").lower()
            message = input("Enter message: ")
            a = int(input("Enter a value: "))
            b = int(input("Enter b value: "))

            if mode == "encrypt":
                print("\nResult:", affine_encrypt(message, a, b))
            elif mode == "decrypt":
                print("\nResult:", affine_decrypt(message, a, b))
            else:
                print("Invalid mode.")
        # Rail Fence Cipher
        elif choice == "5":
            mode = input("Encrypt or decrypt? ").lower()
            message = input("Enter message: ")
            rails = int(input("Enter number of rails: "))

            if mode == "encrypt":
                print("\nResult:", rail_fence_encrypt(message, rails))
            elif mode == "decrypt":
                print("\nResult:", rail_fence_decrypt(message, rails))
            else:
                print("Invalid mode.")    
        # Handle an invalid menu selection
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()