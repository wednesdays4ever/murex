################
##Housekeeping##
################
from time import sleep
import os
import housekeeping
import rooms_intro
import fortress

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
		print housekeeping.clear_screen
		ship_awaken()
	else:
		print housekeeping.clear_screen
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
		print housekeeping.clear_screen
		ship_awaken()
	else:
		print housekeeping.clear_screen
		ship_awaken()


def ship_awaken():
	rooms_intro.ship_awaken()
	
	item = "* The adventure has begun. \n"

	clue = """You spy a grizzled sailor fingering his rosary 
			and mumbling to himself in a corner.
			He averts his eyes when you notice him.
			What you've heard is true, you think,
			seamen are both god-fearing and rude."""

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
	rooms_intro.read_letteri
	print housekeeping.letter 
	print housekeeping.reaction_to_letter

	item = "* Preparations password = murex; Island caretaker = Dobbins \n"

	if item not in housekeeping.notebook: 
		housekeeping.notebook += item

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
	rooms_intro.read_letterii()
	print housekeeping.letter
	print housekeeping.reaction_to_letter

	item = "* Seal is stamped with spiral seashell \n"

	if item not in housekeeping.notebook: 
		housekeeping.notebook += item
	
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

	key1 = ["note","nailed", "read"]
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

	item = "* Mother held in truck on oceanic journey \n"

	if item not in housekeeping.notebook: 
		housekeeping.notebook += item

	wait_dock()

def wait_dock():
	rooms_intro.wait_dock()

	key1 = ["note","nailed", "read"]
	key2 = ["letter", "revisit", "great-grandfather"]
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	clue = """In stories as a child you remember hearing about the 
	ocean as a magical character ready to whisk you off to new and exciting adventures.
	Now, you look at it as something else entirely.

	The formidable barrier between home and the unsettling other."""

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
	print housekeeping.letter
	print housekeeping.reaction_to_letter

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
		path_from_dock()

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
		path_left()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		path_right()
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
		path_left()
	elif housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		path_right()
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

	item = "* The eyes says it will only open for chosen ones. \n"

	if item not in housekeeping.notebook: 
		housekeeping.notebook += item

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

#MISSING HOPELESS WAIT
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

	key1 = ['left', 'forest', 'dirt', 'forward','enter', 'further']
	key2 = ['right', 'cliff', 'cliffs', 'rocks']
	key3 = ['return to docks', 'docks']
	key4 = ['door','knock'] #add a key here?
	key5 = ['no way'] #add a key here?

	clue = """There is nothing new to notice 
	about your environment as far as you can tell.
	But you feel the strength of the sun beating down on you.
	You look up, sweat dripping from your temples, and fight back the 
	overwhelming awareness of the tiny space you take up in this world."""

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		forest_enter()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		path_right()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		path_from_dock()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door4":
		default_door()
	else:
		hopeless_wait()

