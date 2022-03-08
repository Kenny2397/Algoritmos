def palindromo(palabra):
    arr=[]
    i1 = len(palabra)/2
    for i in palabra:
        arr.append(i)
    if len(palabra)%2==0:
        if(arr[0:i1]==arr[i1:len(palabra-1)]):
            return True
        else:
            return False
    else:
        if(arr[:(len(palabra)+1)/2-1] == arr[(len(palabra)+1)/2:]):
            return True
        else:
            return False

print(palindromo("anna"))

