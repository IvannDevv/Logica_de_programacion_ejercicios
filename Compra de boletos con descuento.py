nombre = input("Ingresa tu nombre: ")
entrada = 20
print(f"Bienvenido, {nombre}")
edad = int(input("Ingresa tu edad: "))
if edad <= 12:

    #Descuento por ser menor de 12
    descuento_12anni = float(entrada * 0.50) 
    descuento_total_12anni = entrada - descuento_12anni
    print(f"El total seria: $/{descuento_total_12anni}")

    #Descuento si compra mas de 5 tickets
    print("Cuantos boletos desea comprar??")
    number_tickets = int(input())

    if number_tickets > 5:
        calc = number_tickets * descuento_total_12anni
        total_de_entradas = calc * 0.10
        descuento = calc - total_de_entradas
        print(f"El total a pagar seria: $/{descuento}")
        print("Gracias por tu compra")
        
    elif number_tickets < 5:
        print(f"El total seria {descuento_total_12anni}")
        print("Gracias por tu compra")
else:
    print(f"El total seria. $/{entrada}")
    print("Cuantos boletos desea comprar??")
    number_tickets = int(input())
    if number_tickets > 5:
        calc = number_tickets * entrada
        total_de_entradas = calc * 0.10
        descuento = calc - total_de_entradas
        print(f"El total a pagar seria: $/{descuento}")


