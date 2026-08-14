mxn=float(input("Escriba la cantidad de pesos mexicanos : "))

cambiousd=float(input("Tipo de cambio USD: "))
cambioeur=float(input("Tipo de cambio EUR: "))
u= (mxn / cambiousd)
e= (mxn / cambioeur)

print(mxn,"equivalen a:")
print("En USD: ",u)
print("En EUR: ",e)
