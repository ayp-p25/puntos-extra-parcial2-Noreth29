# Codifica aquí tu programa
entrada=input("Escriba un número: ")
numero= int(entrada)
contador= 0

for dato in entrada:
    if dato != "0":
        if numero % int(dato) == 0:
            contador += 1

print(contador)

#3 errores= int(entrada), dato != "0" y if numero % int (dato).