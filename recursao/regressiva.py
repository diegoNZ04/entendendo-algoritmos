def regressiva(i):
    print(i)
    # caso-base
    if i <= 0:
        return
    # caso recursivo
    else:
        regressiva(i-1)
    
regressiva(10) # => 10... 9... 8... 7...