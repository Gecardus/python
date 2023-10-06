inversion=float(input("Introduce el capital a invertir: "))
interes=float(input("Introduce el interes del banco anualmente en porcentaje: "))
año=int(input("Introduce numero de años: "))
Interesporcentual=interes/100
Capital=inversion - (inversion*Interesporcentual)*año
print("El capital obtenido es " + str(Capital))