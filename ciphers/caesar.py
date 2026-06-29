ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def clean_text(text):
    return "".join(char.upper() for char in text if char.isalpha())

def caesar_encrypt(text, shift):
    text = clean_text(text)
    result = ""

    for char in text:
        index = ALPHABET.index(char)
        new_index = (index + shift) % 26
        result += ALPHABET[new_index]

    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)