myName = "Priscilla Abena Aboagye"
shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"

# print(shifted)

for char in myName.lower():
     index = alphabet.find(char)
     new_index = index + shift
     new_char = alphabet[new_index]
     print(new_char)