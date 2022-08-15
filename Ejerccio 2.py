#Entradas
Sueldo=int(input("Escriba el sueldo del trabajador: $"))
#Caja negra
Aumento=""
if(Sueldo<900000):
    Aumento=Sueldo*0.15
else:
    Aumento=Sueldo*0.12
#Salidas
print("El nuevo saldo del trabajador es: $",Sueldo+Aumento)