my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dictintupout(dict):
	newlist = []
	for key in dict:
		newlist.append((key,dict[key]))
	return newlist

print dictintupout(my_dict)
