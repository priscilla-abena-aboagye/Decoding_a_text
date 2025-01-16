myName = "Priscilla Abena Aboagye"
shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"
encrypted_text = ""

# print(shifted)

for char in myName.lower():
     if char == " ":
          encrypted_text += char
     else: 
         index = alphabet.find(char)
         new_index = index + shift
         encrypted_text +=alphabet[new_index]
     print(f"char: {char} encrypted text: {encrypted_text}")