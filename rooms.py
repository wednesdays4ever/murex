################
### Hey reader! A note:
## This is a the main file of the game, containing all the steps the player can walk through.
# The text of the steps are in other files but this file has the possible commands.
## Possible commands are found in the "keys." Please suggest additional keys!



################
##Housekeeping##
################
from time import sleep
import os
import housekeeping
import rooms_intro
import fortress
import endgame
import saintsbeach

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
    key2 = ['stories', 'revisit','story','mother', 'stories']
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
    key2 = ["path", "island", 'forward', 'walk', 'start']
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                                    key2, key3, key4, key5) == "door1":
        dock_note()
    elif housekeeping.match_input(scanned_input, key1, 
                                    key2, key3, key4, key5) == "door2":
        path_from_dock()
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

    key1 = ["note", "nailed", "read"]
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

    key1 = ["note", "nailed"]
    key2 = ["path", "island"]
    key3 = ["childhood", "visit"]
    key4 = ["stories", "story", "mother"]
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                                    key2, key3, key4, key5) == "door1":
        dock_note()
    elif housekeeping.match_input(scanned_input, key1, 
                                    key2, key3, key4, key5) == "door2":
        path_from_dock()
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
    key3 = ['path','island', 'go ahead', 'start']
    key4 = ['childhood','visit']
    key5 = ['stories','story','mother', 'revisit']

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

    key1 = ['note', 'nailed', 'read', 'look', 'back']
    key2 = ['letter', 'open', 'reread']
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
        try:
            blood
            door_return()
        except NameError: 
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
        try:
            blood
            door_return()
        except NameError: 
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

    try:
        blood
        door_return()
    except NameError:     
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
    
    key1 = ['push', 'pull', 'touch', 'stroke', 'tap', 'knock', 'attack', 'whisper']
    key2 = ['leave', 'away', 'path', 'paths']
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    try:
        blood
        door_return()
    except NameError: 
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
    key3 = ['door', 'knock', 'try', 'eye', 'straight']
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

    key1 = ['left', 'forest', 'tree house']
    key2 = ['right', 'cliff', 'cliffs', 'rocks']
    key3 = ['door', 'knock', 'straight']
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

    key1 = ['left', 'forest', 'dirt', 'forward','enter', 'further', 'yes', 'continue']
    key2 = ['right', 'cliff', 'cliffs', 'rocks', 'no']
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
    key3 = ['door', 'pyramid'] 
    key4 = ['tree house', 'ladder']
    key5 = ['no way']

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        forest_ruins()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        path_from_dock()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        default_from_dock()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door4":
        tree_house()
    else:
        forest_ruins()

def forest_ruins():
    rooms_intro.forest_ruins()

    key1 = ['ladder', 'rope', 'climb rope', 'tree house', 'tree', 'approach']
    key2 = ['clearing', 'head down path', 'path', 'cave', 'marked', 'step']
    key3 = ['return', 'docks', 'go back']
    key4 = ['no way']
    key5 = ['no way']

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        tree_house()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        clearing_path()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        path_from_dock()
    else:
        default_forest()

def default_forest():
    rooms_intro.default_forest()
    
    key1 = ['rope ladder', 'climb rope', 'tree house', 'approach tree']
    key2 = ['clearing', 'head down path', 'path']
    key3 = ['return', 'docks', 'go back']
    key4 = ['cave', 'marked', 'steps', 'GL']
    key5 = ['no way']

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        tree_house()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        clearing_path()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        path_from_dock()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door4":
        follow_steps()
    else: 
        default_forest()

def tree_house():
    rooms_intro.tree_house()

    key1 = ['start', 'walk around', 'inspect']
    key2 = ['clearing', 'leave', 'tree house', 'go back', 'docks' , 'ladder', 'return']
    key3 = ['chess', 'set'] 
    key4 = ['chair', 'rest', 'sit']
    key5 = ['leave', 'go back', 'down ladder', 'return']

    clue = """Amid the chaos, one book remains mostly intact, 
    poking out from beneath the leather chair."""

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        tree_house_inspect()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        return_clearing()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        chess()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door4":
        chair()
    else:
        tree_house_default()

