################
##Housekeeping##
################
from time import sleep

notebook = []

def scan_input(raw):
	lowered = raw.lower()
	scanned_input = lowered.split(' ')
	return scanned_input 

def match_input(scanned_input, key):
	if set(scanned_input) & set(key) == set([]):
		return True
	else:
		return False

import rooms_intro
################
#### Items #####
################
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

################
##Start of Game#
################
def start():
	rooms_intro.start_intro()
	#sleep(1) #This waits a moment between printing messages
	print "Enter BEGIN to approach the island."

	choice = scan_input(raw_input("> "))

	key = ['begin']

	if match_input == True:
		ship_awaken()
	else:
		ship_awaken()

def ship_awaken():
	rooms_intro.ship_awaken()
	
	notebook.append(["The adventure has begun."])

	key = ['run', 'away','leave']

	choice = scan_input(raw_input("> "))

	if "apologize" in choice:
		captain_i()
	elif match_input == True:
		captain_ii()
	else:
		captain_iii()

def captain_i():
	rooms_intro.captain_i()

	choice = scan_input(raw_input("> "))

	if "read" in choice or "letter" in choice or "open" in choice:
		read_letteri()
	elif "watch" in choice or "sea" in choice or "wait" in choice:
		wait_dock()
	else:
		read_letterii()

def captain_ii():
	rooms_intro.captain_ii()

	choice = scan_input(raw_input("> "))

	if "read" in choice or "letter" in choice or "open" in choice:
		read_letteri()
	elif "watch" in choice or "sea" in choice or "wait" in choice:
		wait_dock()
	else:
		read_letterii()

def captain_iii():
	rooms_intro.captain_iii()

	choice = scan_input(raw_input("> "))


	if "read" in choice or "letter" in choice or "open" in choice:
		read_letteri()
	elif "watch" in choice or "sea" in choice or "wait" in choice:
		wait_dock()
	else:
		read_letterii()

def read_letteri():
	print """ You can't help but open the well worn envelope one more time before you dock. Something about it is irresistible.
You slide your finger across the dark blue wax seal, stamped with the shape of a strange and spiny, spiral seashell.
Your great-grandfather's handwriting stands out in green ink that almost glows against the thick, cream paper. """
	print letter 
	choice = scan_input(raw_input("> "))

	if "childhood" in choice or "visit" in choice:
		visit_memory()
	elif "stories" in choice or "revisit" in choice or "story" in choice or "mother" in choice:
		mother_story()
	else:
		dock_arrivei()

def read_letterii():
	rooms_intro.read_letteri()
	print letter
	choice = scan_input(raw_input("> "))

	if "childhood" in choice or "visit" in choice:
		visit_memory()
	elif "stories" in choice or "story" in choice or "mother" in choice:
		mother_story()
	else:
		dock_arrivei()

def visit_memory():
	rooms_intro.visit_memory()

	choice = scan_input(raw_input("> "))


	if "note" in choice or "nailed" in choice:
		dock_note()
	elif "path" in choice or "island" in choice:
		pathi()
	else:
		dock_fill()

def mother_story():
	rooms_intro.mother_story()

def wait_dock():
	rooms_intro.wait_dock()
	
	choice = scan_input(raw_input("> "))

	if "note" in choice or "nailed" in choice:
		dock_note()
	elif "letter" in choice or "great-grandfather" in choice:
		read_letteriii()
	else:
		dock_fill()

def dock_note():
	rooms_intro.dock_note()

def read_letteriii():
	rooms_intro.read_letteriii()
	
	print letter

	choice = scan_input(raw_input("> "))


	if "note" in choice or "nailed" in choice:
		dock_note()
	elif "path" in choice or "island" in choice:
		pathi()
	elif "childhood" in choice or "visit" in choice:
		visit_memory()
	elif "stories" in choice or "story" in choice or "mother" in choice:
		mother_story()
	else:
		dock_fill()

def dock_fill():
	rooms_intro.dock_fill()
	print """ You were supposed to meet someone here. 
Perhaps there is more information in the note on the dock or something you missed in the letter you came with. """
	
	choice = scan_input(raw_input("> "))

	if "note" in choice or "nailed" in choice:
		dock_note()
	elif "letter" in choice or "great-grandfather" in choice:
		read_letteriii()
	elif "path" in choice or "island" in choice:
		pathi()
	elif "childhood" in choice or "visit" in choice:
		visit_memory()
	elif "stories" in choice or "story" in choice or "mother" in choice:
		mother_story()
	else:
		dock_fill()

def dock_arrivei():
	rooms_intro.dock_arrivei()
	
	choice = scan_input(raw_input("> "))

	if "note" in choice or "nailed" in choice:
		dock_note()
	elif "letter" in choice or "great-grandfather" in choice:
		read_letteriii()
	else:
		dock_fill()

start()
