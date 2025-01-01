myName = "Priscilla Abena Aboagye"
shift = 3
# print(type(myName))
# print(myName[3])

alphabet = "abcdefghijklmnopqrstuvwxyz"
index = alphabet.find(myName[0].lower())

print(index)
shifted = alphabet[index + shift]
print(shifted)