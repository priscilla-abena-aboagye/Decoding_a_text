myName = "Priscilla Abena Aboagye"
shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"
encrypted_text = ""

def caesar():
    for char in myName.lower():
         if char == " ":
              encrypted_text += char
         else: 
             index = alphabet.find(char)
             new_index = (index + shift) % len(alphabet)
             encrypted_text +=alphabet[new_index]
    print(f"Plain Text: {myName}")
    print(f"char: {char} encrypted text: {encrypted_text}")