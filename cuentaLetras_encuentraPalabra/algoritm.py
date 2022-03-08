
# def cuentaLetras (string):
#     strin=[]
#     for j in string:
#         strin.append(j)
#     dicc={}
#     l = len(string)
#     pos = 0
#     while l>=0:
#         j=0
#         string[j:]
#         for i in string:
#             char=strin[pos]
#             count=1
#             if(i==char):
#                 count+=1
                
#         dicc[strin[pos]]=count

#         pos+=1
#         l-=1
#         j-=1    
    
#     return dicc

def cuentaLetras(palabra):
    dicc={}
    for letra in palabra:
        if letra in dicc:
            dicc[letra]+=1
        else:
            dicc[letra]=1
    # dicc['a'] = 10      si se añade un valor con mismo key , se sobreescribe en el dicc
    return dicc
    
print(cuentaLetras("hollaa"))



def encuentraPalabra(arreglo, palabra):
    count=0
    for i in arreglo:
        if(i==palabra):
            count+=1
    return count

print(encuentraPalabra(["hi", "hi","hola",'te',"tes","deste","te",'te'],'te'))

