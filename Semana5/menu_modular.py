def sumar(num):
    return sum(num)

def tuplas():
    num = (2, 4, 6, 9, 10, 1, 12)
    print("Tuplas")
    print(f"La tupla original: {num}")
    print(f"El tercer elemento es: {num[2]}")

    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    nueva_tupla = num + (num1,num2)
    print(f"La nueva tupla: {nueva_tupla}")
    lista_numeros = list(nueva_tupla)
    lista_numeros.sort()
    print(f"La lista ordenada: {lista_numeros}")
    suma = sumar(nueva_tupla)
    print(f"La suma de los numeros es: {suma}")

def buscar_telefono(contactos,nombre):
    return contactos.get(nombre)

def diccionarios():
        contactos = {
            "Miguel" : "28861913",
            "Ana"    : "04874671",
            "Eduardo": "163783820"
        }
        print("Diccionario")
        usuario_nuevo = input("Ingrese el nombre del nuevo usuario: ")
        telefono_nuevo = input("Ingrese el telefono del usuario: ")
        contactos [usuario_nuevo] = telefono_nuevo
        print(f"Nombres de usuarios")
        for nombre in contactos.keys():
            print(nombre)
        buscar_usuario = input("Ingrese el nombre de usuario que desea buscar: ")
        telefono = buscar_telefono(contactos, buscar_usuario)
        if telefono:
            print(f"Telefono: {telefono}")
        else:
            print("El contacto no exixte.")
def dividir_numeros():
    try:
        numero1 = int(input("Ingrese el primer número entero: "))
        numero2 = int(input("Ingrese el segundo número entero: "))
        resultado = numero1 / numero2
        print("Suma:", numero1 + numero2)
        print("División:", resultado)
    except ValueError:
        print("Error: Debes ingresar números enteros válidos.")
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")

def contar_palabras(mensaje):
    palabras = mensaje.split()
    return len(palabras)

def trabajar_frase():
    mensaje = input("Ingresa el mensaje deseado: ")
    print("Longitud:", len(mensaje))
    print("En mayúsculas:", mensaje.upper())

    buscar_palabra = input("Palabra que desea remplazar: ") 
    nueva_palabra = input("La nueva palabra es: ")

    mensaje_modificado = mensaje.replace(buscar_palabra,nueva_palabra)
    print(f"El nuevo mensaje es: {mensaje_modificado}")
    cantidad = contar_palabras(mensaje)
    print(f"Cantidad de palabras: {cantidad}")

opcion = 0

while opcion != 5:
    print("       MENÚ PRINCIPAL")
    print("1. Tuplas")
    print("2. Diccionarios")
    print("3. Excepciones")
    print("4. Frases")
    print("5. Finalizar")
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
           tuplas()
        elif opcion == 2:
            diccionarios()
        elif opcion == 3:
            dividir_numeros()
        elif opcion == 4:
            trabajar_frase()
        elif opcion == 5:
            print("\nPrograma finalizado.")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Error: Ingrese un número del 1 al 5.")