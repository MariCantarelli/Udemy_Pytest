def contador(maximo): 
    n = 0 
    while n < maximo:
        yield n
        n += 1

# usando o gerador: 
    for i in contador(5):
        print(i)