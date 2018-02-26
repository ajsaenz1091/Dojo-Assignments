
#part 1

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def names(list1):
# 	for person in list1:
# 		print person['first_name'] + ' ' + person['last_name']
# names(students)


#part 2

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def unpackdictionarie(userdict):
	number = 1
	for key in userdict:
		print key
		number = 1
		for person in userdict[key]:
			print str(number) +" - "+ person['first_name']+ " "+ person["last_name"] + ' - ' + str(len(person['first_name']) + len(person['last_name']))
			number += 1
unpackdictionarie(users)


#  	for type in dict:
#  		print type
#  		for user in range(0,len(dict[type])):
#  			name = dict[type][user].values()
#  			joined = "".join(str(x) for x in name)
#  			print user + 1, "-", len(joined)-1
# unpackdictionarie(users)