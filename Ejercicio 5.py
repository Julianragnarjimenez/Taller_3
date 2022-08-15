#Entradas
Sueldo=int(input("Digite el valor del sueldo devengado: $"))
Ventas_Dep_1=int(input("Digite el valor de las ventas del departamento 1: $"))
Ventas_Dep_2=int(input("Digite el valor de las ventas del departamento 2: $"))
Ventas_Dep_3=int(input("Digite el valor de las ventas del departamento 3: $"))
#Caja negra
Venta_total=Ventas_Dep_1+Ventas_Dep_2+Ventas_Dep_3
Comisión=Venta_total*0.33
if(Ventas_Dep_1>Comisión):
    Sueldo_Dep_1=Sueldo+Sueldo*0.20
else:
    Sueldo_Dep_1=Sueldo
if(Ventas_Dep_2>Comisión):
    Sueldo_Dep_2=Sueldo+Sueldo*0.20
else:
    Sueldo_Dep_2=Sueldo
if(Ventas_Dep_3>Comisión):
    Sueldo_Dep_3=Sueldo+Sueldo*0.20
else:
    Sueldo_Dep_3=Sueldo
#Salidas
print("Las ventas del departamento 1 son: $",Sueldo_Dep_1)
print("Las ventas del departamento 2 son: $",Sueldo_Dep_2)
print("Las ventas del departamento 3 son: $",Sueldo_Dep_3)