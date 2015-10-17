class MurexRoom(object):
	def __init__(self, intro, clue):
		self.intro = intro
		self.clue = clue
		intro = "You shiver."
		clue = "Nothing of note"


class GoldRoom(MurexRoom):
	def __init__(self):
		super(MurexRoom, self).__init__()

	clue = "The gold is worth millions"
	intro = "The room is shimmering"

	print intro
	choice = raw_input("> ")

	if "clue" in choice: 
		print clue
