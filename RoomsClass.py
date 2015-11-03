import Ship_Awaken

class MurexRoom(object):
	def __init__(self, intro, observation):
		self.intro = intro
		self.clue = observation
		intro = "You shiver."
		clue = "Nothing of note"

	def scan_input(self, raw):
		lowered = raw.lower()
		scanned_input = lowered.split(' ')
		return scanned_input 

class Start(MurexRoom):
	def __init__(self):
		super(MurexRoom, self).__init__()

	intro = """
	Welcome to the world of SECRETS OF THE MUREX
	Unveil our mystery. Carry our tradition. Answer our call.
	We depend on you.


	"Enter BEGIN to approach the island."
	"""
	print intro
	choice =raw_input("> ")

	key = ['begin']

	if "yes" in choice:
		ShipAwaken()
	else:
		ShipAwaken()

Start()