notebook = ""
clue = 'Nothing of note.'

def scan_input(raw):
	lowered = raw.lower()
	scanned_input = lowered.split(' ')
	return scanned_input 

def match_input(scanned_input, key1, key2, key3, key4, key5):
	if set(scanned_input) & set(key1) == set([]):
		return "door1"
	elif set(scanned_input) & set(key2) == set([]):
		return "door2"
	elif set(scanned_input) & set(key3) == set([]):
		return "door3"
	elif set(scanned_input) & set(key4) == set([]):
		return "door4"
	elif set(scanned_input) & set(key5) == set([]):
		return "door5"
	else:
		return "door6"

def ask_input():
	choice = scan_input(raw_input("> "))
	if choice == ['check','notebook']:
		print "You return to your notes."
		if notebook == []:
			print "So many secrets to uncover."
		else: 
			print "#"*10
			print notebook
			print "#"*10
			print "This is all you have learned."
		ask_input()
		return choice
	if choice == ['look','around']:
		print clue
		ask_input()
		return choice
	else: 
		return choice
	