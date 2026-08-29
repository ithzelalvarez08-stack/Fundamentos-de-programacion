Algoritmo Sistema_de_restaurante
    Definir numero_mesa, numero_personas Como Entero
    Definir persona, i, opcion_producto Como Entero
    Definir cantidad, total_de_pedidos Como Entero
    Definir numero_pedido, nueva_cantidad Como Entero
	
    Definir respuesta Como Caracter
	
    Definir precio, importe Como Real
    Definir subtotal_mesa, propina_general Como Real
    Definir propina_por_persona, total_general Como Real
    Definir subtotal_persona, total_persona Como Real
	
    Dimension personas[100]
    Dimension productos[100]
    Dimension precios[100]
    Dimension cantidades[100]
    Dimension importes[100]
	
    subtotal_mesa <- 0
    total_de_pedidos <- 0
	
    Escribir " SISTEMA DE PEDIDOS DEL RESTAURANTE"
    Escribir "Ingrese el numero de mesa:"
    Leer numero_mesa
    Escribir "Ingrese la cantidad de personas:"
    Leer numero_personas
    Mientras numero_personas <= 0 Hacer
        Escribir "La cantidad debe ser mayor que cero."
        Leer numero_personas
    FinMientras
    Para persona <- 1 Hasta numero_personas Hacer
        Escribir "PERSONA ", persona
        respuesta <- "SI"
        Mientras respuesta = "SI" O respuesta = "si" Hacer
            Escribir "========== MENU =========="
            Escribir "1. Ensalada Cesar - $100"
            Escribir "2. Enchiladas Rojas - $150"
            Escribir "3. Pasta - $100"
            Escribir "4. Chilaquiles Verdes - $100"
            Escribir "5. Aguachile - $200"
            Escribir "========== POSTRES =========="
            Escribir "6. Pastel de Tres Leches - $50"
            Escribir "7. Helado Napolitano - $80"
            Escribir "========== BEBIDAS =========="
            Escribir "8. Agua del Dia - $40"
            Escribir "9. Cafe - $35"
            Escribir "10. Refresco - $40"
            Escribir "Seleccione un producto:"
            Leer opcion_producto
            Mientras opcion_producto < 1 O opcion_producto > 10 Hacer
                Escribir "Producto no valido."
                Escribir "Seleccione un producto del 1 al 10:"
                Leer opcion_producto
            FinMientras
            Escribir "Ingrese la cantidad:"
            Leer cantidad
            Mientras cantidad <= 0 Hacer
                Escribir "La cantidad debe ser mayor que cero."
                Leer cantidad
            FinMientras
            total_de_pedidos <- total_de_pedidos + 1
            personas[total_de_pedidos] <- persona
            cantidades[total_de_pedidos] <- cantidad
            Segun opcion_producto Hacer
                1:
                    productos[total_de_pedidos] <- "Ensalada Cesar"
                    precios[total_de_pedidos] <- 100
                2:
                    productos[total_de_pedidos] <- "Enchiladas Rojas"
                    precios[total_de_pedidos] <- 150
                3:
                    productos[total_de_pedidos] <- "Pasta"
                    precios[total_de_pedidos] <- 100
                4:
                    productos[total_de_pedidos] <- "Chilaquiles Verdes"
                    precios[total_de_pedidos] <- 100
                5:
                    productos[total_de_pedidos] <- "Aguachile"
                    precios[total_de_pedidos] <- 200
                6:
                    productos[total_de_pedidos] <- "Pastel de Tres Leches"
                    precios[total_de_pedidos] <- 50
                7:
                    productos[total_de_pedidos] <- "Helado Napolitano"
                    precios[total_de_pedidos] <- 80
                8:
                    productos[total_de_pedidos] <- "Agua del Dia"
                    precios[total_de_pedidos] <- 40
                9:
                    productos[total_de_pedidos] <- "Cafe"
                    precios[total_de_pedidos] <- 35
                10:
                    productos[total_de_pedidos] <- "Refresco"
                    precios[total_de_pedidos] <- 40
            FinSegun
            importe <- precios[total_de_pedidos] * cantidades[total_de_pedidos]
            importes[total_de_pedidos] <- importe
            Escribir "Pedido registrado"
            Escribir "¿Desea agregar otro producto? SI/NO"
            Leer respuesta
        FinMientras
        Escribir "PEDIDOS DE LA PERSONA ", persona
        Para i <- 1 Hasta total_de_pedidos Hacer
            Si personas[i] = persona Entonces
				Escribir "Pedido numero: ", i
                Escribir "Producto: ", productos[i]
                Escribir "Cantidad: ", cantidades[i]
                Escribir "Importe: $", importes[i]
            FinSi
        FinPara
        Escribir "¿Desea modificar algun pedido de esta persona? SI/NO"
        Leer respuesta
        Mientras respuesta = "SI" O respuesta = "si" Hacer
            Escribir "Ingrese el numero del pedido que desea modificar:"
            Leer numero_pedido
            Mientras numero_pedido < 1 O numero_pedido > total_de_pedidos O personas[numero_pedido] <> persona Hacer
                Escribir "Ese pedido no pertenece a esta persona."
                Escribir "Ingrese otro numero de pedido:"
                Leer numero_pedido
            FinMientras
            Escribir "========== MENU =========="
            Escribir "1. Ensalada Cesar - $100"
            Escribir "2. Enchiladas Rojas - $150"
            Escribir "3. Pasta - $100"
            Escribir "4. Chilaquiles Verdes - $100"
            Escribir "5. Aguachile - $200"
            Escribir "6. Pastel de Tres Leches - $50"
            Escribir "7. Helado Napolitano - $80"
            Escribir "8. Agua del Dia - $40"
            Escribir "9. Cafe - $35"
            Escribir "10. Refresco - $40"
            Escribir "Seleccione el nuevo producto:"
            Leer opcion_producto
            Mientras opcion_producto < 1 O opcion_producto > 10 Hacer
                Escribir "Producto no valido."
                Leer opcion_producto
            FinMientras
            Escribir "Ingrese la nueva cantidad:"
            Leer nueva_cantidad
            Mientras nueva_cantidad <= 0 Hacer
                Escribir "La cantidad debe ser mayor que cero."
                Leer nueva_cantidad
            FinMientras
            Segun opcion_producto Hacer
                1:
                    productos[numero_pedido] <- "Ensalada Cesar"
                    precios[numero_pedido] <- 100
                2:
                    productos[numero_pedido] <- "Enchiladas Rojas"
                    precios[numero_pedido] <- 150
                3:
                    productos[numero_pedido] <- "Pasta"
                    precios[numero_pedido] <- 100	
                4:
                    productos[numero_pedido] <- "Chilaquiles Verdes"
                    precios[numero_pedido] <- 100
                5:
                    productos[numero_pedido] <- "Aguachile"
                    precios[numero_pedido] <- 200
                6:
                    productos[numero_pedido] <- "Pastel de Tres Leches"
                    precios[numero_pedido] <- 50
                7:
                    productos[numero_pedido] <- "Helado Napolitano"
                    precios[numero_pedido] <- 80
                8:
                    productos[numero_pedido] <- "Agua del Dia"
                    precios[numero_pedido] <- 40
                9:
                    productos[numero_pedido] <- "Cafe"
                    precios[numero_pedido] <- 35
                10:
                    productos[numero_pedido] <- "Refresco"
                    precios[numero_pedido] <- 40
            FinSegun
            cantidades[numero_pedido] <- nueva_cantidad
            importes[numero_pedido] <- precios[numero_pedido] * cantidades[numero_pedido]
            Escribir "Pedido modificado correctamente."
            Escribir "¿Desea modificar otro pedido? SI/NO"
            Leer respuesta
        FinMientras
    FinPara
    subtotal_mesa <- 0
    Para i <- 1 Hasta total_de_pedidos Hacer
        subtotal_mesa <- subtotal_mesa + importes[i]
    FinPara
    propina_general <- subtotal_mesa * 0.05
    propina_por_persona <- propina_general / numero_personas
    total_general <- subtotal_mesa + propina_general
    Escribir "RESUMEN FINAL POR PERSONA"
    Para persona <- 1 Hasta numero_personas Hacer
        subtotal_persona <- 0
        Escribir "PERSONA ", persona
        Para i <- 1 Hasta total_de_pedidos Hacer
            Si personas[i] = persona Entonces
                Escribir "Producto: ", productos[i]
                Escribir "Cantidad: ", cantidades[i]
                Escribir "Importe: $", importes[i]
                subtotal_persona <- subtotal_persona + importes[i]
            FinSi
        FinPara
        total_persona <- subtotal_persona + propina_por_persona
        Escribir "Subtotal personal: $", subtotal_persona
        Escribir "Parte de la propina general: $", propina_por_persona
        Escribir "TOTAL PERSONAL: $", total_persona
    FinPara
	
    Escribir "CUENTA TOTAL DE LA MESA"
    Escribir "Mesa: ", numero_mesa
    Escribir "Numero de personas: ", numero_personas
    Escribir "Subtotal general: $", subtotal_mesa
    Escribir "Propina total (5%): $", propina_general
    Escribir "Propina por persona: $", propina_por_persona
    Escribir "TOTAL A PAGAR: $", total_general

FinAlgoritmo