myName = "Priscilla Abena Aboagye"
shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesar(message, changed):
    encrypted_text = ""
    
    for char in message.lower():
         if char == " ":
              encrypted_text += char
         else: 
             index = alphabet.find(char)
             new_index = (index + changed) % len(alphabet)
             encrypted_text +=alphabet[new_index]
    print(f"Plain Text: {message}")
    print(f"encrypted text: {encrypted_text}")

caesar(myName, shift)
caesar(myName, 10)


def vigenere(message, changed):
     encrypted_text = ""
     for char in message.lower():
          if char == " ":
               encrypted_text += char
          else:
               index = alphabet.find(char)
               new_index = alphabet[index + shift]
