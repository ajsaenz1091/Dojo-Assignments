class Employee(object):
	raise_amt = 1.04
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@email.com'
		self.pay = pay
	def fullname(self):
		print self.first + self.last
	def apply_raise(self):
		self.pay = (self.pay * 1.04)
		return self

class Developer(Employee):
	raise_amt = 1.10

	def __init__(self,first,last,pay,prog_lang):
		super(Developer,self).__init__(first,last,pay)
		self.prog_lang = prog_lang

dev_1 = Developer("Corey","Schafer",50000,"JS")
dev_2 = Developer("Test","Employee",60000,"Python")

print (dev_1.pay)
print (dev_1.prog_lang)