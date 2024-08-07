class company:
	def __init__(self,nm = "RK Builders",city="Hydrabas",mo = 302720):
		self.nm = nm
		self.city = city
		self.mo = mo
	def value(self):
		print("Company Name Is :"+self.nm)
		print("Company Address Is :"+self.city)
		print("Company Mobile No Is :",self.mo)
class emp(company):
	def __init__(self,enm,desig,salary):
		super().__init__()
		self.enm = enm
		self.desig = desig
		self.salary = salary
	def printvalue(self):
		print("Employe Name Is :"+self.enm)
		print("Employe Designation Is :"+self.desig)
		print("Employe Salary Is :",self.salary)
obj2 = emp("Digvijay Rathee","Senior Manager",45000)
obj2.value()
obj2.printvalue()