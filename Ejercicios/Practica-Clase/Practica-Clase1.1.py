calif = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]
total = 0
count = 0
lenght = len(calif)

while count < lenght:
    total += calif[count]
    count += 1;

promedio = total / lenght

print("La media es: ",promedio)