def forest_enter():
	rooms_intro.forest_enter()

	key1 = ['proceed','forest', 'forward','enter']
	key2 = ['turn back', 'return', 'docks']
	key3 = ['door'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		forest_ruins()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		path_from_dock
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		default_from_dock
	else:
		forest_ruins()

def forest_ruins():
	rooms_intro.forest_ruins()

	key1 = ['rope ladder', 'climb rope', 'tree house', 'approach tree']
	key2 = ['clearing', 'head down path']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		tree_house()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		clearing_path()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door3":
		default_forest()
	else:
		tree_house()

def default_forest():
	rooms_intro.default_forest()
	tree_house() 

def tree_house():
	rooms_intro.tree_house()

	key1 = ['start', 'walk around', 'inspect']
	key2 = ['clearing', 'leave tree house']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	clue = """Amid the chaos, one book remains mostly intact, 
	poking out from beneath the leather chair."""

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		tree_house_inspect()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		clearing_path()
	else:
		tree_house_inspect()

def tree_house_inspect():
	rooms_intro.tree_house_inspect()

	key1 = ['read', 'open', 'diary']
	key2 = ['clearing', 'leave tree house']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		open_diary()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		clearing_path()
	else:
		open_diary()

def open_diary():
	rooms_intro.open_diary()

	key1 = ['read', 'open', 'clues']
	key2 = ['discard', 'toss', 'worthless']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		read_diary()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		discard_diary()
	else:
		read_diary()

def read_diary():
	rooms_intro.read_diary()

	item = housekeeping.diary

	if item not in housekeeping.notebook: 
		housekeeping.notebook += item

	rope_bridge()

def discard_diary():
	rooms_intro.discard_diary()
	rope_bridge()
	pass

def rope_bridge():
	rooms_intro.rope_bridge()

	key1 = ['forward', 'venture', 'bridge']
	key2 = ['return', 'back', 'close', 'door']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?	

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		cross_bridge()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		no_bridge()
	else:
		cross_bridge()

def no_bridge():
	rooms_intro.no_bridge()

	key1 = ['forward', 'venture', 'bridge']
	key2 = ['ladder', 'down', 'clearing']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?	

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		cross_bridge()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		clearing_path()
	else:
		cross_bridge()

def cross_bridge():
	rooms_intro.cross_bridge()

	key1 = ['continue', 'closed eye', 'fortress']
	key2 = ['ladder', 'down', 'clearing']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		second_sect_hq()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		clearing_path()
	else:
		second_sect_hq()

def second_sect_hq():
	rooms_intro.second_sect_hq()

	key1 = ['read', 'paper', 'pick up']
	key2 = ['ladder', 'down', 'ground']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door1":
		second_sect_manifesto()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2, key3, key4, key5) == "door2":
		ladder_down()
	else:
		second_sect_manifesto()

def second_sect_manifesto():
	rooms_intro.second_sect_manifesto()

	item = housekeeping.manifesto

	if item not in housekeeping.notebook: 
		housekeeping.notebook += item

	ladder_down()

def ladder_down():
	rooms_intro.ladder_down()
	
	key1 = ['continue', 'investigation', 'forest', 'footsteps']
	key2 = ['path', 'return', 'clearing']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2) == "door1":
		follow_steps()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2) == "door2":
		path_back()
	else:
		follow_steps()

def follow_steps():
	rooms_intro.follow_steps()

	key1 = ['continue', 'enter', 'darkness']
	key2 = ['path', 'return', 'clearing']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	
	if housekeeping.match_input(scanned_input, key1, 
									 key2) == "door1":
		cave_enter
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2) == "door2":
		path_back()
	else:
		cave_enter

def cave_enter():
	rooms_intro.cave_enter()

	key1 = ['hello', 'introduce', 'say hi', 'talk']
	key2 = ['punch', 'hit']
	key3 = ['no way']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	
	if housekeeping.match_input(scanned_input, key1, 
									 key2) == "door1":
		gl_introduce()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2) == "door2":
		gl_threaten()
	else:
		gl_introduce()
		

def gl_introduce():
	rooms_intro.gl_introduce()
	
	key1 = ['stand', 'look','nothing']
	key2 = ['punch', 'hit', 'slap', 'walk']
	key3 = ['diary', 'show', 'letter']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	
	if housekeeping.match_input(scanned_input, key1, 
									 key2) == "door1":
		gl_no_patience()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2) == "door2":
		gl_threaten()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key3) == "door3":
		gl_diary_show()
	else:
		gl_teymor()

def gl_taymor():
	rooms_intro.gl_taymor()

	key1 = ['stand', 'look','nothing']
	key2 = ['punch', 'hit', 'slap', 'walk']
	key3 = ['diary', 'show', 'letter']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	
	if housekeeping.match_input(scanned_input, key1, 
									 key2) == "door1":
		gl_no_patience()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2) == "door2":
		gl_threaten()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key3) == "door3":
		gl_diary_show()
	else:
		gl_no_patience()

def gl_threaten():
	rooms_intro.gl_threaten()
	pass

def gl_diary_show():
	rooms_intro.gl_diary_show()
	
	key1 = ['yes', 'i do']
	key2 = ['no', 'i don\'t', 'do not']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	
	if housekeeping.match_input(scanned_input, key1, 
									 key2) == "door1":
		gl_purity()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2) == "door2":
		gl_no_patience()
	else:
		gl_no_patience()

