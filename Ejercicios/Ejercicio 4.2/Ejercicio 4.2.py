import platform
import os
system = platform.system()

# I switch from linux and windows, so I check what im using and in base of that
# i modify the text inside of the system so i dont have to be changing it everytime
# i switch from windows to linux or linux to windows.
if system == "Windows":
    clear = "CLS"
else:
    clear = "clear"

os.system(clear)

main_inventory = []
listBought = []
itemBought = []

with open("Ejercicios/Ejercicio 4.2/inventario.txt", "r") as inventory:
    main_inventory = inventory.readlines()
with open("Ejercicios/Ejercicio 4.2/Lista de compras.txt", "r") as list:
    listBought = list.readlines()

for item in listBought:
    print(item, end='')
item = ''

while item not in listBought:
    



