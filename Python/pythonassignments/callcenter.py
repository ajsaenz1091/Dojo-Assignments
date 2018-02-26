
call_id = 1
class call(object):

	def __init__(self, name, phone_number, time_of_call, reaason_for_call, call_id):
		self.name = name
		self.phone_number = phone_number
		self.time_of_call = time_of_call
		self.reason_for_call = reaason_for_call
	#need to figure out how to get a unique id
		self.id =call_id
	
	#self.id =To be defined
	def displayCall(self):
		print "******* "
		print "ID:{}"
		print "caller: {}".format(self.name)
		print "Number: {}".format(self.phone_number)
		print"time of call: {}".format(self.time_of_call)
		print"Reason:{}".format(self.reaason_for_call)
		print "-------"
		return self

	def __repr__(self):
		return "Name:{},ID: {}".format(self.name,self.call_id)

class callCenter(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.callList = []
		self.queue = 0
		self.call_id =1

#need these methods:
#add a call
	def addCall(self, name, phone_number, time_of_call, reason_for_call):
		c1 = call(name,phone_number,time_of_call,reason_for_call,self.call_id)
		self.call_id += 1
		self.callList.append(c1)
		self.queue += 1
#remove a call from front of list
#info : orint info about a call
#ninja: find and remove by phone_number
#hacker: queue sort by time ascending order
		

center1 = callCenter()
center1.addCall("Bob","555-555-5555", "Feb-8-2018","Angry about billing")
center1.addCall("Nick","575-565-5895", "Mar-2-2018","Never ever angry about anything")
print center1.callList