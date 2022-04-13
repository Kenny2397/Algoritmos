def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos==1:
        return 1
    else:
        return fibonacci(pos-1)+fibonacci(pos-2)

pos=10
print(fibonacci(pos))
print("=============")
for i in range(pos+1):
    print(str(i) +"° - "+str(fibonacci(i)))
    
# =================================================
