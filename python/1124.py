while True:
	try:
		cadena = input()
	except EOFError:
		break
	
	print(cadena)