#Para probar con otros valores editar la lista A
A = [2,2,1,22,15]  

def verificar_bueno(subconjunto): #O(n)
	es=False
	uno=True
	if len(subconjunto)!=0:
		for x in range(len(subconjunto)):
			if subconjunto[x]%(x+1)==0:
				es=True
			else:
				es=False
				uno=False
	return (es and uno)


def subarreglos_buenos(A):
	A = [[x] for x in A]
	buenos = []
	for x in range(len(A)):
		for y in range(len(buenos)):
			if verificar_bueno(buenos[y]+A[x]):
				buenos.append(buenos[y]+A[x])
		if verificar_bueno(A[x]):
			buenos.append(A[x])
	return buenos

n = subarreglos_buenos(A)
print("El arreglo ",A, " tiene ",len(n)," subarreglos buenos que son:")
print(n)


