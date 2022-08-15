#Entradas
Nombre_cliente=str(input("Escriba el nombre del cliente: "))
Compra_realizada=int(input("Digite el valor de la compra: $"))
#Caja negra
if(Compra_realizada<50000):
    print("No es posible hacer descuento")
elif(Compra_realizada>=50000 and Compra_realizada<=100000):
    Descuento=Compra_realizada*0.05
    print("El descuento realizado a la compra es del 5%")
elif(Compra_realizada>=100000 and Compra_realizada<=700000):
    Descuento=Compra_realizada*0.11
    print("El descuento realizado a la compra es del 11%")
elif(Compra_realizada>=700000 and Compra_realizada<=1500000):
    Descuento=Compra_realizada*0.18
    print("El descuento realizado a la compra es del 18%")
elif(Compra_realizada>1500000):
    Descuento=Compra_realizada*0.25
    print("El descuento realizado a la compra es del 25%")
#Salidas
print("El valor de la compra realizada es de: $",Compra_realizada, "El monto total a pagar es de: $",Compra_realizada-Descuento, "El cliente que recibió el descuento aplicable es: ",Nombre_cliente)