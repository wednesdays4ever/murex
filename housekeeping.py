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
		APRIL, EXPECTANS ANNIS IV

	Great, great strides have been made.
	Early setbacks have been overcome, 
	and the group that first arrived four years ago 
	remains on the divine course ordained for us.
	Our fortress is complete and I do believe that 
	it is worthy of the One we serve. 
	Discovery continues. 
	My bones vibrate with possibility.
	To harness the Great One's power 
	is to change this imperfect world forever.
	Hope slides toward us, 
	in the violet sunset, 
	across the horizon.


		JANUARY, EXPECTANS ANNIS V

	It is snowing at home, I imagine.
	At the outset, I believed that Angela would
	be by my side again by this time.
	The pangs of homesickness and doubt
	and mistrust of my fellow servants
	may be embraced as proof that I am only
	an imperfect human leader.
	Ultimately, 
	the Great One's consciousness will consume mine,
	and all uncertainty will cease.


		MARCH, EXPECTANS ANNIS V

	Seven of our number have drowned at the Holy Beach.
	High Priest Huntingdon was the only one to return 
	from what should have been a typical salute to the sea.
	He claims that as they knelt and he led them in the Deference,
	a great wave larger than any he'd seen before
	rose up and crashed down upon them.
	When it washed away, he was the only one standing.
	The seven had been ripped out to sea.
	Huntingdon sees this as a sign that
	the Great One is ready to approach us,
	but is frustrated and kept at bay by
	imperfections in our number.

	It is true that all of the drowned 
	had voiced controversial opinions during their time as servants.
	But in my memory,
	their words were directed at our High Priest himself, 
	and not with any disrespect to the one we serve.

	I am an imperfect servant,
	and suspicion clouds my grief.


		MAY, EXPECTANS ANNIS VII

	Exiled. 
	Kept from the house I built and pledged to serve.
	But we cannot leave the island where we believe
	the Great One will one day return,
	I wait here, in my makeshift study, 
	humiliated by the beautiful glimmer of the spire that
	tops the temple I built in service
	through this treehouse window.

	A small group of the devout have followed me here. 
	The Great One will know who was loyal.
	Taymor has abandoned reason, 
	he no longer seeks improvement of this world
	and only ascension for himself.
	Thoughts of the punishment he is sure to receive
	are my only comfort in isolation.
	
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
	