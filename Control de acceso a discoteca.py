print("#########  DEJAVÚ  ##########")

#Datos personales
print("Hola, ingresa tus datos: ")
nombre = input("Tu nombre: ")
apellido = input("Tu apellido: ")
edad = int(input("Tu edad: ") )
mail = input("Ingresa tu correo: ")

print("Ingresa tu genero ingresando un numero: ")
print("1. Hombre")
print("2. Mujer")
print("3. No binario")
genero = int(input("Genero: "))
precio_hom = 15
precio_muj = 5
precio_nob = 8

def run_proy(nom, ape, ed, gmail, gen):
    #Genero
    if gen == 1:
        print(f"Bienvenido {nom} {ape}")
    elif gen == 2:
        print(f"Bienvenida {nom} {ape}")
    elif gen == 3:
        print(f"Bienvenide {nom} {ape}")
    else:
        print("No reconocido")
    #Edad
    if ed >= 18:
        print(f"Tu edad es {ed}, cumples con el requisito para ingresar")
    elif ed < 18:
        print(f"No cumples con el requisito de edad, no puedes ingresar")
    elif ed > 60:
        print(f"Lo siento tu edad es muy avanzada para ingresar")
    #Precios
    if gen == 1:
        print(f"El costo total es de: ${precio_hom}")
    elif gen == 2:
        print(f"El costo total es de: ${precio_muj}")
    elif gen == 3:
        print(f"El costo total es: ${precio_nob}")

run_proy(nombre, apellido, edad, mail, genero)
