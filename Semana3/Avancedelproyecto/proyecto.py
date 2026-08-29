
print("======================================")
print(" SISTEMA DE PEDIDOS DEL RESTAURANTE")
print("======================================")

numero_mesa = int(input("Ingrese el número de mesa: "))

cantidad_personas = int(input("Ingrese la cantidad de personas en la mesa: "))

while cantidad_personas <= 0:

    print("La cantidad debe ser mayor que cero.")
    cantidad_personas = int(input("Ingrese nuevamente la cantidad: "))
for persona in range (1, cantidad_personas +1):

    print("\n======================================")
    print("PERSONA", persona)
    print("======================================")
    
    respuesta = "si"

    while respuesta == "si":
         
         print("           MENU       ")
         print("1. Ensalada Cesar - $100")
         print("2. Enchiladas Rojas - $150")
         print("3. Pasta - $100")
         print("4. Chilaquiles Verdes - $100")
         print("5. Aguachile - $200")
         print("========== POSTRES ==========")
         print("6. Pastel de Tres Leches - $50")
         print("7. Helado Napolitano - $80")
         print("========== BEBIDAS ==========")
         print("8. Agua del Dia - $40")
         print("9. Cafe - $35")
         print( "10. Refresco - $40")

         opcion_producto =int(input("Seleccione un producto:"))

         while opcion_producto <1 or opcion_producto > 10:
            print("producto no valido")
            opcion_producto =int(input("Seleccione un producto del 1 al 10: "))

         cantidad = int(input("Ingrese la cantidad: "))

         while cantidad <= 0:
          print("La cantidad debe ser mayor a 0")
          cantidad = int(input("Ingrese la cantidad nuevamente: "))
         print("Producto: ",opcion_producto)
         print("Cantidad: ",cantidad)
         respuesta=input("Desea agreagar algun otro produnto: ")
    print("se termino el pedido de ", persona)

print("Se fializo el registro")
        
          
