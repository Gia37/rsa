# Autor: Gisela Arrieta Rivera
# 
# Problema 2
#
# Objetivo: Escriba una funcion (Python sugerido) que dada la clave publica de RSA y un mensaje compuesto de
#cuatro numeros codificados m 1 , m 2 , m 3 , m 4 en el rango 0-9 desencripte el mensaje formado por estos
#cuatro numeros n1 , n2 , n3 , n4 = hackrsa (e , N , m1 , m2 , m3 , m4 )
#
# Estrategia: se crea primero la funcion isprime que nos servira de ayuda para la funcion hackrsa,
# luego se definen los datos necesarios y se procede a hallar los mismos.
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

# al multiplicar p y q nos debe dar como resultado N, siendo p y q dos numeros primos que seran de ayuda 
# para encontrar phi(N) que a su vez ayuda para encontrar el "e" de la llave publica y "d" de la privada
#
# para encontrar estos dos numeros se crean dos contadores p y q que vayan desde 2 hasta N 
#
# Utilizando la funcion isprime escogemos de las listas de p y q los que son primos y que al multiplicarlos
# dan como resultado a N.
#
# Ya que encontramos a N, se procede a encontrar phi(N) con la formula phi(N) = (p-1) * (q-1)
# en este caso no se coloca phi(N) sino phi_N ya que si se coloca phi(N) sale error al momento de ejecutar.
#


def hackrsa (e, N, n1, n2, n3, n4): 
	for p in range (2, N): 
		for q in range (2, N):
			if isprime(p) == 1 and isprime(q) == 1:
				if p * q == N:
					phi_N = (p-1) * (q-1)							
							

# se crea un range en el que "d" es un contador que va desde 0 hasta phi(n).
#
#Para desencriptar un mensaje codificado(n) se realiza la siguiente operacion: m = n^d % N.

	for d in range (0,phi_N):
		if e*d % phi_N ==1:
			m1 = n1**d % N
			m2 = n2**d % N
			m3 = n3**d % N
			m4 = n4**d % N

#Le asigno a abc, una lista que va desde a hasta z, que son las 26 letras del abecedario:
# abc = list(map(chr, range(97, 123)))--->[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
#
# como la lista empieza desde la posicion 0 de modo que abc[0]=a, entonces abc[m-1]=m, 
# ya que si dejamos abc[m]  entonces abc[1]=b.
#
# Y por ultimo se imprimen los numeros desencriptados.

def hackrsa (e , N , m1 , m2 , m3 , m4 ):
	abc = list(map(chr, range(97, 123)))

	print m1, m2, m3, m4	
	print abc[m1-1], abc[m2-1], abc[m3-1], abc[m4-1]

print hackrsa (12, 21, 7, 9, 19, 5)

