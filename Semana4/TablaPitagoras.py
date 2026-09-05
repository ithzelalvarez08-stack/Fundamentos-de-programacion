# tabla de pitagoras
d = 11
matriz=[]

def llenar_matriz(matriz):
      for i in range(1,11):
        fila=[]
        for c in range(1,11):
             resultado = 0
             for c in range(c):
                resultado = resultado + i
             fila.append(resultado)
        matriz.append(fila)


def multiplicacion(factor1, factor2,matriz):
      return matriz[factor1-1][factor2-1]

llenar_matriz(matriz)


print("     ", end="")
for c in range(1,11):
    print(f"{c:2}", end=" ")
print()

for i in range(1,11):
    print(f"{i:2}   ", end="")
    for c in range(1,11):
        print(f"{matriz[i-1][c-1]:2}", end=" ")
    print()

print("                                              ")

factor1=int(input("Ingrese el primer factor de 1 a 10: "))
factor2=int(input("Ingrese el segundo factor de 1 a 10: "))

resultado = multiplicacion(factor1, factor2,matriz)
print(f"El resultado es: {resultado} ")