import housekeeping

class MurexRoom(object):
	"""A room in Secrets of Murex with the following properties:
	   
	   Attributes:
	   intro: The inital text that prints.
	   observation: What a user will see if they look around.
	   notebook_entry: What is added to the notebook from this room."""
	 
	 __metaclass__ = ABCMeta

	def __init__(self, intro, observation, notebook_entry):
		self.intro = intro
		self.observation = observation
		self.notebook_entry = notebook_entry
		room_visited = False

	def play_room(self):
		print self.intro
		room_visited = True
		housekeeping.ask_input()