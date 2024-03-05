num = int(input("Ingresa un valor entero: "))

maxEggsPerCarton = 6
isEmpty = True
isPair = True
isNegative = True


if (num >= 0):
    isNegative = False

    if (num != 0):
        isEmpty = False

        if (num % maxEggsPerCarton == 0):
            isPair = False
            if (num / maxEggsPerCarton == 1):
                print("Se lleno ", int(num / maxEggsPerCarton), "cartera de ", maxEggsPerCarton, "huevos")
            if (num / maxEggsPerCarton > 1):
                print("Se llenaron ", int(num / maxEggsPerCarton), "carteras de ", maxEggsPerCarton, "huevos")

        if (isPair):
            if (num > maxEggsPerCarton):
                print("Se lleno",int(num / maxEggsPerCarton) ,"catera de ", maxEggsPerCarton, "huevos")
                if (num % maxEggsPerCarton == 1):
                    print("En la ultima cartera se coloco: ", num % maxEggsPerCarton, "huevo")
                if (num % maxEggsPerCarton > 1):
                    print("En la ultima cartera se colocaron: ", num % maxEggsPerCarton, "huevos")
                print("La cantidad de huevos adicionales que se necesitan para llenar una cartera es de: ", maxEggsPerCarton - (num % maxEggsPerCarton))

            if (num < maxEggsPerCarton):
                print("La cantidad de huevos que se necesitan para llenar una cartera es de: ", maxEggsPerCarton - (num % maxEggsPerCarton))
                if (num % maxEggsPerCarton == 1):
                    print("En la ultima cartera se coloco: ", num % maxEggsPerCarton, "huevo")
                if (num % maxEggsPerCarton > 1):
                    print("En la ultima cartera se colocaron: ", num % maxEggsPerCarton, "huevos")
                print("La cantidad de huevos adicionales que se necesitan para llenar una cartera es de: ", maxEggsPerCarton - (num % maxEggsPerCarton))

    if (isEmpty):
        print("La cantidad de huevos que se necesitan para llenar una cartera es de: ", maxEggsPerCarton)

if (isNegative):
    print("El valor ingresado es negativo")