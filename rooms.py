################
##Housekeeping##
################
from time import sleep
import os
import housekeeping
import rooms_intro

clear_screen = "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n"

################
#### Items #####
################

#notebook = ""

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

	key1 = ['help', 'menu']
	key2 = ['begin']
	key3 = ['stop']
	key4 = ['madness']
	key5 = ['please']
	key6 = ['work']

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		help_menu()
	elif housekeeping.match_input(scanned_input, key1, 
								  key2, key3, key4, key5) == "door2":
		print clear_screen
		ship_awaken()
	else:
		print clear_screen
		ship_awaken()

def help_menu():
	rooms_intro.help_menu()

	scanned_input = housekeeping.ask_input()

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
	
	item = "* The adventure has begun. \n"

	if item not in housekeeping.notebook: 
		housekeeping.notebook += item

	scanned_input = housekeeping.ask_input()

	key1 = ['apologize', 'sorry']
	key2 = ['run', 'away',' leave']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		captain_i()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
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

	item = "* The captain is a strange one. \n"
	
	if item not in housekeeping.notebook: 
		housekeeping.notebook += item

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		read_letteri()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		wait_dock()
	else:
		read_letterii()

def captain_ii():
	rooms_intro.captain_ii()

	key1 = ['read', 'letter','open']
	key2 = ['watch', 'letter', 'sea', 'wait']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		read_letteri()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
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

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		read_letteri()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
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

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		visit_memory()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
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

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		visit_memory()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
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

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		dock_note()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		pathi()
	else:
		dock_fill()

def mother_story():
	rooms_intro.mother_story()
	wait_dock()

def wait_dock():
	rooms_intro.wait_dock()

	key1 = ["note","nailed"]
	key2 = ["letter", "great-grandfather"]
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		dock_note()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		read_letteriii()
	else:
		dock_fill()

def dock_note():
	rooms_intro.dock_note()

	still_on_dock()

def read_letteriii():
	rooms_intro.read_letteriii()	
	print letter

	key1 = ["note","nailed"]
	key2 = ["path","island"]
	key3 = ["childhood","visit"]
	key4 = ["stories", "story", "mother"]
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		dock_note()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		pathi()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		visit_memory()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door4":
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

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		dock_note()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		read_letteriii()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		pathi()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door4":
		visit_memory()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door5":
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

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		dock_note()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		read_letteriii()
	else:
		dock_fill()

def still_on_dock(): 
	rooms_intro.still_on_dock()

	key1 = ['note','nailed', 'read']
	key2 = ['letter', 'open']
	key3 = ['forge on', 'forge', 'ahead', 'forward']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		dock_note()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		read_letteriii()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
	    path_from_dock()
	else:
		still_on_dock

def path_from_dock(): 
	rooms_intro.path_from_dock()

	key1 = ['left','turn left']
	key2 = ['right', 'turn right']
	key3 = ['straight','forward', 'right', 'ahead']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		dock_path_left()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		dock_path_right()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
	    door_with_no_knob()
	else:
		default_from_dock()


def default_from_dock():
	rooms_intro.default_from_dock()

	key1 = ['left','turn left']
	key2 = ['right', 'turn right']
	key3 = ['forward', 'right', 'ahead', 'straight']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		dock_path_left()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		dock_path_right()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
	    door_with_no_knob()
	else:
		default_from_dock()

def door_with_no_knob(): 
	rooms_intro.door_with_no_knob()

	key1 = ['push', 'pull', 'touch', 'stroke']
	key2 = ['leave', 'away', 'path', 'paths']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		push_or_pull_door()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		leave_door()
	else:
		default_door()

def default_door():
	rooms_intro.default_door()
	
	key1 = ['push', 'pull', 'touch', 'stroke', 'tap', 'knock']
	key2 = ['leave', 'away', 'path', 'paths']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		push_or_pull_door()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		leave_door()
	else:
		default_door()

