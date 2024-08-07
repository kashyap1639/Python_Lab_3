class B1:
	def sum(self,a,b):
		self.c = a + b
class B2:
	def mul(self,x,y):
		self.z = x*y
class C1(B1,B2):
	def printValue(self):
		print("Sum Is :",self.c)
		print("Multiplication Is:",self.z)
c = C1()
c.sum(192,929)
c.mul(92,82)
c.printValue()