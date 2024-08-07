jclass emp:
	def __init__(self,nm,doj,desig,salary):
		self.nm = nm
		self.doj = doj
		self.desig = desig
		self.salary = salary
	def printvalue(self):
		print(self.nm)
		print(self.doj)
		print(self.desig)
		print(self.salary)
		
obj = emp("Kashyap Thakor","6th july 2020","Jr. Developer", 30000)
obj.printvalue()

	