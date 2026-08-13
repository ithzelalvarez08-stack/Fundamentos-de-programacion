
print("Bienvenido, este programa te ayudara a encontrar tu IMC")
nombre=(input("Ingresa tu nombre: "))
p=float(input("¿Cual es tu peso? "))
a=float(input("¿Cual es tu altura? "))

imc= str(p/(a**2))

print("Tu indice de masa corporal ", nombre,"es: ", imc)
