ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def clean_text(text):
    return "".join(char.upper() for char in text if char.isalpha())

def vigenere_encrypt(text, key):
    text = clean_text(text)
    key = clean_text(key)
    result = ""

    for i, char in enumerate(text):
        text_index = ALPHABET.index(char)
        key_index = ALPHABET.index(key[i % len(key)])
        result += ALPHABET[(text_index + key_index) % 26]

    return result

def vigenere_decrypt(text, key):
    text = clean_text(text)
    key = clean_text(key)
    result = ""

    for i, char in enumerate(text):
        text_index = ALPHABET.index(char)
        key_index = ALPHABET.index(key[i % len(key)])
        result += ALPHABET[(text_index - key_index) % 26]

    return result