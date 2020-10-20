def sqrt2():
    x = 2*(10**200) #x is assigned the integer equivalent of 2.0 with 100 zeros after the decimal place 200000...000 (100)
    y = (x + 1) // 2 # 2 #precision number
    while y < x: # algorithm terminates when the y is less than or equal to x
        x = y
        y = (x + 2*(10**200) // x) // 2
    answer = str(x)
    result = answer[:1]+'.'+answer[1:-1]+answer[-1:]
    return result


print(sqrt2())
