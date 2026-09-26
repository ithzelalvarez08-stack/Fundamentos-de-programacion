# Sistema de pedidos del restaurante "LAS FLORES"
# Registra pedidos por mesa, calcula cuentas y propinas,
# conserva la fecha, guarda información en archivos y permite depuración con PDB.

import os
import time
import pdb
#Variable de depuracion.
MODO_DEBUG = False

menu = [
    [1, "Ensalada Cesar", 100],
    [2, "Enchiladas Rojas", 150],
    [3, "Pasta", 100],
    [4, "Enchiladas Verdes", 100],
    [5, "Aguachile", 200],
    [6, "Pastel de tres leches", 50],
    [7, "Helado napolitano", 150],
    [8, "Agua del dia", 40],
    [9, "Cafe", 35],
    [10, "Refresco", 40]
]
#Lista de los archivos .txt relacionados con las 5 mesas.
archivos_prueba = [
    "pedidos_mesa1.txt",
    "pedidos_mesa2.txt",
    "pedidos_mesa3.txt",
    "pedidos_mesa4.txt",
    "pedidos_mesa5.txt"
]

def bienvenida(usuario):
    mensaje = (
        f"Bienvenido/a {usuario} al sistema de pedidos "
        "del Restaurante Las Flores."
    )
    print("\n" + "=" * 55)
    print(mensaje)
    print("=" * 55)


def pantalla():
    print("\nCargando sistema...")
    for segundo in range(1, 5):
        print(f"Carga: {segundo} segundo(s)")
        time.sleep(1)
    print("Sistema listo.")


def capturar_fecha():
    """Devuelve la fecha en la tupla requerida: Fecha = dia, mes, anio."""
    while True:
        try:
            dia = int(input("Ingrese el día: "))
            mes = int(input("Ingrese el mes: "))
            anio = int(input("Ingrese el año: "))

            # Validar que el día exista en el mes y año indicados.
            import datetime
            datetime.date(anio, mes, dia)

            Fecha = dia, mes, anio
            return Fecha
        except ValueError:
            print("Fecha no válida. Verifique día, mes y año.")

#Verifica que los archivos .txt de las mesas exixtan y que si no exixten los cree.
def preparar_archivos():
    for nombre in archivos_prueba:
        try:
            if not os.path.exists(nombre):
                with open(nombre, "w", encoding="utf-8") as archivo:
                    archivo.write("ARCHIVO DE PEDIDOS - RESTAURANTE LAS FLORES\n")
                    archivo.write("=" * 45 + "\n")
        except PermissionError:
            print(f"No hay permisos para crear {nombre}.")
        except OSError as error:
            print(f"No se pudo preparar {nombre}: {error}")


def mostrar_menu():
    print("\n========== MENÚ ==========")
    for producto in menu:
        print(f"{producto[0]}. {producto[1]} - ${producto[2]:.2f}")


def buscar_producto(opcion):
    for producto in menu:
        if producto[0] == opcion:
            return producto
    return None

# Nos ayuda a que se ingresen solamente valores enteros y que este dentro del rango.
def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser como mínimo {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"El valor debe ser como máximo {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")


def guardar_pedido(numero_mesa, cantidad_personas, Fecha, pedidos_mesa,
                   subtotal_mesa, propina, total_mesa, modalidad):
    nombre_archivo = f"pedidos_mesa{numero_mesa}.txt"
    try:
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write("\nREGISTRO DE PEDIDO - RESTAURANTE LAS FLORES\n")
            archivo.write(f"Fecha (día, mes, año): {Fecha}\n")
            archivo.write(f"Mesa: {numero_mesa}\n")
            archivo.write(f"Personas: {cantidad_personas}\n")
            archivo.write(f"Modalidad de pago: {modalidad}\n")

            for pedido in pedidos_mesa:
                archivo.write(f"\nPersona {pedido['persona']}\n")
                for producto in pedido["productos"]:
                    archivo.write(
                        f"{producto['nombre']} | Precio: ${producto['precio']:.2f}"
                        f" | Cantidad: {producto['cantidad']}"
                        f" | Importe: ${producto['importe']:.2f}\n"
                    )
                archivo.write(f"Subtotal individual: ${pedido['subtotal']:.2f}\n")
                archivo.write(f"Propina individual: ${pedido['propina']:.2f}\n")
                archivo.write(f"Total individual: ${pedido['total']:.2f}\n")

            archivo.write(f"\nSubtotal de la mesa: ${subtotal_mesa:.2f}\n")
            archivo.write(f"Propina total: ${propina:.2f}\n")
            archivo.write(f"Total de la mesa: ${total_mesa:.2f}\n")
            archivo.write("-" * 45 + "\n")

        print(f"Pedido guardado correctamente en {nombre_archivo}.")
    except FileNotFoundError:
        print("No se encontró la ruta del archivo.")
    except PermissionError:
        print("No hay permisos para escribir en el archivo.")
    except OSError as error:
        print(f"No se pudo guardar el pedido: {error}")


