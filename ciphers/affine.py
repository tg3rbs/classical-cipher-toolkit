import math

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text, a, b):
    if math.gcd(a, 26) != 1:
        return "Error: a must be coprime with 26."

    result = ""

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            x = ord(char) - base
            encrypted = (a * x + b) % 26
            result += chr(encrypted + base)
        else:
            result += char

    return result

def affine_decrypt(text, a, b):
    if math.gcd(a, 26) != 1:
        return "Error: a must be coprime with 26."

    inverse = mod_inverse(a, 26)
    result = ""

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            y = ord(char) - base
            decrypted = inverse * (y - b) % 26
            result += chr(decrypted + base)
        else:
            result += char

    return result