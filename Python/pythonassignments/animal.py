class animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def display_health(self):
		print "Health:", self.health
		return self

class dog(animal):
	def __init__(self,name):
		super(dog,self).__init__(name)
		self.health = 150
	def pet(self):
		self.health += 5
		return self

class dragon(animal):
	def __init__(self,name):
		super(dragon,self).__init__(name)
		self.health = 170
	def fly(self):
		self.health -= 10
		return self
	def display_health(self):
		super (dragon,self).display_health()
		print "I am a Dragon"
Dog1 = dog("Drako")
Dog1.walk().walk().walk().run().run().pet().display_health()

Dragon = dragon("Karma").display_health()

