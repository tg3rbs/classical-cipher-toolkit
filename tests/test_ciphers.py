from ciphers.caesar import caesar_encrypt, caesar_decrypt
from ciphers.vigenere import vigenere_encrypt, vigenere_decrypt
from ciphers.atbash import atbash
from ciphers.affine import affine_encrypt, affine_decrypt
from ciphers.rail_fence import rail_fence_encrypt, rail_fence_decrypt

def test_caesar():
    assert caesar_encrypt("abc", 3) == "DEF"
    assert caesar_decrypt("def", 3) == "ABC"

def test_vigenere():
    assert vigenere_encrypt("attackatdawn", "lemon") == "LXFOPVEFRNHR"
    assert vigenere_decrypt("lxfopvefrnhr", "lemon") == "ATTACKATDAWN"

def test_atbash():
    assert atbash("abc") == "zyx"
    assert atbash("Hello") == "Svool"

def test_affine():
    encrypted = affine_encrypt("hello", 5, 8)
    assert encrypted == "rclla"
    assert affine_decrypt(encrypted, 5, 8) == "hello"

def test_rail_fence():
    encrypted = rail_fence_encrypt("HELLOWORLD", 3)
    assert encrypted == "HOLELWRDLO"
    assert rail_fence_decrypt(encrypted, 3) == "HELLOWORLD"