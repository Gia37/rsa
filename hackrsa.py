# Autor: Gisela Arrieta Rivera
# 
# Problema 2
#
# Objetivo: Escriba una funcion (Python sugerido) que dada la clave publica de RSA y un mensaje compuesto de
#cuatro numeros codificados m 1 , m 2 , m 3 , m 4 en el rango 0-9 desencripte el mensaje formado por estos
#cuatro numeros n1 , n2 , n3 , n4 = hackrsa (e , N , m1 , m2 , m3 , m4 )
#
# Estrategia:
#############################################################################################################


# Funcion necesaria para hackrsa

# La funcion isprime encuentra si un numero dado es primo, aparecera  1 si es primo, o 0 si no lo es.

def isprime (k):

	for i in range (2, k):
		if k % i ==0:
			return 0
	return 1

# FUNCION HACKRSA

# informacion sobre esta funcion: dada la clave publica de RSA y un mensaje compuesto de cuatro numeros
# codificados en el rango 0-9 desencrpte el mensaje formado por estos cuatro numeros.

# Datos necesarios:

	# Llave publica: (e, N)
	# Llave privada: (d, N)
	# Numeros codificados: n1, n2, n3, n4
	# Mensaje codificado: m1, m2, m3, m4
	# p y q numeros primos que al multiplicarlos encontramos N
	# phi(N): cuya formula es phi(N) = (p-1) * (q-1)

## DESARROLLO DE LA FUNCION HACKRSA