def registro_pedido(Fecha):
    print("\n========== REGISTRO DE PEDIDO ==========")

    # Solo se permiten las mesas 1 al 5.
    numero_mesa = pedir_entero("Ingrese el número de mesa (1 al 5): ", 1, 5)
    cantidad_personas = pedir_entero("Ingrese la cantidad de personas: ", 1)

    pedidos_por_mesa = []
    subtotal_mesa = 0
# Conteo de cada persona en la mesa.
    for persona in range(1, cantidad_personas + 1):
        print(f"\n========== PERSONA {persona} ==========")
        productos_persona = []
        subtotal_persona = 0
# Ciclo para capturar los diferentes produntos que pida una persona.
        while True:
            mostrar_menu()
            opcion_producto = pedir_entero("Seleccione un producto (1 al 10): ", 1, 10)
            producto = buscar_producto(opcion_producto)
            cantidad = pedir_entero("Ingrese la cantidad: ", 1)

            importe = producto[2] * cantidad
            subtotal_persona += importe

            productos_persona.append({
                "nombre": producto[1],
                "precio": producto[2],
                "cantidad": cantidad,
                "importe": importe
            })

            print(f"Agregado: {producto[1]} x {cantidad} = ${importe:.2f}")
            print(f"Subtotal acumulado de la persona: ${subtotal_persona:.2f}")

            respuesta = input(
                "Desea agregar otro producto a esta misma cuenta (si/no): ").strip().lower()
            while respuesta not in ("si", "no"):
                respuesta = input('Responda "si" o "no": ').strip().lower()
            if respuesta == "no":
                break
# Almacena el pedido de la mesa.
        pedidos_por_mesa.append({
            "persona": persona,
            "productos": productos_persona,
            "subtotal": subtotal_persona,
            "propina": 0,
            "total": 0
        })
        subtotal_mesa += subtotal_persona
        print(f"Cuenta de la persona {persona}: ${subtotal_persona:.2f}")

    print("\n¿Cómo se pagará la cuenta?")
    print("1. Una sola cuenta para toda la mesa (propina del 5%)")
    print("2. Cada persona paga su cuenta (propina del 2.5% por persona)")
    modalidad_pago = pedir_entero("Seleccione 1 o 2: ", 1, 2)

    if modalidad_pago == 1:
        modalidad = "Cuenta por mesa (5%)"
        propina = round(subtotal_mesa * 0.05, 2)
        total_mesa = round(subtotal_mesa + propina, 2)

        # Se reparte la propina de mesa entre las personas solo para mostrarla.
        propina_base = propina / cantidad_personas
        propinas_individuales = [
            round(propina_base, 2) for _ in pedidos_por_mesa
        ]
        # Ajustar cualquier diferencia de centavos en la última persona.
        diferencia = round(propina - sum(propinas_individuales), 2)
        propinas_individuales[-1] = round(
            propinas_individuales[-1] + diferencia, 2
        )

    else:
        modalidad = "Cuentas separadas (2.5% por persona)"
        propinas_individuales = [
            round(pedido["subtotal"] * 0.025, 2)
            for pedido in pedidos_por_mesa
        ]
        propina = round(sum(propinas_individuales), 2)
        total_mesa = round(subtotal_mesa + propina, 2)

    print("\n========== RESUMEN DE CUENTAS ==========")
    for indice, pedido in enumerate(pedidos_por_mesa):
        pedido["propina"] = propinas_individuales[indice]
        pedido["total"] = round(
            pedido["subtotal"] + pedido["propina"], 2
        )

        print(f"\nPersona {pedido['persona']}:")
        for producto in pedido["productos"]:
            print(
                f"  {producto['nombre']} x {producto['cantidad']} "
                f"= ${producto['importe']:.2f}"
            )
        print(f"  Subtotal: ${pedido['subtotal']:.2f}")
        print(f"  Propina: ${pedido['propina']:.2f}")
        print(f"  Total individual: ${pedido['total']:.2f}")

    print("\n======================================")
    print(f"Mesa: {numero_mesa}")
    print(f"Fecha: {Fecha}")
    print(f"Modalidad: {modalidad}")
    print(f"Subtotal de la mesa: ${subtotal_mesa:.2f}")
    print(f"Propina total: ${propina:.2f}")
    print(f"TOTAL DE LA MESA: ${total_mesa:.2f}")
    print("======================================")

    respuesta_guardar = input(
        "Desea guardar este pedido (si/no): "
    ).strip().lower()
    if respuesta_guardar == "si":
        guardar_pedido(
            numero_mesa, cantidad_personas, Fecha, pedidos_por_mesa,
            subtotal_mesa, propina, total_mesa, modalidad
        )


