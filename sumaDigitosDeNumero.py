def SumaDigitos():
    numero=input("ingrese numero: ")
    sum=0
    for i in numero:
        sum+=int(i)
    print(sum)    
    
SumaDigitos()

#
# print(10/4,10//4)  # //redondea hacia abajo
#

# 6%2:
# 6/2 = cociente:3 + resto: 0

# 6%4:
# 6/4= cociente:1 +resto :2

# el modulo(%) regresa el resto 
# la division(/) regresa el cociente