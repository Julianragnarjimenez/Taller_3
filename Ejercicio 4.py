#Entradas
Número_piezas=int(input("Digite el número de piezas: "))
Costo_por_pieza=int(input("Digite el valor por cada pieza: $"))
#Caja negra
Precio_total=Número_piezas*Costo_por_pieza
if(Precio_total>5000000):
    Inversión=Precio_total*0.55
    Prestamo=Precio_total*0.30
    Crédito=Precio_total*0.15
else:
    Inversión=Precio_total*0.70
    Crédito=Precio_total*0.30
Intereses=Crédito*0.20
#Salidas
print("La cantidad a invertir es de: $",round(Inversión,1))
print("La cantidad del prestamo es de: $",Prestamo)
print("La cantidad del crédito es de: $",Crédito)
print("El interes es de: ",Intereses)