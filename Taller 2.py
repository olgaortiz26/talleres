#TALLER 2 - EJERCICIOS DE ALGORITMIA ESTRUCTURA CONDICIONAL
#1. Leer dos (2) números y los imprima en forma ascendente.
num1=int(input('Indique el numero 1: '))
num2= int(input('Indique el numero 2: '))
if num1 > num2:
    print('el orden ascendete de los numeros es: ', num2, "y", num1 )
else:
    print('El orden ascendente de los numeros es: ', num1, "y", num2)

##Ejercicio 2

numero1= int(input('Ingrese un numero a comparar: '))


if numero1==1 and numero1==2 and numero1== 3 and numero1==4 and numero1==5  and numero1==6 and numero1==7 and numero==8 and numero1==9 and numero1==10:
    print('El numero que ingresaste: ', numero1, 'esta entre el rango de 1 a 10')
elif numero1!=1 and numero1!= 3 and numero1!=5  and numero1!=7  and numero1!=9:
    print('El numero que ingresaste: ', numero1, 'es un numero par')

elif numero1!=2 and numero1!=4 and numero1!=6 and numero1!=8 and numero1!=10:
    print('el numero que ingresaste: ', numero1, 'es un numero impar')
else: 
    print('El numero que ingresaste no esta entre el rango 1 a 10')    
#------------------------------------------------------------------------------------------------------------------------------------
##4 Ejercicio 4

llamada= int(input('Cuanto duro tu llamada en minutos: '))
if llamada<=3:
    print('El costo de tu llamada fue: ', llamada*200,'pesos')
else:
    print('El costo de los minutos adicionales es: ', (llamada-3)*100, 'pesos.', 'El total de la llamada fue: ', ((3*200)+(llamada-3)*100), 'pesos')

#Ejercicio 5
N= int(input('Cuantos conejos tienes: '))
C1= int(input('Ingrese la cantidad de conejos blancos que tienes: '))
C2= int(input('Ingrese la cantidad de conejos negros que tienes: '))

if (C1+C2>N) or (C1 or C2)>N:
    print("Ingresa un valor valido para el total de los conejos")
else: 
    X= int(input('Ingrese la cantidad de conejos negros que quieres vender: '))
    Y= int(input('Ingrese la cantidad de conejos blancos que quieres vender: '))
    P1=int(input('Indique el precio en venta de los conejos blancos: '))
    P2= int(input('Indique precio de los conejos negros: '))
    TP1Y=(P1*Y)
    TP2X=P2*X


    print('La cantidad de conejos negros vendida es ', X, 'y la cantidad de conejos blancos vendida es: ', Y)

    print('El precio total en venta de los conejos blancos y negros es: ', (TP1Y+TP2X)) 

    if TP1Y>TP2X:
        print('Los conejos que mas se vendieron fueron los blancos con un total de ', TP1Y) 
    else: 
        print('La cantidad de conejos que mas se vendieron fueron los negros con un total de ', TP2X)
#--------------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 6 
""" #6. Diseñe un algoritmo que permita calcular la nota definitiva para los estudiantes, determinadas sobre las siguientes condiciones:
#• NOTA PREVIOS será el promedio de los previos por el 60%. Cada estudiante tendrá 3 evaluaciones.
#• NOTA TRABAJOS será el promedio de los trabajos por el 40%. Cada estudiante
presentara 2 trabajos.
• NOTA FINAL será la suma de la nota de los previos y nota de los trabajos.
• Nota mínima 1,0 nota máxima: 5,0 """

previo1=float(input('Ingrese la nota del previo numero 1:  '))
previo2=float(input('Ingrese la nota del previo numero 2:  '))
previo3=float(input('Ingrese la nota del previo numero 3:  '))
notaprevio= float((((previo1+previo2+previo3)/3)*0.60))
print('el total de los previos es: ', notaprevio)
trabajo1=float(input('Indique la nota del trabajo 1: '))
trabajo2=float(input('Indique la nota del trabajo 2: '))
notatrabajos= float(((trabajo1+trabajo2)/2)*0.40)
print('el total del trabajo final es: ', notatrabajos)
notafinal=notaprevio + notatrabajos
print('La notal final es: ', notafinal)
if 1<=notafinal<=5:
    print('Aprobaste')
else: 
    print('Reprobaste')

##Ejercicio7
""" ##7. Hacer un algoritmo que imprima el nombre de un artículo, clave, precio original, 
cantidad y su precio con descuento. El descuento lo hace en base a la clave, si la
clave es 1 el descuento es del 10% y si la clave es 2 el descuento es del 20% (solo
existen dos claves). """ 

articulo=input('Ingrese el nombre del articulo: ')
clave= float(input('Ingrese el numero de clave del articulo')) 
preciooriginal= float(input('Ingrese el precio original del articulo: '))
cantidadarticulos=float(input('Ingrese la cantidad de articul: '))
preciocondescuento1= cantidadarticulos*preciooriginal*1.10
preciocondescuento2= cantidadarticulos*preciooriginal*1.20

if clave==1:
    print('El precio del articulo con descuento es: ', (preciocondescuento1) )
    print('El articulo ', articulo, 'con clave ', clave, 'precio original de ', preciooriginal, 'cantidad ', cantidadarticulos, 'y su precio con descuento es ', preciocondescuento1 )
else:
    print('El precio del articulo con descuento es: ', (preciocondescuento2))
    print('El articulo ', articulo, 'con clave ', clave, 'precio original de ', preciooriginal, 'cantidad ', cantidadarticulos, 'y su precio con descuento es ', preciocondescuento2 )


#Ejercicio 8
presupuesto_anual= float(input('Ingrese el presupuesto anual: '))
porcentaje_psiquiatria= float(input('Ingrese el presupuesto asignado a psiquiatría: '))
porcentaje_pediatria= float(input('Ingrese el presupuesto asignado a pediatría: '))
porcentaje_traumatologia= float(input('Ingrese el presupuesto asignado a traumatología: '))
presupuesto_psquiatria= presupuesto_anual*(porcentaje_psiquiatria/100)
presupuesto_pediatria= presupuesto_anual*(porcentaje_pediatria/100)
presupuesto_traumatologia= presupuesto_anual*(porcentaje_traumatologia/100)
porcentaje_total_areas= (porcentaje_psiquiatria+porcentaje_pediatria+porcentaje_traumatologia)
if porcentaje_total_areas !=100:
    print('El porcentaje no es el 100%')
else: 
    ('El porcentaje de las areas es el 100%')

#------------------------------------------------------------------------------------------------------------------------------------------
""" tiquete_ida= float(input('Ingrese el precio del tiquete de ida: '))
tiquete_vuelta= float(input('Ingrese el valor del tiquete de vuelta: ')) """
numero_dias=int(input('cual es la cantidad de dias de estancia que tendrás?: '))
distancia= float(input('Ingresa la cantidad de recorrido de tu viaje:  '))
tiquete= distancia*2.5
if numero_dias>= 7 and distancia>800:
    print('el precio de tu tiquete de ida y vuelta es: ', tiquete*0.30)
else: 
    if numero_dias>=7 and distancia<800: 
        print('El precio de tu tiquete de ida y vuelta es: ', tiquete+(distancia*2.5), 'dolares')
    else:
        print('el precio total de tu tiquete es: ', (distancia*2.5), 'dolares')



#comentario