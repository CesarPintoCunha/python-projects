from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text, shift, direction):
        coded = ""
        if direction == "encode":
            for letter in  text:
                coded += "".join(alphabet[(alphabet.index(letter) + shift) % 26])
            print(f"The encoded text is {coded}")
        if direction == "decode":
            for letter in text:
                coded += "".join(alphabet[(alphabet.index(letter) - shift) % 26])
            print(f"The decoded text is {coded}")
        
    caesar(text, shift, direction)

    answer = input("Type 'yes' if you want to do another operation. Otherwise type 'no'\n")

    if answer.lower() == "yes":
        continue
    elif answer.lower() == 'no':
        print("Goodbye")
        break    
