import numpy as np 

def tiempo(x,y):  #O(1)
	return ((x[1]-x[0])**2+(y[1]-y[0])**2)

def create_d(A):  #O(n)
	d = [0]*len(A)
	d2 = [0]*len(A)
	for x in range(len(A)):
		d[x] = tiempo((0,0),A[x])
		d2[x] = tiempo((0,0),A[x])
	return [d,d2]

def create_s(A):   #O(n^2)
	n=len(A)    
	s = np.zeros((n, n))
	for x in range(len(A)):   
		for y in range(len(A)):
			s[x][y] = tiempo(A[x],A[y])
			if x!=y:
				continue
			else:
				s[x][y] = -1
	return s

def tiempo_avion(maleta_pos,d2): #O(1)
	return d2[maleta_pos]

def siguiente_tiempo_min(a):  #O(n)
	return min(a)

def pos_minimo(visitadas,d,d2): #O(n)
	minimo = min(d)
	this = 0
	for x in range(len(d2)):
		if d2[x] == minimo and x not in set(visitadas):
			this=x 
	return this

def tiempo_minimo(A):
	[d,d2] = create_d(A)
	s = create_s(A)
	m = min(d)
	pos_primera_maleta = d.index(m)
	a = list(s[:,pos_primera_maleta])
	a.pop(pos_primera_maleta)
	original = list(s[:,pos_primera_maleta])

	Q = [pos_primera_maleta]
	tiempo = d[pos_primera_maleta]
	d[0] = 15000000
	conseguidas = 0
	taken = [x for x in range(len(A))]
	visitadas = []
	while taken!=[]:
		pos = Q[0]
		taken.remove(pos)
		visitadas.append(pos)
		Q.pop(0)
		a = list(s[:,pos])
		a.pop(pos)
		original = list(s[:,pos])
		conseguidas+=1
		if conseguidas<=2:
			if tiempo_avion(pos,d2) < siguiente_tiempo_min(a):
				#dejarla en el avion
				pos_siguiente_maleta = pos_minimo(visitadas,d,d2)
				if pos_siguiente_maleta not in visitadas:
					tiempo += d2[pos_siguiente_maleta]
					d[pos_siguiente_maleta] = 15000000
					Q.append(pos_siguiente_maleta)
					conseguidas=0
			else:
				#buscar otra maleta minima
				h = siguiente_tiempo_min(a)
				pos_siguiente_maleta = original.index(h)
				if pos_siguiente_maleta not in visitadas:
					tiempo += siguiente_tiempo_min(a)
					Q.append(pos_siguiente_maleta)
	return tiempo

#Para probar con otros valores editar la lista A
A = [(2,3),(4,5),(10,20),(6,7),(10,2)]
t = tiempo_minimo(A)
print("Para las maletas en las posiciones: ",A)
print("El tiempo minimo en llevarlas al avión es de: ", t)