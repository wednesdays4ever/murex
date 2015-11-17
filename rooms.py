################
##Housekeeping##
################
from time import sleep
import os
import housekeeping
import rooms_intro

notebook = []



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

clear_screen = "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n"

################
##Start of Game#
################
def start():
	rooms_intro.start_intro()
	#sleep(1) #This waits a moment between printing messages
	print "Enter BEGIN to approach the island."

	choice = housekeeping.scan_input(raw_input("> "))

	key1 = ['begin']
	key2 = ['begin']
	key3 = ['begin']
	key4 = ['begin']
	key5 = ['begin']
	key6 = ['begin']

	if housekeeping.match_input == "door1":
		print clear_screen
		ship_awaken()
	else:
		print clear_screen
		ship_awaken()

def ship_awaken():
	rooms_intro.ship_awaken()
	
	notebook.append(["The adventure has begun."])

	key1 = ['apologize', 'say sorry']
	key2 = ['run', 'away',' leave']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	choice = housekeeping.scan_input(raw_input("> "))

	if housekeeping.match_input == 'door1':
		captain_i()
	elif housekeeping.match_input == 'door2':
		captain_ii()
	else:
		captain_iii()

def captain_i():
	rooms_intro.captain_i()

	key1 = ['read', 'letter','open']
	key2 = ['watch', 'letter', 'sea']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	choice = housekeeping.scan_input(raw_input("> "))

	if housekeeping.match_input == "door1":
		read_letteri()
	elif housekeeping.match_input == "door2":
		wait_dock()
	else:
		read_letterii()

def captain_ii():
	rooms_intro.captain_ii()

	key1 = ['read', 'letter','open']
	key2 = ['watch', 'letter', 'sea']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?
	rooms_intro.captain_ii()

	choice = housekeeping.scan_input(raw_input("> "))

	if housekeeping.match_input == "door1":
		read_letteri()
	elif housekeeping.match_input == "door2":
		wait_dock()
	else:
		read_letterii()

def captain_iii():
	rooms_intro.captain_iii()
	key1 = ['read', 'letter','open']
	key2 = ['watch', 'letter', 'sea']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	choice = housekeeping.scan_input(raw_input("> "))

	if housekeeping.match_input == "door1":
		read_letteri()
	elif housekeeping.match_input == "door2":
		wait_dock()
	else:
		read_letterii()

def read_letteri():
	print """ You can't help but open the well worn envelope one more time before you dock. Something about it is irresistible.
You slide your finger across the dark blue wax seal, stamped with the shape of a strange and spiny, spiral seashell.
Your great-grandfather's handwriting stands out in green ink that almost glows against the thick, cream paper. """
	print letter 

	key1 = ['childhood','visit']
	key2 = ['stories', 'revisit','story','mother']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	choice = housekeeping.scan_input(raw_input("> "))

	if housekeeping.match_input == "door1":
		visit_memory()
	elif housekeeping.match_input == "door2":
		mother_story()
	else:
		dock_arrivei()

def read_letterii():
	rooms_intro.read_letteri()
	print letter
	
	key1 = ['childhood','visit']
	key2 = ['stories', 'revisit','story','mother']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	choice = housekeeping.scan_input(raw_input("> "))

	if housekeeping.match_input == "door1":
		visit_memory()
	elif housekeeping.match_input == "door2":
		mother_story()
	else:
		dock_arrivei()

def visit_memory():
	rooms_intro.visit_memory()

	key1 = ["note","nailed"]
	key2 = ["path", "island"]
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	choice = housekeeping.scan_input(raw_input("> "))

	if housekeeping.match_input == "door1":
		dock_note()
	elif housekeeping.match_input == "door2":
		pathi()
	else:
		dock_fill()

def mother_story():
	rooms_intro.mother_story()

def wait_dock():
	rooms_intro.wait_dock()

	key1 = ["note","nailed"]
	key2 = ["letter", "great-grandfather"]
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	choice = housekeeping.scan_input(raw_input("> "))

	if housekeeping.match_input == "door1":
		dock_note()
	elif housekeeping.match_input == "door2":
		read_letteriii()
	else:
		dock_fill()

def dock_note():
	rooms_intro.dock_note()

def read_letteriii():
	rooms_intro.read_letteriii()	
	print letter

	key1 = ["note","nailed"]
	key2 = ["path","island"]
	key3 = ["childhood","visit"]
	key4 = ["stories", "story", "mother"]
	key5 = ['no way'] #add a key here?

	choice = housekeeping.scan_input(raw_input("> "))

	if housekeeping.match_input == "door1":
		dock_note()
	elif housekeeping.match_input == "door2":
		pathi()
	elif housekeeping.match_input == "door3":
		visit_memory()
	elif housekeeping.match_input == "door4":
		mother_story()
	else:
		dock_fill()

def dock_fill():
	rooms_intro.dock_fill()

	key1 = ['note','nailed']
	key2 = ['letter','great-grandfather']
	key3 = ['path','island']
	key4 = ['childhood','visit']
	key5 = ['stories','story','mother']

	choice = housekeeping.scan_input(raw_input("> "))

	if housekeeping.match_input == "door1":
		dock_note()
	elif housekeeping.match_input == "door2":
		read_letteriii()
	elif housekeeping.match_input == "door3":
		pathi()
	elif housekeeping.match_input == "door4":
		visit_memory()
	elif housekeeping.match_input == "door5":
		mother_story()
	else:
		dock_fill()

def dock_arrivei():
	rooms_intro.dock_arrivei()

	key1 = ['note','nailed']
	key2 = ['letter','great-grandfather']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	choice = housekeeping.scan_input(raw_input("> "))

	if housekeeping.match_input == "door1":
		dock_note()
	elif housekeeping.match_input == "door2":
		read_letteriii()
	else:
		dock_fill()

start()
