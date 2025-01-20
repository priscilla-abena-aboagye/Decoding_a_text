myName = "Priscilla Abena Aboagye"
shift = 3
custom_key = "python"
alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesar(message, changed):
    encrypted_text = ""
    
    for char in message.lower(): # it takes every letter in message which is myName
         if char == " ":
              encrypted_text += char # if char is an empty space then add it to the encrpted_text
         else: 
             index = alphabet.find(char) # finds char and places it in alphabet and the number gotten is stored in a variable.
             new_index = (index + changed) % len(alphabet)
             encrypted_text +=alphabet[new_index]
    print(f"Plain Text: {message}")
    print(f"encrypted text: {encrypted_text}")

caesar(myName, shift) # calls the function
caesar(myName, 10)




def vigenere(message, key):
     key_index = 0 # this makes it repeat itself and also makes it start from the first letter
     encrypted_text = ""
     for char in message.lower():
          if char == " ":
               encrypted_text += char
          else:
               index = alphabet.find(char)
               new_index = (index + changed) % len(alphabet)
               encrypted_text += alphabet[new_index]
