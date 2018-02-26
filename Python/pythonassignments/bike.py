class Bike(object):
	def __init__(self, price,max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayinfo(self):
		print self.price, self.max_speed, self.miles
		return self
	def ride(self):
		self.miles +=10
		print "Riding", self.miles
		return self
	def reverse(self):
		self.miles -=5
		print "Rversing", self.miles
		return self

bike1 = Bike(200,"15mph")
bike1.ride().ride().ride().reverse().displayinfo()

# bike2 = Bike(300,"20mph")
# bike2.ride().ride().reverse().reverse().displayinfo()

# bike3 = Bike(400,"30mph")
# bike3.reverse().reverse().reverse().displayinfo()

		