def push_or_pull_door():
	rooms_intro.push_or_pull_door()

	key1 = ['push', 'pull', 'touch', 'tap', 'knock', 'hit', 'strike', 'punch', 'attack']
	key2 = ['Taymor', 'letter', 'search'] 
	key3 = ['who', 'your', 'name'] 
	key4 = ['need', 'let', 'dobbins'] 
	key5 = ['leave', 'away', 'path', 'paths']
	
	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		door_eye_other()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		door_eye_attempt_enter()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		door_eye_name()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door4":
		door_eye_answer()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door5":
		leave_door()
	else:
		door_eye_answer()

def door_eye_answer():
	rooms_intro.door_eye_answer()

	key1 = ['yes', 'servant', 'chosen', 'let', 'know' 'secrets']
	key2 = ['no', 'touch', 'tap', 'knock', 'hit', 'strike', 'punch', 'attack']
	key3 = ['leave', 'away', 'path', 'paths']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?
	
	scanned_input = housekeeping.ask_input()
	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		door_eye_other()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		door_eye_attempt_enter()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		leave_door()
	else:
		door_waits()


def door_eye_other():
	rooms_intro.door_eye_other()

	key1 = ['servant', 'chosen', 'let', 'know' 'secrets']
	key2 = ['touch', 'tap', 'knock', 'hit', 'strike', 'punch', 'attack']
	key3 = ['leave', 'away', 'path', 'paths']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		door_eye_attempt_enter()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		door_eye_not_chosen()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		leave_door()
	else:
		door_waits()
	#Finish this (all paths lead to door_eye_not_chosen or door_eye_attempt_enter, perhaps need to add extra sentence to end of it)
def door_eye_name():
	rooms_intro.door_eye_name()

	key1 = ['servant', 'chosen', 'let', 'know' 'secrets']
	key2 = ['touch', 'tap', 'knock', 'hit', 'strike', 'punch', 'attack']
	key3 = ['leave', 'away', 'path', 'paths']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		door_eye_attempt_enter()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		door_eye_not_chosen()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		leave_door()
	else:
		door_waits()

def door_eye_attempt_enter():
	rooms_intro.door_eye_attempt_enter()

	key1 = ['left', 'forest']
	key2 = ['right', 'cliff', 'cliffs', 'rocks']
	key3 = ['door', 'knock']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		path_left()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		path_right()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		door_shut_eye()
	else:
		wait_after_door()

def door_eye_not_chosen():
	rooms_intro.door_eye_not_chosen()

	key1 = ['left', 'forest']
	key2 = ['right', 'cliff', 'cliffs', 'rocks']
	key3 = ['door', 'knock']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		path_left()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		path_right()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		door_shut_eye()
	else:
		wait_after_door()

def door_waits():
	rooms_intro.door_waits()

	key1 = ['servant', 'chosen', 'let', 'know' 'secrets']
	key2 = ['touch', 'tap', 'knock', 'hit', 'strike', 'punch', 'attack']
	key3 = ['leave', 'away', 'path', 'paths']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		door_eye_attempt_enter()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		door_eye_not_chosen()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		leave_door()
	else:
		door_eye_not_chosen()

def leave_door():
	rooms_intro.leave_door()

	key1 = ['left', 'forest']
	key2 = ['right', 'cliff', 'cliffs', 'rocks']
	key3 = ['door', 'knock']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		path_left()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		path_right()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		door_shut_eye()
	else:
		wait_after_door()

def door_shut_eye():
	rooms_intro.door_shut_eye()

	key1 = ['left', 'forest']
	key2 = ['right', 'cliff', 'cliffs', 'rocks']
	key3 = ['door', 'knock']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		path_left()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		path_right()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		door_shut_eye()
	else:
		wait_after_door()

def wait_after_door():
	rooms_intro.wait_after_door()

	key1 = ['left', 'forest']
	key2 = ['right', 'cliff', 'cliffs', 'rocks']
	key3 = ['door', 'knock']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		path_left()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		path_right()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		door_shut_eye()
	else:
		hopeless_wait()

def hopeless_wait():
	rooms_intro.hopeless_wait()

	key1 = ['left', 'forest']
	key2 = ['right', 'cliff', 'cliffs', 'rocks']
	key3 = ['door', 'knock']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		path_left()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		path_right()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		door_shut_eye()
	else:
		hopeless_wait()

def path_left():
	rooms_intro.path_left()

def path_right():
	rooms_intro.path_right()



start()