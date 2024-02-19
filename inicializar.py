import sys

class Inicializador:
	def __init__(self):
		self.T = []
		self.ctr = 0
		self.a = []
		self.b = []
		self.n = 1

	def comando_valido(self,comando):
		lista = comando.split()
		valido = False
		val = 0
		i = []
		if lista[0] == "ASIGNAR":
			if len(lista)>3:
				valido=False
			else:
				try:
					pos = int(lista[1])
					value = int(lista[2])
					i = [pos,value]
					val=0
					valido=True
				except:
					valido=False
		elif lista[0] == "CONSULTAR":
			if len(lista)>2:
				valido=False
			else:
				try:
					pos = int(lista[1])
					i = [pos]
					val=1
					valido=True
				except:
					valido=False
		elif lista[0]=="LIMPIAR":
			if len(lista)>1:
				valido=False
			else:
				valido=True
				val=2
		elif lista[0]=="SALIR":
			if len(lista)>1:
				valido=False
			else:
				valido=True
				val=3
		else:
			valido=False		

		return [valido,val,i]

	def assign(self,pos,val):
		if 0<=pos<self.n:
			self.ctr += 1
			self.a[self.ctr] = pos
			self.b[pos] = self.ctr
			self.T[pos] = val
		else:
			print("La posición introducida no pertenece al arreglo")

	def consult(self,pos):
		if 0<=pos<self.n:
			if 1<=self.b[pos]<=self.ctr:
				if self.a[self.b[pos]]==pos:
					print("Se ha inicializado con el valor ",self.T[pos])
				else:
					print("No se ha inicializado la posición ",pos)
			else:
				print("No se ha inicializado la posición ",pos)
		else:
			print("La posición introducida no pertenece al arreglo")
		

	def valores_iniciales(self):
		self.T = [0]*self.n
		self.ctr = 0
		self.a = [0]*self.n
		self.b = [0]*self.n


	def clean(self):
		self.valores_iniciales()

	def do(self,option,values):
		if option==0: #asignar
			self.assign(values[0],values[1])
		elif option==1: #consultar
			self.consult(values[0])
		elif option==2: #limpiar
			self.clean()

	def call(self):
		try:
			arg = sys.argv[1]
			try:
				self.n = int(arg)
				self.valores_iniciales()
				print("Acciones disponibles:")
				print("Para asignar un valor ASIGNAR POS VAL")
				print("Para consultar un valor CONSULTAR POS")
				print("Para limpiar el arreglo LIMPIAR")
				print("Para salir del programa SALIR")
				while True:
					get = input("Comando: ")
					if get=="":
						continue
					c = self.comando_valido(get)
					if c[0]:
						if c[1]==3:
							break
						else:
							self.do(c[1],c[2])
					else:
						print("Comando no válido")
			except:
				print("Introduzca un numero válido")
		except:
			print("La llamada a inicializar debe ser:")
			print("python inicializar.py X con X siendo el número de elementos del arreglo")

A = Inicializador()
A.call()