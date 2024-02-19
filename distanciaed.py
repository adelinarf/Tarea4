import numpy as np

def distancia_edicion(A,B):
	m = len(B)
	n = len(A)
	d = np.zeros((n+1, m+1))
	for x in range(n+1):
		d[x][0] = x
	for z in range(1,m+1):
		d[0][z] = z
	A = [0]+A
	B = [0]+B
	for i in range(1,n+1):
		for j in range(1,m+1):
			if (A[i] == B[j]):
				d[i][j] = d[i-1][j-1]
			else:
				d[i][j] = 1+min([d[i-1][j],d[i][j-1],d[i-1][j-1]])
	return d

#Para probar con otros nombres editar las variables name y lastname
name="adelina"
lastname="figueira"
A = list(name)
B = list(lastname)

a = (distancia_edicion(A,B))
print("La tabla de distancia de edicion para",name,lastname,"es:")
print(a)