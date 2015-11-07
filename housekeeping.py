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