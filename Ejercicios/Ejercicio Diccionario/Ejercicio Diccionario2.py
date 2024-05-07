def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

diccionario = {}
userInput = "El cuadrado del primer término, más el doble producto del primero por el segundo, más el cuadrado del segundo"

cleanSTR = normalize(userInput)
noComas = cleanSTR.replace(",", "")
words = noComas.split()

for word in words:
    if word in diccionario:
        diccionario[word] += 1
    else:
        diccionario[word] = 1

i = 0
print("Conteo de palabras en la frase:")
for palabra, conteo in diccionario.items():
    print(f"{palabra}: {conteo}")
    i = i +1 

print("Número de palabras únicas: ", i)
