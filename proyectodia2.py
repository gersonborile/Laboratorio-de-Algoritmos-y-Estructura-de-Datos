nombre= input(" Ingrese su nombre")
cant_vendido= float(input(" Ingrese la cantidad de sus ventas este mes"))
comision= cant_vendido*13/100
round(comision,2)
print(f"El monto que le corresponde a {nombre} por sus comisiones es de {comision}")