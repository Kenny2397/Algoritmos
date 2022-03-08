
def pageCount(n,p):
    #Abre de frente
    count_frente=1
    count_turned=0
    if(n>p):
        while(p>count_frente):
            count_frente+=2
            count_turned+=1
            
    #Abre de atras
    count_atras = 1
    count_turned = 0
    return count_turned
print(pageCount(5,2))