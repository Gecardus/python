numeropayasos=int(input("Introduce el numero de payasos vendidos: "))
numeromuñecas=int(input("Introduce el numero de muñecas vendidas: "))
Pesopayaso=int(input("Introduce el peso de cada payaso en gramos: "))
Pesomuñeca=int(input("Introduce el peso de cada muñeca en gramos: "))
Pesopayasos= (Pesopayaso*numeropayasos)
Pesomuñecas=(Pesomuñeca* numeromuñecas)
Pesototal=  Pesopayasos+Pesomuñecas
print("El peso de los payasos es " + str(Pesopayasos) + " gramos i el peso de las muñecas es " + str(Pesomuñecas) + " gramos i el peso total es " + str(Pesototal) + " gramos")