def leer_archivo():
    print("\n========== ARCHIVOS DISPONIBLES ==========")
    for numero, nombre in enumerate(archivos_prueba, 1):
        print(f"{numero}. {nombre}")

    opcion = pedir_entero("Seleccione un archivo (1 al 5): ", 1, 5)
    nombre_archivo = archivos_prueba[opcion - 1]

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            print("\n" + archivo.read())
    except FileNotFoundError:
        print("El archivo no existe.")
    except PermissionError:
        print("No hay permisos para leer el archivo.")
    except OSError as error:
        print(f"Error al leer el archivo: {error}")


def anexar_archivo(Fecha):
    print("\n========== ANEXAR INFORMACIÓN ==========")
    for numero, nombre in enumerate(archivos_prueba, 1):
        print(f"{numero}. {nombre}")

    opcion = pedir_entero("Seleccione un archivo (1 al 5): ", 1, 5)
    nombre_archivo = archivos_prueba[opcion - 1]
    texto = input("Escriba la información que desea agregar: ")

    try:
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(f"\nFecha de modificación: {Fecha}\n")
            archivo.write(texto + "\n")
        print("Información agregada correctamente.")
    except FileNotFoundError:
        print("No se encontró el archivo.")
    except PermissionError:
        print("No hay permisos para modificar el archivo.")
    except OSError as error:
        print(f"Error al modificar el archivo: {error}")


def depuracion():
    print("\n Modo de depuración PDB activado.")
    pdb.set_trace()


def menu_principal(Fecha):
    opciones = [
        [1, "Registrar nuevo pedido"],
        [2, "Leer archivo de pedidos"],
        [3, "Anexar información a un archivo"],
        [4, "Preparar archivos de prueba"],
        [5, "Salir"]
    ]

    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        for opcion in opciones:
            print(f"{opcion[0]}. {opcion[1]}")

        seleccion = pedir_entero("Seleccione una opción: ", 1, 5)

        if seleccion == 1:
            registro_pedido(Fecha)
        elif seleccion == 2:
            leer_archivo()
        elif seleccion == 3:
            anexar_archivo(Fecha)
        elif seleccion == 4:
            preparar_archivos()
            print("Archivos preparados correctamente.")
        elif seleccion == 5:
            print("Gracias por utilizar el sistema.")
            break

        # Cambiar MODO_DEBUG a True para entrar a PDB tras una opción.
        if MODO_DEBUG:
            depuracion()

# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    print("==== SISTEMA DE PEDIDOS DEL RESTAURANTE ====")
    usuario = input("Ingrese su nombre: ").strip()
    if not usuario:
        usuario = "Usuario"

    bienvenida(usuario)
    pantalla()

    print("\nIngrese la fecha de operación.")
    Fecha = capturar_fecha()

    preparar_archivos()
    menu_principal(Fecha)

    print("\nSe finalizó el programa.")
