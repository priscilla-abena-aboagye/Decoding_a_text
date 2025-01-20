myName = "Priscilla Abena Aboagye"
shift = 3
custom_key = "python"
alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesar(message, changed):
    encrypted_text = ""
    
    for char in message.lower(): # it takes every letter in message which is myName
         if char == " ":
              encrypted_text += char # Append space to the message
         else: 
             index = alphabet.find(char) # finds char and places it in alphabet and the number gotten is stored in a variable.
             new_index = (index + changed) % len(alphabet)
             encrypted_text +=alphabet[new_index]
    print("----------------")
    print(f"Plain Text: {message}")
    print(f"encrypted text: {encrypted_text}")

caesar(myName, shift) # calls the function
caesar(myName, 10)




def vigenere(message, key, direction = 1):
     key_index = 0 # this makes it repeat itself and also makes it start from the first letter
     encrypted_text = ""
     for char in message.lower():
          if not char.isalpha():
               encrypted_text += char
          else:
               key_char = key[key_index % len(key)]
               # Every time you process a letter in the text, you increase key_index by 1 to use the next letter of the key.
               key_index += 1 
               # Define the offset and the encrypted/decrypted letter
               offset = alphabet.index(key_char) 
               index = alphabet.find(char)
               new_index = (index + offset * direction) % len(alphabet)
               encrypted_text += alphabet[new_index]
     return encrypted_text

def encrypt(message, key):
     return vigenere(message, key)
def decrypt(message, key):
     return vigenere(message, key, -1)

encryption = encrypt(myName, custom_key)
decryption = decrypt(encryption, custom_key)
print("------------")
print(f"Encrypted text: {encryption}")
print(f"Key: {custom_key}")
print(f"Decryted text: {decryption}")
print("-------------")