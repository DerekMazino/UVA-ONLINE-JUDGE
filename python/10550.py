def conversion(numero):
        return int((360*numero)/40)
while True:
    linea = input().split(' ')
    if linea[0]=='0' and linea[1]=='0' and linea[2]=='0' and linea[3]=='0':
        break
    linea = [int(i) for i in linea]
    n1, n2, n3 ,n4 = linea
    #Paso 1
    total = 2*conversion(40)
    #Paso 2
    if n1 > n2:
        total += conversion(n1)-conversion(n2)
    else:
        total += conversion(n1) + conversion(40) - conversion(n2)
    #Paso 3
    total += conversion(40)
    #Paso 4
    if n2 > n3:
        total += conversion(n3) + conversion(40) - conversion(n2)
    else:
        total += conversion(n3) - conversion(n2)
    # Paso 5
    if n3 > n4:
        total += conversion(n3) - conversion(n4)
    else:
        total += conversion(n3) + conversion(40) - conversion(n4)
    print(total)

    