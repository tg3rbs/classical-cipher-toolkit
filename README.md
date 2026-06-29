# Classical Cipher Toolkit

A Python command-line application that implements several classical encryption algorithms. This project demonstrates modular programming, unit testing with pytest, and the fundamentals of classical cryptography.

## Features

- Caesar Cipher
- Vigenère Cipher
- Atbash Cipher
- Affine Cipher
- Rail Fence Cipher
- Encrypt and decrypt messages
- Interactive command-line interface
- Automated unit tests with pytest

## Project Structure

```
classical-cipher-toolkit/
│
├── ciphers/
│   ├── __init__.py
│   ├── caesar.py
│   ├── vigenere.py
│   ├── atbash.py
│   ├── affine.py
│   └── rail_fence.py
│
├── tests/
│   ├── __init__.py
│   └── test_ciphers.py
│
├── main.py
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/classical-cipher-toolkit.git
```

Move into the project folder:

```bash
cd classical-cipher-toolkit
```

## Running the Program

Run the application:

```bash
python3 main.py
```

## Running the Tests

Run all unit tests with:

```bash
python3 -m pytest
```

## Example

```
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

## Technologies Used

- Python 3
- pytest

## Future Improvements

- Playfair Cipher
- Hill Cipher
- Columnar Transposition Cipher
- Frequency analysis tools
- File encryption support
- Graphical user interface (GUI)

## Author

Theo Gerber

