# Classical Cipher Toolkit

A Python command-line toolkit implementing five classical cryptographic ciphers with a modular cipher interface and automated tests.

## Supported Ciphers

- **Caesar Cipher** — substitution using a fixed alphabetic shift
- **Vigenère Cipher** — polyalphabetic substitution using a repeating key
- **Atbash Cipher** — substitution based on a reversed alphabet
- **Affine Cipher** — substitution using an affine transformation over the alphabet
- **Rail Fence Cipher** — transposition using a configurable number of rails

Each cipher supports encryption and decryption through the command-line interface.

## Project Structure

```text
classical-cipher-toolkit/
├── ciphers/
│   ├── __init__.py
│   ├── caesar.py
│   ├── vigenere.py
│   ├── atbash.py
│   ├── affine.py
│   └── rail_fence.py
├── tests/
│   ├── __init__.py
│   └── test_ciphers.py
├── main.py
├── README.md
└── requirements.txt
```

Cipher implementations are separated into individual modules, while `main.py` provides the interactive command-line interface.

## Installation

Clone the repository:

```bash
git clone https://github.com/tg3rbs/classical-cipher-toolkit.git
cd classical-cipher-toolkit
```

Install the required dependencies:

```bash
python3 -m pip install -r requirements.txt
```

## Usage

Run the command-line interface:

```bash
python3 main.py
```

Example:

```text
Choose a cipher

1. Caesar
2. Vigenere
3. Atbash
4. Affine
5. Rail Fence
6. Quit

Choose cipher: 1
Encrypt or decrypt? encrypt
Enter message: HELLO
Enter shift: 3

Result: KHOOR
```

## Testing

Run the automated test suite with pytest:

```bash
python3 -m pytest
```

Tests cover encryption and decryption behavior across the implemented cipher modules.

## Security Considerations

These classical ciphers are historically significant cryptographic algorithms but provide no meaningful security against modern cryptanalysis.

This toolkit is intended for studying classical cryptographic transformations and their implementation rather than protecting sensitive information.

