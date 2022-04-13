def conteo_regresivo(num):
    if num>0:
        print(num)
        conteo_regresivo(num-1)
    
conteo_regresivo(10)

def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)


print(factorial(5))

def reverse(text):
    if len(text) == 1:
        return text
    else:
        return text[len(text)-1]+reverse(text[:-1])
    
print(reverse('Hola'))
