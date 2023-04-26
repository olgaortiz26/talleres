""" 1. Resuelva los siguientes ejercicios


a) 40 + 2 * 7 ^ 2
b) 3+ (2+5)*1+ (3-2*3)
c) 16 - 8 * (10 - (5 + 4))
d) (5+3*2)-(7*2)*(3+ (2*3-1))
e) (24+220)/3*2
f) (6/3*2)-(7*2)+ (2*(3+ (2/3-1)*4)) """

#EJERCICIO 1

a=40 
b=2
c=7
d=3
e=5
f=1
g=16
h=8
i=10
j=4
k=24
l=220
m=6

resultado1= int(a+((b*c)**b))
print('El primer resultado es ', resultado1)
resultado2= int(d+((b+e)*f)+(d-(b*d)))
print("El segundo resultado es ", resultado2)
resultado3=(g-(h*(i-(e+j))))
print('El tercer resultado es ', resultado3)
resultado4=((e+(d*b)-((c*b)*(d+((b*d)-f)))))
print('El cuarto resultado es ', resultado4)
resultado5=((k+l)/(b*d))
print('El quinto resultado es', resultado5)
resultado6=(((m/d)-(c*b))+(b*(d+(((b/d)-f)*j))))
print('El sexto resultado es ', resultado6)


