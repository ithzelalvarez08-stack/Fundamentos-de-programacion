precio_por_niño_menor_3 = 0.0
precio_menor_edad = 30.0      # ESTE VALOR ES PAR NIÑOS DE 3 A 17 AÑOS
precio_mayor_edad = 45.0      # MAYORES DE 18 AÑOS

#DESCUENTOS
descuento_adulto = 0.12
descuento_profesor = 0.10
descuento_estudiante = 0.10
descuento_ninguno = 0.0
total=0.0
descuento=0.0
print("===============================================================================")
print("=================== SISTEMA DE COBRO, MUSEO DE ANTROPOLIGIA ===================")
print("===============================================================================")
#TABLA DE DESCUENTOS
print("                                                ")
print("======== TABLA DE DATOS SOBRE DESCUENTOS =======")
print("                                                ")
print("|        PERSONAS          | PRECIO |")
print("|NIÑOS MENORES DE 3 AÑOS   |  $0.0  |")
print("|PERSONAS DE 3 A 17 AÑOS   |  $30.0 |")
print("|PERSONAS MAYORES DE EDAD  |  $45.0 |")
print("                                                ")
print("                                                ")
t_visitantes= int(input("INGRESE LA CANTIDAD DE VISITANTES: "))

for i in range(1,t_visitantes +1):
    print(f"\n ============== Visitante {i}  ===============")

    edad=int(input("Ingrese la edad del visitante: "))
    #ELECCION DEL PRECIO SEGUN LA EDAD
    if edad <3:
        precio_inicial = precio_por_niño_menor_3
    elif  edad >=3 and edad <=17:
        precio_inicial = precio_menor_edad
    else:
        precio_inicial = precio_mayor_edad

    #ELECCION SOBRE EL TIPO DE VISITANTE

    visitante= input("SELECCIONE EL TIPO DE VISITANTE (A)ADULTO MAYOR, (B)PROFESOR, (C)ESTUDIANTE ")
    # DESCUENTOS POR PERSONA (APLICA SOLO UNO POR PERSONA)
    if (visitante in ["adulto mayor", "a"]):
        descuento = descuento_adulto
    elif (visitante in ( "profesor", "b")):
        descuento = descuento_profesor
    elif (visitante in ( "estudiante", "c")):
        descuento = descuento_estudiante
    else:
        descuento == descuento_ninguno

    descuento_final = (precio_inicial * descuento)
    sub_total = (precio_inicial - descuento_final)
    total += sub_total


    print(f"Preccio Inicial:  ${precio_inicial:.2f}")
    print(f"Descuento aplicado: ${descuento:.2f}({int(descuento * 100)}%)")
    

print(f"TOTAL A PAGAR POR TODOS LOS VISITANTES: ${total:.2f}")
