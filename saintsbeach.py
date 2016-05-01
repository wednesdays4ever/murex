### Hey reader! A note:
## This is one of the four main files containing the text of the game.
# The others are fortress.py, saintsbeach.py and endgame.py

def rocky_path():
	print """ 
	You descend the rocky path. 
	Soon the docks and compound disappear from view.
	You were sweating the entire trip to the island,
	unbearable heat is all that you can remember for days.
	But with every step, your temperature lowers,
	the ground turns to dark mud and you begin to shiver.

	Do you continue,
	or return to warmth?
	"""

def rocky_path_return():
	print """ 
	You find yourself at the same crossroads.
	The door lies ahead.
	A wooded path leads off to the left,
	and the cold damp way stretches back the way
	you just returned from.
	To where do you turn?"""

def rocky_path_decide():
	print """
	You shiver as you stand stationary.
	Continue to the right, go to the left, or head to the door?"""

def rocky_path_continue():
	print """ 
	As you press on, the chill does not leave you.
	Your feet sink deeper into black earth
	that looks dark purple in the shadows.
	Damp rocks stretch high on either side,
	and press in against your shoulders.

	Your soles and your bladder tingle.
	A pain appears behind your eyebrows,
	and tears begin to well up in your eyes.

	There is a bad feeling here,
	but you are here to discover.
	Do you press on or turn back?
	"""
	#press on is beach, return is all the way back

def beach_enter():
	print """ 
	The thin path opens up onto a stunning beach,
	dotted with palm trees and covered in lavender sand.

	The fact that the ground is purple is almost less
	disturbing than the chest-tightening fear that
	floods your body.

	A large obsidian block is 
	positioned in the center of the beach,
	and another narrow path stretches 
	off further down the beach.

	Where do you go?
	"""
	#lavender sand see altar, path near cliffs

def altar_investigate():
	print """ 
	The shining black rectangle is large enough 
	for a large man to lie across 
	with space to spare 
	and situated parallel to the waves.

	In the center, a silver plaque reads:

	7 SERVANTS PERISHED HERE
	IN THE MIRACULOUS AND AWAKENING WAVE
	SURVIVED AND SPOKEN OF BY
	HIGH PRIEST HUNTINGDON

	Your great-grandfather was a high priest.
	Maybe he really is here for something important.

	The waves lap the purple sand.
	Two paths stretch behind you.
	Do you return the way you came,
	or head down the unknown path?"""

def cliff_investigate():
	print """ 
	It doesn't seem like you 
	could have descended from so high,
	but you need to crane your neck 
	to see the top of these cliffs.

	To look up at them gives you a sense of vertigo,
	even though you are far below."""
	#you feel a sense of vertigo even though you are firmly rooted on the ground

def path_under_cliffs():
	print """ 
	You suppress your uneasiness and head forward.
	This path is even narrower than the one that lead
	you to the beach.
	Soon, the two sides connect and force you into a crawl.

	The tunnel narrows in further and further
	and less and less light leaks in this deep.
	Just as you are beginning to wonder if you should
	turn back, the palm of your hand lands on something
	that cracks beneath it.

	Do you turn around, or look at what your hand
	has broken?"""

def look_down():
	print """ 
	Bones.
	Undeniably, old dry bones.

	You scurry forward to get away from the rest
	of the skeleton
	and find yourself in a small circular cave.

	When you sit down and pause to catch your breath,
	you realize that you've escaped nothing,
	this cavern is littered with even more
	human remains."""

## This should be a Look Around. 
def skeleton_investigate():
	print """ 
	You count seven skulls and assorted bones
	that you assume make up seven skeletons
	in the dim light.

	This mass grave makes your soul shiver."""

def cave_stay():
	print """ 
	Further investigation might have been fruitful,
	but every time you look at a skull,
	you see the face that used to cover it,
	and hear the man's voice that once came out.

	You aren't sure what you expected,
	but you were not prepared for this.

	A flood of vomit surprises you as it pours from 
	your mouth.

	You crawl away as you realize it has settled
	into a puddle around one of the seven skulls."""

def tunnel_turn_back():
	print """ 
	You skitter like a mouse
	back out of the tunnel.
	You're not sure if you've learned much else
	besides the fact that bad things have happened here.
	"""

def take_bone():
	print """ 
	It is a morbid thought,
	but it is true that something feels mystical
	and perhaps darkly holy about this place.
	A relic from here could prove useful.
	"""

def cliff_path_return():
	print """ 
	You are surprised that you feel no relief
	when the path opens back up.

	In the distance, you see the ship that 
	brought you here finally fading out into the distance.

	An intense feeling of loneliness and despair
	is almost strong enough to unseat
	the supernatural unease that this place
	gives you.

	Do you head away from this place?
	Or wallow in your discomfort?
	"""
#rocky_path_return if you leave
def beach_wallow():
	print """ 
	Tears come almost immediately.
	You remember a moment on an elementary school bus,
	when you wet yourself and the seat that you shared
	with your teacher.
	She slapped your wrist hard when she felt your
	urine beneath her,
	and screamed so that the whole class heard.
	This lost feeling of helplessness and shame
	is similar to that one,
	and it would really be best if you fled from it.
	"""



