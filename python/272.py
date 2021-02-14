bandera = 0
while True:
    #Controlamos el error dado el caso que no dijite nada
	try :
		cadena1 = input()
	except EOFError:
		break	
	
	cadena2 = []
	for i in cadena1:
		if i == "\"":
			if bandera == 0:
				cadena2.append("``")
				bandera = 1
			else:
				cadena2.append("''")
				bandera = 0
		else:
			cadena2.append(i)
	print("".join(cadena2))
    
