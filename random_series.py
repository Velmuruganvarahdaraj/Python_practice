def series(n):
    a= []
    c= 0
    for i in range(n):
        a.append(c)
        if i % 2 == 0:
            c+= 7  
        else:
            c+= 6  
    return a
num =int(input())
print(series(num))
