import platform
import os

system = platform.system()

# Determine the clear command based on the operating system
clear_command = "cls" if system == "Windows" else "clear"
os.system(clear_command)

main_inventory = []
listBought = []
itemBought = []

with open("Ejercicios/Ejercicio 4.2/inventario.txt", "r") as inventory_file:
    main_inventory = inventory_file.readlines()

with open("Ejercicios/Ejercicio 4.2/Lista de compras.txt", "r") as list_file:
    listBought = list_file.readlines()

lowerListBought = [item.strip().lower() for item in listBought]
lowerMainInventory = [item.strip().lower() for item in main_inventory]

for item in listBought:
    print(item, end='')
print()
while True:
    item = input("Ingrese el artículo que desea eliminar del inventario o 'fin' para salir: ").strip().lower()
    
    if item == 'fin':
        break
    else:
        if item in lowerListBought and item in lowerMainInventory:
            lowerListBought.remove(item)
            lowerMainInventory.remove(item)
            itemBought.append(item)
            print(f"'{item}' eliminado del inventario y añadido a la lista de comprados.")
        else:
            print("El artículo no está en el inventario o ya se ha eliminado.")

print("Artículos comprados:")
for item in itemBought:
    print(item)
