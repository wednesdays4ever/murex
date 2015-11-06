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
	print """
	Welcome to the world of SECRETS OF THE MUREX
	Unveil our mystery. Carry our tradition. Answer our call.
	We depend on you.

	"""
	#sleep(1) #This waits a moment between printing messages
	print "Enter BEGIN to approach the island."

	choice = scan_input(raw_input("> "))

	key = ['begin']

	if match_input == True:
		ship_awaken()
	else:
		ship_awaken()

def ship_awaken():
	print """ For days you've dreamed of the sight of land,
but the tiny island that lies on the horizon does nothing to quell the uneasy feeling you've had this entire trip.
Seasickness has kept your mouth sour for the week you've been on the boat, and this morning is no different.
Some distant spire catches the sun and glints impossibly bright, making your headache even worse.
You close your eyes and recoil, stepping back from your vantage point and directly into the ship's captain.
He glares down at you. Do you apologize? Or run away? """
	
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
	print """ The Captain sighs at your apology.
I WAS BORN WITH A HARD FACE AND THE WEATHER HAS NOT BEEN KIND TO IT.
IT IS MY CURSE TO BE FOREVER FRIGHTENING TO STRANGERS, WHEN ALL I MIGHT LIKE IS TO LET THEM KNOW THE WARMTH I HAVE TO OFFER.
You are rendered speechless by the Captain's confession.
He looks up at the sky as if he's forgotten you're there.
THAT THE SKY CAN BE SO BRIGHT AND CLEAR AND BEAUTIFUL WITH SO MANY TERRIBLE THINGS SWIRLING AROUND BENEATH IT.
IT'S PAINFUL.
THAT'S A QUOTE FROM SOMEWHERE.
He sighs again. Your sympathy for this sad man has turned to boredom bordering on disgust, and he can sense the shift.
BE THERE SOON, HOPE YOU KNOW WHAT YOU'RE GETTING INTO, he says before he clomps away, leaving you alone again.
Was that a threat? What are you getting yourself into?
You thumb the edges of the thick envelope the letter from your late great-grandfather came in.
You've read it over and over so many times, but still, nothing makes much sense.
Do you read it again? Or watch the sea and wait to dock? """
	
	choice = scan_input(raw_input("> "))

	if "read" in choice or "letter" in choice or "open" in choice:
		read_letteri()
	elif "watch" in choice or "sea" in choice or "wait" in choice:
		wait_dock()
	else:
		read_letterii()

def captain_ii():
	print """I HOPE YOU KNOW WHAT YOU'RE GETTING INTO, you hear the sad and ugly captain call as you run to the other side of the ship.
You catch your breath here and feel the breeze in your hair. It eases the pain of your headache."
You go back over in your mind the Captain's words, and the rest of the laconic crew's attitude during the entirety of the trip.
What are they afraid of you learning? Do they even know?
You thumb the edges of the thick envelope the letter from your late great-grandfather came in.
You've read it over and over so many times, but still, nothing makes much sense.
Do you read it again? Or watch the sea and wait to dock? """
	choice = scan_input(raw_input("> "))

	if "read" in choice or "letter" in choice or "open" in choice:
		read_letteri()
	elif "watch" in choice or "sea" in choice or "wait" in choice:
		wait_dock()
	else:
		read_letterii()

def captain_iii():
	print """ He sighs.
It is unlikely that he has had any recent contact with a young girl like you, and appears to read all of your actions as nonsense.
BE THERE SOON, HOPE YOU KNOW WHAT YOU'RE GETTING INTO, he says before he clomps away, leaving you alone again."
Was that a threat? What are you getting yourself into?
You thumb the edges of the thick envelope the letter from your late great-grandfather came in.
You've read it over and over so many times, but still, nothing makes much sense.
Do you read it again? Or watch the sea and wait to dock? """
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
	print """ Something compels you to open the well worn envelope one more time before you dock.
You slide your finger across the dark blue wax seal, stamped with the shape of a strange and spiny, spiral seashell.
Your great-grandfather's handwriting stands out in green ink that almost glows against the thick, cream paper. """
	print letter
	choice = scan_input(raw_input("> "))

	if "childhood" in choice or "visit" in choice:
		visit_memory()
	elif "stories" in choice or "story" in choice or "mother" in choice:
		mother_story()
	else:
		dock_arrivei()

def visit_memory():
	print "The man's face is a shadow, but you recall your mother in an intense argument with him."
	print "You were very young,"
	print "Sent upstairs, but you disobeyed. You sat just behind the kitchen door, trying to make sense of their yelling."
	print "SHE IS THE ONE I'VE BEEN WAITING FOR! and YOU'RE CRAZY! are the only two phrases that have stuck with you."
	print "You remember not being able to sleep that night, wondering if you were being held back from some great adventure."
	print "Perhaps that's why you didn't tell your mother when you received the letter,"
	print "or when you bought your ticket."
	print "Well, you've made your decision, and there's nothing she can do to prevent you now."
	print "You feel the ship's bow knock against the island's dock."
	print "You've arrived."
	print "No one is here to meet you, but your eyes catch the note nailed to the dock post, and see a path leading to the rest of the island ahead."

	choice = scan_input(raw_input("> "))


	if "note" in choice or "nailed" in choice:
		dock_note()
	elif "path" in choice or "island" in choice:
		pathi()
	else:
		dock_fill()

def mother_story():
	print "Your mother would only speak about her grandfather Taymor when she was really pushed to do it."
	print "When you did push her to the limit, something changed in her eyes."
	print "She wasn't your mother anymore, she was a scared and confused young woman."

def wait_dock():
	print """ You stare at the island as the ship approaches.
Something about the bright glint in the distance won't let you look away. 
You can't quite make out its source, but it is hopelessly mesmerizing.
You can only rip your eyes away when you feel the ship bump against the dock with a hard wooden knock.
Before you realize what is happening, the crew has shuffled you off the deck, thrown your bag at your feet, and set sail once more.
The letter that sent you here in the first pokes against your ribs from inside your pocket. 
A note is nailed to one of the posts on the dock.
Do you read the note? Or revisit the letter from your great-grandfather? """
	choice = scan_input(raw_input("> "))


	if "note" in choice or "nailed" in choice:
		dock_note()
	elif "letter" in choice or "great-grandfather" in choice:
		read_letteriii()
	else:
		dock_fill()

def dock_note():
	pass

def read_letteriii():
	print """ Now that you're actually here, all alone, a small panic hits you.
Thinking that there might be something to glean from one more read, you pull your great-grandfather's letter from your pocket.
You slide your finger across the dark blue wax seal, stamped with the shape of a strange and spiny, spiral seashell.
Your great-grandfather's handwriting stands out in green ink that almost glows against the thick, cream paper. """
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
	print """ You stare at the island as the ship approaches.
Something about the bright glint in the distance won't let you look away. 
You can't quite make out its source, but it is hopelessly mesmerizing.
You can only rip your eyes away when you feel the ship bump against the dock with a hard wooden knock.
Before you realize what is happening, the crew has shuffled you off the deck, thrown your bag at your feet, and set sail once more.
The letter that sent you here in the first pokes against your ribs from inside your pocket. 
A note is nailed to one of the posts on the dock.
Do you read the note? Or revisit the letter from your great-grandfather? """
	choice = scan_input(raw_input("> "))

	if "note" in choice or "nailed" in choice:
		dock_note()
	elif "letter" in choice or "great-grandfather" in choice:
		read_letteriii()
	else:
		dock_fill()

start()
