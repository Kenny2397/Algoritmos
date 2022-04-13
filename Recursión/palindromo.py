def palindromo(text):
    if len(text) == 1 or len(text)==0:
        return True
    elif text[0] == text[-1]:
        # print(text[1:-1])
        return palindromo(text[1:-1])
    else:
        return False
    
print(palindromo('bav4nab'))