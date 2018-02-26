class product(object):
	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"
	def sell(self):
		self.status = "Sold"
		return self
	def add_tax(self, tax):
		total = self.price + (self.price * tax)
		return total
	def return_reason(self, reason):
		if reason == "defective":
			self.status = "defective"
			self.price = 0
		elif reason == "in box":
			self.status = "for sale"
		elif reason == "opened":
			self.status = "used"
			self.price = self.price * 0.20
		return self
	def display_info(self):
		print "Price", self.price
		print "item_name", self.item_name
		print "weight", self.weight
		print "brand", self.weight
		print "status", self.status
		return self


p1 = product(200,"chair","30lb","SiTech")
p1.add_tax(0.13)
p1.sell().display_info()
p2 = product(1000,"bed","180lb","SiTech")
p2.return_reason("defective").display_info()
p3 = product(100,"lamp","10lb","SiTech")
p3.return_reason("in box").display_info()
p4 = product(100,"lamp","10lb","SiTech")
p4.return_reason("opened").display_info()

		