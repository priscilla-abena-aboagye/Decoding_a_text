myName = "Priscilla Abena Aboagye"
shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"

# print(shifted)

for i in myName.lower():
     index = alphabet.find(i)
     print(i, index)
     new_index = index + shift