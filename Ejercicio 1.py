#Entradas
Cantidad=int(input("Escriba la cantidad invertida: $"))
Tasa=float(input("Escriba la tasa de interes: "))
#Caja negra
Intereses=Cantidad*Tasa
if(Intereses>100000):
#Salida
    print("El interes obtenido es: ",Intereses, "supera los 100000")
else:
#Salida
    print("El interes obtenido es: ",Intereses, "no supera los 100000")
#Salida
print("El monto total existente en la cuenta es de: ",Cantidad+Intereses)