def tree_house_default():
    rooms_intro.tree_house_default()

    key1 = ['start', 'walk around', 'inspect', 'book', 'open']
    key2 = ['clearing', 'tree house', 'go back', 'docks' , 'ladder']
    key3 = ['chess', 'set'] 
    key4 = ['chair', 'rest', 'sit'] 
    key5 = ['bridge', 'door', 'daylight', 'cross', 'leave', 'opposite'] 

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        tree_house_inspect()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        return_clearing()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        chess()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door4":
        chair()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door5":
        rope_bridge()
    else:
        tree_house_inspect()

def chair():
    rooms_intro.chair()

    tree_house_default()

def chess():
    rooms_intro.chess()

    tree_house_default()

def tree_house_inspect():
    rooms_intro.tree_house_inspect()

    key1 = ['read', 'open', 'diary', 'ask', 'book']
    key2 = ['clearing', 'leave', 'tree house', 'go back', 'docks' , 'ladder']
    key3 = ['bridge', 'rope', 'cross room', 'continue'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        open_diary()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        return_clearing()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        rope_bridge()
    else:
        tree_house_default()

def open_diary():
    rooms_intro.open_diary()

    key1 = ['read', 'open', 'clues', 'take']
    key2 = ['discard', 'toss', 'worthless', 'throw out']
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

    tree_house_default()

def discard_diary():
    rooms_intro.discard_diary()

    tree_house_default()

def rope_bridge():
    rooms_intro.rope_bridge()

    key1 = ['forward', 'venture', 'bridge' , 'continue']
    key2 = ['return', 'back', 'close', 'door', 'tree house']
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
    key3 = ['back', 'return', 'tree house'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?  

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        cross_bridge()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        clearing_path()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        tree_house()
    else:
        cross_bridge()

def cross_bridge():
    rooms_intro.cross_bridge()

    key1 = ['continue', 'closed eye', 'fortress']
    key2 = ['ladder', 'down', 'clearing']
    key3 = ['back', 'return', 'tree house'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        second_sect_hq()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        clearing_path()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        tree_house_default()
    else:
        second_sect_hq()

def second_sect_hq():
    rooms_intro.second_sect_hq()

    key1 = ['read', 'paper', 'pick up']
    key2 = ['ladder', 'down', 'ground']
    key3 = ['return', 'bridge'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        second_sect_manifesto()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        ladder_down()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        cross_bridge()
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
    
    key1 = ['continue', 'investigation', 'forest', 'footsteps', 'take', 'path']
    key2 = ['path', 'return', 'clearing']
    key3 = ['leave', 'return', 'go back', 'sect', 'hut']
    key4 = ['tree house']
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        follow_steps()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        path_back()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        second_sect_hq()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door4":
        tree_house_default()
    else:
        follow_steps()

def follow_steps():
    rooms_intro.follow_steps()

    key1 = ['continue', 'enter', 'darkness', 'yes', 'cave']
    key2 = ['path', 'return', 'clearing', 'no', 'go back']
    key3 = ['thatched hut', 'hut', 'ladder']
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        cave_enter()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        path_back()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        second_sect_hq()
    else:
        cave_enter()

def cave_enter():
    rooms_intro.cave_enter()

    key1 = ['hello', 'introduce', 'say hi', 'talk', 'taymor', 'pyramid']
    key2 = ['punch', 'hit', 'kill', 'attack', 'kick']
    key3 = ['no way']
    key4 = ['no way'] 
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        gl_introduce()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        gl_threaten()
    else:
        gl_introduce()
        

def gl_introduce():
    rooms_intro.gl_introduce()
    
    key1 = ['stand', 'look','nothing']
    key2 = ['punch', 'hit', 'slap', 'walk', 'kill', 'attack', 'stab', 'kick']
    key3 = ['diary', 'show', 'letter']
    key4 = ['taymor', 'great-grandfather', 'grandfather']
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        gl_no_patience()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        gl_threaten()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        gl_diary_show()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door4":
        gl_taymor()
    else:
        gl_taymor()

def gl_taymor():
    rooms_intro.gl_taymor()

    key1 = ['stand', 'look','nothing']
    key2 = ['punch', 'hit', 'slap', 'walk', 'kill', 'attack', 'stab', 'kick']
    key3 = ['diary', 'book']
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        gl_no_patience()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        gl_threaten()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key3, key3, key4, key5) == "door3":
        gl_diary_show()
    else:
        gl_no_patience()

def gl_threaten():
    rooms_intro.gl_threaten()
    
    key1 = ['stand', 'look','nothing']
    key2 = ['punch', 'hit', 'slap', 'walk', 'kill', 'attack','stab','kick']
    key3 = ['diary', 'book']
    key4 = ['taymor, letter, grandfather']
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        gl_no_patience()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        gl_no_patience()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        gl_diary_show()
    elif housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door4":
        gl_taymor()
    else:
        gl_no_patience() 

def gl_no_kill_stay():
    rooms_intro.gl_no_kill_stay()

    still_on_dock()
 

def gl_diary_show():
    rooms_intro.gl_diary_show()
    
    key1 = ['yes', 'i do']
    key2 = ['no', 'i don\'t', 'do not']
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door1":
        gl_purity()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door2":
        gl_no_patience()
    else:
        gl_no_patience()

def gl_purity():
    rooms_intro.gl_purity()

    key1 = ['yes', 'i have']
    key2 = ['no', 'i  haven\'t', 'do not']
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        gl_end_me()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        gl_end_me()
    else:
        gl_end_me()

def gl_no_patience():
    rooms_intro.gl_no_patience()
    
    key1 = ['temple', 'taymor']
    key2 = ['punch', 'hit', 'kick', 'attack', 'kill', 'stab']
    key3 = ['diary', 'show', 'letter', 'note', 'tree house']
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        gl_end_me()
    elif housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        gl_threaten()
    elif housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        gl_diary_show()
    else:
        gl_no_kill()


def gl_end_me():
    rooms_intro.gl_end_me()

    key1 = ['yes', 'i do', 'kill', 'dead', 'end']
    key2 = ['no', 'i don\'t', 'do not', 'will not']
    key3 = ['leave', 'turn back'] 
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        gl_dead()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        gl_no_kill()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        gl_no_kill_leave()
    else:
        gl_no_kill_stay()

def gl_dead():
    rooms_intro.gl_dead()

    gl_end = True

    blood = "blood"

    return_clearing()

def return_clearing():

    rooms_intro.return_clearing()

    key1 = ['investigate', 'tree house', 'tree']
    key2 = ['cave', 'trace', 'steps', 'GL']
    key3 = ['dock', 'docks', 'ship', 'return'] 
    key4 = ['pyramid', 'door', 'straight', 'continue']
    key5 = ['no way']

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        tree_house()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        follow_steps()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        still_on_dock()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        try:
            blood
            door_return()
        except NameError: 
            door_return_refuse()
    else:
        door_return()

def gl_no_kill():
    rooms_intro.gl_no_kill()

    key1 = ['stay', 'wait', 'watch', 'nothing']
    key2 = ['leave', 'turn back', 'return', 'docks']
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        gl_no_kill_stay()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
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
                            key2, key3, key4, key5) == "door1":
        gl_end_me()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        path_back()
    else:
        gl_end_me()

def path_back():
    rooms_intro.path_back()

    key1 = ['investigate', 'tree house', 'tree']
    key2 = ['cave', 'trace', 'steps']
    key3 = ['dock', 'docks', 'ship', 'return'] #add a key here?
    key4 = ['pyramid', 'door', 'approach'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        tree_house()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        follow_steps()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        still_on_dock()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door4":
        try:
            blood
            door_return()
        except NameError: 
            door_return_refuse()
    else:
        default_forest()  

def clearing_path():
    rooms_intro.clearing_path()

    key1 = ['investigate', 'tree house', 'tree']
    key2 = ['cave', 'trace', 'steps', 'follow', 'marked', 'path']
    key3 = ['dock', 'docks', 'ship', 'return', 'leave'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        tree_house()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        follow_steps()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        still_on_dock()
    else:
        default_forest()  

def path_right():
    saintsbeach.rocky_path()


    key1 = ['yes', 'continue', 'path', 'walk']
    key2 = ['no', 'go back', 'leave', 'warmth', 'docks'] 
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    
    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        rocky_path_continue()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        rocky_path_return()
    else:
        rocky_path_continue

def rocky_path_return():
    saintsbeach.rocky_path_return()

    key1 = ['pyramid', 'door', 'approach door', 'straight']
    key2 = ['wooded path', 'left', 'woods'] 
    key3 = ['return', 'cold damp', 'right']
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        door_with_no_knob()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        path_left()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        rocky_path_continue()
    else:
        rocky_path_decide()

def rocky_path_decide():
    saintsbeach.rocky_path_decide()

    key1 = ['pyramid', 'door', 'approach door', 'straight']
    key2 = ['wooded path', 'left', 'woods'] 
    key3 = ['return', 'cold damp', 'right']
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here? 

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        door_with_no_knob()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        path_left()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        rocky_path_continue()
    else:
        rocky_path_decide()


def rocky_path_continue():
    saintsbeach.rocky_path_continue()

    key1 = ['yes', 'continue', 'path', 'right', 'walk', 'press on', 'press']
    key2 = ['no', 'go back', 'leave', 'warmth', 'turn back']
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here? 
    
    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        beach_enter()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        default_from_dock()
    else:
        rocky_path_decide()

def beach_enter():
    saintsbeach.beach_enter()

    key1 = ['altar', 'obsidian', 'stone', 'large', 'block']
    key2 = ['path', 'cliffs', 'beach', 'narrow'] 
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?
    
    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        altar_investigate()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        cliff_investigate()
    else:
        rocky_path_decide()

def altar_investigate():
    saintsbeach.altar_investigate()

    key1 = ['return', 'head back', 'walk', 'way']
    key2 = ['path', 'head down', 'beach', 'narrow', 'unknown'] 
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?
    
    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        rocky_path_return()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        path_under_cliffs()
    else:
        cliff_investigate()

def cliff_investigate():
    saintsbeach.cliff_investigate()

    path_under_cliffs()

def path_under_cliffs():
    saintsbeach.path_under_cliffs()

    key1 = ['return', 'head back', 'walk', 'way', 'turn around']
    key2 = ['look down', 'hand', 'broken', 'look', 'unknown'] 
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?
    
    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        tunnel_turn_back()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        look_down()
    else:
        look_down()

def look_down():
    saintsbeach.look_down()

    key1 = ['return', 'head back', 'walk', 'way', 'turn around']
    key2 = ['investigate', 'stay', 'continue', 'dig', 'gross'] 
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?
    
    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        tunnel_turn_back()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        cave_stay()
    else:
        cave_stay()

def tunnel_turn_back():
    saintsbeach.tunnel_turn_back()

    cliff_path_return()

def cave_stay():
    key1 = ['return', 'head back', 'walk', 'way', 'turn around']
    key2 = ['investigate', 'stay', 'continue', 'dig', 'take bone', 'pocket'] 
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?
    
    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        tunnel_turn_back()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        take_bone()
    else:
        tunnel_turn_back()

def take_bone():
    saintsbeach.take_bone()

    saintsbeach.cliff_path_return()

def cliff_path_return():
    saintsbeach.cliff_path_return()

    key1 = ['return', 'head back', 'walk', 'way', 'turn around']
    key2 = ['wallow', 'stay', 'beach', 'discomfort'] 
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?
    
    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        rocky_path_return()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        beach_wallow()
    else:
        beach_wallow()

def beach_wallow():
    saintsbeach.beach_wallow()

    rocky_path_return()

def door_return_refuse():
    fortress.door_return_refuse()
    door_return()

def door_return():
    fortress.door_return()

    key1 = ['yes', 'yeah', 'ready', 'judgement']
    key2 = ['no', 'not ready', 'leave'] 
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?
    
    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        door_return_yes()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        door_return_no()
    else:
        door_return_no()

def door_return_yes():
    fortress.door_return_yes()
    
    key1 = ['yes', 'yeah', 'ready', 'succumb', 'desire']
    key2 = ['no', 'not ready', 'leave'] 
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        door_judgement()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        door_judgement_resist()
    else:
        door_judgement()

def door_return_no():
    fortress.door_return_no()
    door_judgement()

def door_judgement():
    fortress.door_judgement()

    key1 = ['yes', 'yeah', 'ready', 'enter', 'fortress']
    key2 = ['no', 'not ready', 'leave', 'dock'] 
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        enter_fortress()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        door_judgement_resist()
    else:
        enter_fortress()


def door_judgement_resist():
    fortress.door_judgement_resist()
    enter_fortress()


def enter_fortress():
    fortress.enter_fortress()

    key1 = ['yes', 'yeah', 'creature', 'address', 'mythic creatrue']
    key2 = ['investigate', 'marble buildings', 'marble'] 
    key3 = ['move', 'shining', 'shell']
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?


    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        faceless_sphinx_approach()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        barracks_investigate()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        pyramid_approach()
    else:
        faceless_sphinx_approach()


def faceless_sphinx_approach():
    fortress.faceless_sphinx_approach()
    
    key1 = ['question', 'ask', 'talk']
    key2 = ['presence', 'not ready', 'leave', 'dock'] 
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        sphinx_defer()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        sphinx_defer()
    else:
        sphinx_defer()


def sphinx_defer():
    fortress.sphinx_defer()

    key1 = ['taymor', 'grandfather', 'letter', 'ship']
    key2 = ['murex', 'shining', 'shell']
    key3 = ['diary', 'GL', 'treehouse']
    key4 = ['kill', 'punch', 'push', 'yell', 'aggression']
    key5 = ['beach', 'rocky', 'shore']

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        sphinx_taymor()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        sphinx_murex()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        sphinx_diary()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door4":
        sphinx_beach()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door5":
        sphinx_aggression()
    else:
        sphinx_taymor()

def sphinx_defer():
    fortress.sphinx_defer()

    key1 = ['taymor', 'grandfather', 'letter', 'ship']
    key2 = ['murex', 'shining', 'shell']
    key3 = ['diary', 'GL', 'treehouse']
    key4 = ['kill', 'punch', 'push', 'yell', 'aggression']
    key5 = ['beach', 'rocky', 'shore']

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        sphinx_taymor()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        sphinx_murex()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        sphinx_diary()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door4":
        sphinx_beach()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door5":
        sphinx_aggression()
    else:
        sphinx_taymor()

def sphinx_murex():
    fortress.sphinx_murex()
    sphinx_default()

def sphinx_diary():
    fortress.sphinx_diary()
    sphinx_default()

def sphinx_beach():
    fortress.sphinx_beach()
    sphinx_default()

def sphinx_taymor():
    fortress.sphinx_taymor()
    
    key1 = ['taymor', 'yes', 'divinity', 'sacrifice', 'prepared']
    key2 = ['no', 'kill', 'return']
    key3 = ['do not know', 'don\'t know'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        sphinx_taymor_yes()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        sphinx_taymor_no()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        sphinx_unsure()
    else:
        sphinx_default()

def sphinx_taymor_yes():
    fortress.sphinx_unsure()

    fortress_reassess()       

def sphinx_taymor_yes():
    fortress.sphinx_taymor_yes()

    fortress_reassess()

def sphinx_taymor_no():
    fortress.sphinx_taymor_no()

    fortress_reassess()

def sphinx_default():
    fortress.sphinx_default()

    key1 = ['taymor', 'grandfather', 'letter', 'ship', 'mother']
    key2 = ['murex', 'shining', 'shell']
    key3 = ['diary', 'GL', 'tree house']
    key4 = ['kill', 'punch', 'push', 'yell', 'aggression']
    key5 = ['beach', 'rocky', 'shore']

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        sphinx_taymor()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        sphinx_murex()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        sphinx_diary()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door4":
        sphinx_beach()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door5":
        sphinx_aggression()
    else:
        fortress_reassess()

def fortress_reassess():
    fortress.fortress_reassess()

    key1 = ['sphinx', 'question', 'creature', 'address', 'mythic creatrue']
    key2 = ['investigate', 'marble structures', 'marble'] 
    key3 = ['move', 'shining', 'shell', 'pyramid', 'press']
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        sphinx_return()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        barracks_investigate()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        pyramid_approach()
    else:
        sphinx_return()

def sphinx_return():
    fortress.sphinx_return()
    fortress_reassess()

def barracks_investigate():
    fortress.barracks_investigate()

    choice_number = raw_input("> ")

    if int(choice_number) % 2 == 0:
        barracks_even()
    else:
        barracks_odd()

def barracks_odd():
    fortress.barracks_odd()

    key1 = ['chair', 'wooden', 'wall', 'cushion' 'sit']
    key2 = ['bed', 'single', 'neatly', 'under']
    key3 = ['book', 'nightstand', 'purple']
    key4 = ['chamber', 'pot', 'glistening', 'copper']
    key5 = ['window']

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        odd_chair()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        odd_under_bed()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        odd_book()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door4":
        odd_chamber_pot()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door5":
        odd_bed()
    else:
        odd_default()

def odd_chair():
    fortress.odd_chair()
    odd_default()

def odd_under_bed():
    fortress.odd_under_bed()
    odd_default()

def odd_bed():
    fortress.odd_bed()
    odd_default()

def odd_chamber_bed():
    fortress.odd_chamber_bed()
    odd_default()

def odd_book():
    fortress.odd_book()

    key1 = ['read', 'book', 'open', 'inside']
    key2 = ['put it back', 'close']
    key3 = ['leave', 'exit', 'pyramid', 'return'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        odd_book_read()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        odd_default()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        leave_barracks()
    else:
        odd_book_read()

def odd_book_read():
    fortress.odd_book_read()
    odd_default()

def odd_default():
    fortress.odd_default()

    key1 = ['chair', 'wooden', 'wall']
    key2 = ['bed', 'single', 'neatly', 'under']
    key3 = ['book', 'nightstand', 'purple']
    key4 = ['chamber pot', 'glistening', 'copper']
    key5 = ['touch bed', 'lie', 'sleep']

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        odd_chair()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        odd_under_bed()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        odd_book()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door4":
        odd_chamber_pot()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door5":
        odd_bed()
    else:
        leave_barracks()


def barracks_even():
    fortress.barracks_even()

    key1 = ['chair', 'overturned', 'right', 'sit']
    key2 = ['bed', 'lie', 'sleep', 'mussed'] 
    key3 = ['chamber pot', 'copper', 'under bed', 'crouch']
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?


    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        even_upright_chair()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        even_bed()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        even_chamber_pot()
    else:
        even_default()

def even_upright_chair():
    fortress.even_upright_chair()
    even_default()

def even_bed():
    fortress.even_bed()
    even_default()

def even_chamber_pot():
    fortress.even_chamber_pot()
    even_must_leave()

def even_must_leave():
    fortress.even_must_leave()

    leave_barracks()

def even_default():
    fortress.even_default()

    key1 = ['chair', 'overturned', 'right', 'sit']
    key2 = ['bed', 'lie', 'sleep', 'mussed'] 
    key3 = ['chamber pot', 'copper', 'under bed', 'crouch']
    key4 = ['leave', 'depart', 'pyramid']
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        even_upright_chair()
    elif housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        even_bed()
    elif housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        even_chamber_pot()
    elif housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door4":
        leave_barracks()
    else:
        even_default()

def leave_barracks():
    fortress.leave_barracks()

    key1 = ['sphinx', 'question', 'creature', 'address', 'mythic creatrue']
    key2 = ['investigate', 'marble structures', 'marble'] 
    key3 = ['move', 'shining', 'shell', 'pyramid', 'press']
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        sphinx_return()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        barracks_investigate()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        pyramid_approach()
    else:
        fortress_reassess()

def pyramid_approach():
    endgame.pyramid_approach()
    
    key1 = ['hit', 'attack', 'slap', 'hurt', 'kick', 'punch']
    key2 = ['ask', 'question', 'investigate', 'why'] 
    key3 = ['taymor', 'letter', 'grandfather', 'GL']
    key4 = ['push', 'past', 'forward', 'pyramid']
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        dobbins_attack()
    elif housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        dobbins_question()
    elif housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        dobbins_taymor()
    elif housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door4":
        dobbins_hurry_forward()
    else:
        dobbins_other()

def dobbins_attack():
    endgame.dobbins_attack()

    key1 = ['yes', 'enter', 'pyramid', 'push past']
    key2 = ['no', 'return', 'docks', 'do not', 'stay'] 
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?


    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        pyramid_enter()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        pyramid_other()
    else:
        pyramid_other()

def dobbins_question():
    endgame.dobbins_question()

    key1 = ['slap', 'hit', 'strike', 'attack', 'violence']
    key2 = ['no', 'return', 'docks', 'do not', 'stay'] 
    key3 = ['no way'] #add a key here?
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?

    scanned_input = housekeeping.ask_input()

    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        dobbins_attack()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        pyramid_other()
    else:
        pyramid_other()


def dobbins_taymor():
    endgame.dobbins_taymor()

    key1 = ['slap', 'hit', 'strike', 'attack']
    key2 = ['apprach', 'move', 'forward', 'pyramid', 'walk'] 

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                                     key2) == "door1":
        dobbins_attack()
    elif  housekeeping.match_input(scanned_input, key1, 
                                     key2) == "door2":
        pyramid_second_approach()
    else:
        dobbins_hurry_forward()


def dobbins_other():
    endgame.dobbins_other()

    pyramid_enter()

def dobbins_hurry_forward():
    endgame.dobbins_hurry_forward()
    
    pyramid_enter()

def pyramid_second_approach():
    endgame.pyramid_second_approach()

    pyramid_enter()

def pyramid_other():
    endgame.pyramid_other()

    pyramid_enter()

def pyramid_enter():
    endgame.pyramid_enter()

    key1 = ['yes', 'hug', 'great-grandfather', 'embrace']
    key2 = ['no', 'no way', 'leave', 'refuse'] 
    key3 = ['attack', 'kill', 'stab', 'punch', 'hit', 'slap']
    key4 = ['question', 'what', 'who', 'where']
    key5 = ['why']

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door1":
        taymor_hug()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door2":
        hug_no()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door3":
        taymor_attack()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door4":
        taymor_question()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door5":
        taymor_speech()
    else:
        taymor_other()

def taymor_hug():
    endgame.taymor_hug()

    key1 = ['yes', 'help', 'great-grandfather', 'embrace', 'divine work']
    key2 = ['no', 'refuse', 'no way', 'leave', 'recoil'] 
    key3 = ['attack', 'kill', 'stab', 'punch', 'hit', 'slap']
    key4 = ['question', 'what', 'why', 'who', 'where']
    key5 = ['why']

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door1":
        hug_yes()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door2":
        hug_no()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door3":
        taymor_attack()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door4":
        taymor_question()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door5":
        taymor_speech()
    else:
        taymor_other()

def hug_yes():
    endgame.hug_yes()

    key1 = ['yes', 'hug', 'embrace', 'great one', 'give in']
    key2 = ['no', 'refuse', 'no way', 'leave', 'recoil'] 
    key3 = ['attack', 'kill', 'stab', 'punch', 'hit', 'slap']
    key4 = ['question', 'what', 'who', 'where']
    key5 = ['why']

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door1":
        taymor_embrace_divinity()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door2":
        hug_no()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door3":
        taymor_attack()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door4":
        taymor_question()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door4":
        taymor_speech()
    else:
        taymor_other()

def hug_no():
    endgame.hug_no()

    key1 = ['yes', 'hug', 'embrace', 'great one', 'give in']
    key2 = ['no', 'refuse', 'attempt', 'escape', 'leave', 'recoil'] 
    key3 = ['attack', 'kill', 'stab', 'punch', 'hit', 'slap', 'violence']
    key4 = ['question', 'what', 'who', 'where']
    key5 = ['why']

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        taymor_embrace_divinity()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        hug_no_ascension()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        taymor_attack()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door4":
        taymor_question()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door4":
        taymor_speech()
    else:
        taymor_other()

def hug_no_ascension():
    endgame.hug_no_ascension()

def taymor_question():
    endgame.taymor_question()

    key1 = ['yes', 'hug', 'embrace', 'great one', 'give in']
    key2 = ['no', 'refuse', 'attempt', 'escape', 'leave', 'recoil'] 
    key3 = ['attack', 'kill', 'stab', 'punch', 'hit', 'slap']
    key4 = ['why']
    key5 = ['no way'] #add key here

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door1":
        taymor_embrace_divinity()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door2":
        hug_no_ascension()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door3":
        taymor_attack()
    elif  housekeeping.match_input(scanned_input, key1, 
                        key2, key3, key4, key5) == "door4":
        taymor_speech()
    else:
        taymor_other()
    

def taymor_attack():
    endgame.taymor_attack()

    key1 = ['yes', 'hug', 'embrace', 'accept', 'take', 'hand']
    key2 = ['no', 'refuse', 'attempt', 'escape', 'leave', 'recoil'] 
    key3 = ['attack', 'kill', 'stab', 'punch', 'hit', 'slap']
    key4 = ['question', 'what', 'who', 'where']
    key5 = ['why']

    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door1":
        taymor_embrace_divinity()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door2":
        hug_no_ascension()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door3":
        taymor_attack_again()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door4":
        taymor_question()
    elif  housekeeping.match_input(scanned_input, key1, 
                                key2, key3, key4, key5) == "door5":
        taymor_speech()
    else:
        taymor_attack_again()

def taymor_speech():
    endgame.taymor_speech()

    key1 = ['accept', 'embrace', 'take', 'hold', 'hands']
    key2 = ['refuse', 'recoil', 'leave'] 
    key3 = ['attack', 'kill', 'stab', 'punch', 'hit', 'slap']
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?


    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        taymor_embrace_divinity()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        hug_no_ascension()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        taymor_attack()
    else:
        taymor_other()

def taymor_other():
    endgame.taymor_other()
    
    key1 = ['accept', 'embrace', 'take', 'hold', 'hands']
    key2 = ['refuse', 'recoil', 'leave'] 
    key3 = ['violence', 'attack', 'kill', 'stab', 'punch', 'hit', 'slap']
    key4 = ['no way'] #add a key here?
    key5 = ['no way'] #add a key here?


    scanned_input = housekeeping.ask_input()
    
    if housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door1":
        taymor_embrace_divinity()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door2":
        taymor_attack_again()
    elif  housekeeping.match_input(scanned_input, key1, 
                            key2, key3, key4, key5) == "door3":
        taymor_attack()
    else:
        taymor_other()

def taymor_embrace_divinity():
    endgame.taymor_embrace_divinity()


start()