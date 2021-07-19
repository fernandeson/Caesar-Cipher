#####CAESAR CYPHER PROGRAM

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("\n****************** CAESAR CYPHER *****************\n")

def caesar (start_text, shif_number, direction_to_shift):
    end_text = ""
    if direction_to_shift == "decode":
        shif_number *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shif_number
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction}d text for '{start_text}' is: {end_text}.")

should_continue = True
while should_continue:
    direction = input("1. Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":
        direction = input(" > Please try again. You should type 'encode' to encrypt or 'decode' to decrypt:\n")
    text = input("2. Type your message:\n").lower()
    shift = int(input("3. Type the shift number:\n"))
    if shift < 0:
        shift = int(input(" > The shift number must be greater than zero! Try again:\n"))
    else:
        shift = shift % 26
    caesar(start_text=text, shif_number=shift, direction_to_shift=direction)
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if go_again == "no":
        should_continue = False
        print("Bye Bye!")