def gl_no_patience():
	rooms_intro.gl_no_patience()
	
	key1 = ['temple', 'taymor']
	key2 = ['punch', 'hit']
	key3 = ['diary', 'show', 'letter']
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	
	if housekeeping.match_input(scanned_input, key1, 
									 key2) == "door1":
		gl_end_me()
	else:
		gl_no_kill()


def gl_diary_show():
	rooms_intro.gl_diary_show()
	
	rooms_intro.gl_end_me()

def gl_end_me():
	rooms_intro.gl_end_me()

	key1 = ['yes', 'i do', 'kill', 'dead']
	key2 = ['no', 'i don\'t', 'do not', 'will not']
	key3 = ['leave', 'turn back'] 
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()
	
	if housekeeping.match_input(scanned_input, key1, 
									 key2) == "door1":
		gl_dead()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2) == "door2":
		gl_no_kill()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key3) == "door3":
		gl_no_kill_leave()
	else:
		gl_no_kill_stay()

def gl_dead():
	rooms_intro.gl_dead()

	rooms_intro.return_clearing()

def gl_no_kill():
	rooms_intro.gl_no_kill()

	key1 = ['stay', 'wait', 'watch', 'nothing']
	key2 = ['leave', 'turn back', 'return', 'docks']
	key3 = ['no way'] #add a key here?
	key4 = ['no way'] #add a key here?
	key5 = ['no way'] #add a key here?

	scanned_input = housekeeping.ask_input()

	if housekeeping.match_input(scanned_input, key1, 
									 key2) == "door1":
		gl_no_kill_stay()
	elif  housekeeping.match_input(scanned_input, key1, 
									 key2) == "door2":
		gl_no_kill_leave()
	else:
		gl_no_kill_leave()

def gl_no_kill_leave():
	rooms_intro.gl_no_kill_leave()

    key1 = ['cave', 'return', 'GL', 'kill']
    key2 = ['leave', 'turn back', 'return', 'docks']
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                                     key2) == "door1":
        gl_end_me()
    elif  housekeeping.match_input(scanned_input, key1, 
                                     key2) == "door2":
        path_back()
    else:
        gl_end_me	

def gl_no_kill_stay():
	rooms_intro.gl_no_kill_stay()

	still_on_dock()


def path_back():
	rooms_intro.path_back()

	clearing_path()


def clearing_path():
    rooms_intro.clearing_path()

    key1 = ['investigate', 'tree house', 'tree']
    key2 = ['cave', 'trace', 'steps']
    key3 = ['dock', 'docks', 'ship', 'return'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                                     key2) == "door1":
        tree_house()
    elif  housekeeping.match_input(scanned_input, key1, 
                                     key2) == "door2":
        path_back()
    elif  housekeeping.match_input(scanned_input, key1, 
                                     key2) == "door2":
        still_on_dock()
    else:
        default_forest()  

def path_right():
	rooms_intro.path_right()

##Need to write a whole path to reach this door again.
def door_return_refuse():
    fortress.door_return_refuse()
    door_return()

def door_return():
    fortress.door_return()

    key1 = ['yes', 'yeah', 'ready', 'judgement']
    key2 = ['no', 'not ready', 'leave'] 
    
    if housekeeping.match_input(scanned_input, key1, 
                                     key2) == "door1":
        door_return_yes()
    elif  housekeeping.match_input(scanned_input, key1, 
                                     key2) == "door2":
        door_return_no()
    else:
        door_return_no()

def door_return_yes():
    fortress.door_return_yes()
    
    key1 = ['yes', 'yeah', 'ready', 'succumb', 'desire']
    key2 = ['no', 'not ready', 'leave'] 
    
    if housekeeping.match_input(scanned_input, key1, 
                                     key2) == "door1":
        door_return_judgement()
    elif  housekeeping.match_input(scanned_input, key1, 
                                     key2) == "door2":
        door_return_judgement()
    else:
        door_return_judgement()

def door_return_no():
    fortress.door_return_no()
    pass







start()