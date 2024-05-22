alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    coded = ""
    for letter in  text:
        coded += "".join(alphabet[(alphabet.index(letter) + shift) % 26])
    print(f"The encoded text is {coded}")

def decrypt(text, shift):
    decoded = ""
    for letter in  text:
        decoded += "".join(alphabet[(alphabet.index(letter) - shift) % 26])
    print(f"The decoded text is {decoded}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Not a valid input")
