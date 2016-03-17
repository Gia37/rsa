# Autor: Gisela Arrieta Rivera
# 
# Problema 1
#
# Objetivo: Escriba una funcion (Python sugerido) que dados dos numeros primos p y q 
# genere las llaves publica y privada del algoritmo RSA: e , d , N = myrsa (p , q )
#
# Estrategia: inicialmente se anaden cuatro funciones que mas adelante seran necesarias para una quinta funcion
# que es la funcion que dados dos numeros primos genere las llaves publica y privada del algoritmo RSA.
#################################################################################################################

# Funciones necesarias para la funcion myrsa.

# La funcion minimo es para encontrar el minimo entre dos numeros.

def minimo (x, y):
	if x<y:
		return x
	else:
		return y

# La funcion mcd es para encontrar el maximo comun divisor (m.c.d) entre dos numeros.

def mcd (x, y):
	m = minimo (x, y)
	for i in range (m, 0, -1):
		if x%i == 0 and y%i ==0:
			return i

#La funcion arecoprime  devuelve 1 si dos numeros son coprimos o 0 en el caso contrario.

def arecoprime (x, y):
	m = mcd(x,y)
	if m==1:
		return 1
	else:
		return 0

# La funcion isprime encuentra si un numero dado es primo, aparecera  1 si es primo, o 0 si no lo es.

def isprime (k):

	for i in range (2, k):
		if k % i ==0:
			return 0
	return 1


## DESARROLLO DE LA FUNCION MYRSA

# Ahora se procede a crear la funcion que dados dos numeros primos p y q, genere las llaves publica y privada del algoritmo RSA.
# con la funcion isprime verificamos si los dos numeros son primos, en el caso de que uno o los dos no sean primos mostrara el mensaje: 
# "no son primos"
#
# Si los dos son primos se haya N, que esta dado por la formula N = p * q
#
# Luego se calcula phi(N) con la formula phi(N) = (p-1) * (q-1), gracias a phi(N) podemos encontrar a "e" y "d" de las llaves.
#
# Se escoge un entero positivo "e" que cumpla con dos condiciones: la primera es 1 < e < phi(N),  y la segunda es que sea coprimo con phi(N).
# para que cumpla la primera condicion se crea un range (2, phi(n)+1) y para la segunda condicion se utiliza la funcion arecoprime.
#
# Luego de la lista del range "e" se escoge el ultimo numero de la lista, ya que entre mas grande sea "e", habra menos riesgo de seguridad.
#
# se escoge un "d" tal que d * e * %phi(N) = 1, donde "d" es una lista de numeros (1,2,3...), para hallar "d" 
# se crea un range que va desde 0 hasta phi(n) * 3, lo multiplico por tres para hallar el tercero de la lista.
#
# Por ultimo se muestra la llave publica (e, N) y la llave privada (d, N).


def myrsa (p, q):
	if isprime (p)==0 or isprime (q)==0:
		return  "no son primos"
	else:
		N = p * q
	        phi_N = (p-1) * (q-1)

		for e in range (2, phi_N+1):
			if arecoprime (e, phi_N) == 1:
				e

		for d in range (0, phi_N*3):
			if d * e % phi_N == 1:
				d

		print "La llave publica es: ",e,",",N
		print "La llave privada es: ",d,",",N

print myrsa(3, 7) 
