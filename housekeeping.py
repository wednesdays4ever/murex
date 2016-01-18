################
#### Items #####
################

clear_screen = "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n"

notebook = ""
clue = 'Nothing of note.'

letter = """
ELSA,
	YOU WERE TOO YOUNG TO REMEMBER OUR ONLY MEETING, BUT I ASSUME YOU'VE HEARD OF ME. 
	OUR SHARED RELATIVES ARE SMALL-MINDED, SO GOOD OR BAD, I WOULD NOT TRUST WHAT YOU HAVE HEARD.
	TO TRUST EVEN YOU IS A RISK, BUT ONE I MUST TAKE. YOUR BLOOD IS MINE AND OURS IS OF THE ANCIENTS.
	THE ISLE OF MURESTOS IS REMOTE, BUT THERE IS A CHARTERED SHIP THAT WILL BEGIN PREPARATIONS IMMEDIATELY WHEN YOU UTTER THE PASSWORD MUREX.
	THE SEA IS RISING. THE CONDITIONS ARE PERFECT.
	IF YOU CARE ABOUT THE FUTURE OF OUR WORLD AND MANY OTHERS, I WILL SEE YOU WITHIN THE MONTH."
	THE ISLAND'S CARETAKER, MINISTER DOBBINS, WILL MEET YOU AT THE DOCK UPON YOUR ARRIVAL."
		YOUR RELATION,
			TAYMOR HUNTINGDON VII
You barely remember him, and everything you've heard mentioned is so vague.
Do you push to remember his childhood visit? Or revisit the stories your mother told? Or wait to see him yourself? """

diary = """
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		The Diary of the Mad GL
		>> His deepest secrets here. <<
		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		"""

###################
## Key Functions ##
###################		

def scan_input(raw):
	lowered = raw.lower()
	scanned_input = lowered.split(' ')
	return scanned_input 

def match_input(scanned_input, key1, key2, key3, key4, key5):
	if set(scanned_input) & set(key1) != set([]):
		return "door1"
	elif set(scanned_input) & set(key2) != set([]):
		return "door2"
	elif set(scanned_input) & set(key3) != set([]):
		return "door3"
	elif set(scanned_input) & set(key4) != set([]):
		return "door4"
	elif set(scanned_input) & set(key5) != set([]):
		return "door5"
	else:
		return "door6"

	#The below is an attempt to put this into a loop.
	# n = 1
	# keys = [key1, key2, key3, key4, key5]
	# for key in keys:
	# 	if set(scanned_input) & set(key) != set([]):
	# 	    pass
	# 	else: 
	# 	    n += 1
	# door = "door" + str(n)
	# return door

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
	elif choice == ['look','around']:
		print clue
		ask_input()
		return choice
	else: 
		return choice
	