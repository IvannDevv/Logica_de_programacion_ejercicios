#CALCULADORA DE IMPUESTOS
print("####Calculador de impuestos####")

#Pedir Datos
nom = input("Ingresa tu nombre: ")
ape = input("Ingresa tu apellido: ")
ingre = int(input("Ingresa el numero de tus ingresos por mes: "))
habitad = input("Vives en zona rural? Si o No:     ")

#Funcion condicional
def saludo (nombre, apellido, ingresos, habi):
    print(f"Bienvenido {nombre} {apellido}")
    impuesto = 0

    if ingresos < 1000:
        print("Ok, no pagas impuestos")
    elif ingresos >= 1000 and ingresos < 2000:
        impuesto = ingresos * 0.10
        print(f"Impuestso del 10%: {impuesto:.2f}")
    else:
        impuesto = ingresos * 0.2
        print(f"Impuesto del 20%: {impuesto:.2f}")

    #Descuento por habitad
    habi = habi.lower()
    if habi.startswith("si") and impuesto > 0:
        descuento_5 = impuesto * 0.05
        con_zona_rural = impuesto - descuento_5
        print(f"El descuento por vivir en zona rural es de 5%, el total seria: {con_zona_rural}")
    elif impuesto > 0:
        print(f"El descuento de habitad en zona rural no aplica")



saludo(nom, ape, ingre,habitad)