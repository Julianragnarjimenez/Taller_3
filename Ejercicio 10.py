#Entradas
Sueldo_bruto=int(input("Introduzca el sueldo devengado por el empleado: $"))
Categoria=int(input("Digite la categoria a la que pertenece el empleado: "))
#Caja negra
if(Sueldo_bruto>=5000000):
    Aumento=Sueldo_bruto*0.10
    print("La categoria del trabajador es: ",Categoria)
elif(Sueldo_bruto>=4300000):
    Aumento=Sueldo_bruto*0.15
    print("La categoria del trabajador es: ",Categoria)
elif(Sueldo_bruto>=3600000):
    Aumento=Sueldo_bruto*0.20
    print("La categoria del trabajador es: ",Categoria)
elif(Sueldo_bruto>=2000000):
    Aumento=Sueldo_bruto*0.40
    print("La categoria del trabajador es: ",Categoria)
elif(Sueldo_bruto>=900000):
    Aumento=Sueldo_bruto*0.60
    print("La categoria del trabajador es: ",Categoria)
#Salidas
print("El nuevo saldo bruto del trabajador es de: $",Sueldo_bruto+Aumento)