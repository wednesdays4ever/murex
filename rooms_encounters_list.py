rooms_encounters_list.py

def path_from_dock():
	print """ You can see the tip of what must be the Great Pyramid far off in the distance, beyond a giant stone wall. 
The path ahead leads away from the dock and splits in three directions.
One straight ahead toward a door in the stone island fortress.
Another forks to the left toward a sparse wood, removed from the stone walls and hugging the rocky shore.
The path to the right drops off and out of sight. There may be cliffs ahead.
The waves crash and the wind whistles at your back. You know you must proceed, but in which direction?"""

def door_with_no_knob():
	print """ What appeared to be a door from a distance has no handle.
Carved in to the surface is a single, enormous closed eye, 
perched atop a massive, winding shell, taller than a man, 
with spines longer than your legs stretching out from it at every angle.
Your great-grandfather and the reason you're here wait somewhere behind this wall, 
but there is no obvious way to open it."""

def push_or_pull_door():
	print """ The giant eye springs open, impossibly.
Beneath the stone lid, there is the real shining eye of some living creature.
It glistens like a man's would in this light. It reflects back the waves behind you, flipped and magnified.
You are in shock and lost in the world of the eye that is larger than the car you drive to work, 
when you see it narrow into a glare and hear a thin voice enter your mind from no obvious origin.
SMALL CREATURE. WHY DO YOU COME? """

def door_eye_answer():
	print """ LONG AGO, ENTRANCE WAS FOR ALL, BUT HERETICS HAVE CLOSED OUR DOORS.
THE SECRETS INSIDE ARE SAFE BEHIND ME. I WILL OPEN ONLY FOR THE CHOSEN ONES AND THEIR SERVANTS.
ARE YOU MEANT TO ENTER?"""

def door_eye_other():
	print """ IF THIS IS SOME SORT OF JOKE IT IS UNACCEPTABLE.
I WAS AWAKENED BY THE CHOSEN TO GUARD HIS SECRETS, NOT ENTERTAIN HIS VISITORS.
DISTURB ME AGAIN AT YOUR OWN PERIL.

The eye is a slit now, it waits for your next move."""

def door_eye_name():
	print """ I AM YORHAM.
I ASSUME, IF YOU ARE HERE HONORABLY, THAT YOU KNOW MY PURPOSE.
I ASK AGAIN, ARE YOU MEANT TO ENTER? """

def door_eye_attempt_enter():
	print """ IT IS TRUE, YOUR BLOOD SMELLS PURE, 
BUT YOUR INTENTIONS REMAIN A MYSTERY.
THERE IS A FEAR IN YOU THAT HAS YET TO BE SNUFFED BY THE GREAT ONE.
STEEL YOUR HEART BEFORE HE COMES.
DELIVERANCE LIES BEHIND MY WALLS ALONE """

def door_eye_not_chosen():
	print """ I DO NOT WASTE TIME WITH THOSE WHO DO NOT WALK OUR PATH.
BE GONE.
FIND THE GLOW OR NEVER RETURN.

With that, the eye snaps shut, 
and you are left alone again with a stone door that cannot be opened by human hands. """

def path_left():
	print """ The sand and rocks near the shore give way almost immediately to a firm, 
	well-worn dirt path.
It gets narrower as it winds into a thick, overgrown forest.
It is obvious that, while it has seen much use, not much care 
has been taken with its upkeep recently.
Do you head further into the forest? """

def forest_enter():
	print """ Dense and overgrown, it becomes harder and harder to follow the path.
Something about the thick air and large damp leaves reminds you of something.
Your mind goes back to a favorite film from your childhood, 
a nature tape about South America and its rainforests. 
You cannot remember its title now, but it was narrated by a cheerful, British voice, 
expounding on the countless layers of animal mystery in every centimeter of these 
remote areas of the world.
He encouraged you, while out in the world, 
to take a moment and listen to all that surrounds you.
You do this now, and your stomach sinks. 
This is a silent forest. 
You have left behind even the sound of the waves.
It lacks the life of your nature tape, 
of any other place you've ever set foot in this world.
You suddenly become aware of the swift thump of your heart. 
It is the only perceivable sound and it is less than comforting.
To proceed is to descend even further into silence, into dread.
To turn back is to learn nothing.
Indecision is not an option. """

def forest_ruins():
	print """ Moments after it felt as though the path would end in overgrowth, 
	it breaks open into a large, man made clearing.
A series of platforms and huts, elevated in the trees and strung together by rope bridges, 
sit above a central fire pit.
These signs of life bring you a moment of joy.
But then you realize, the silence persists.
Across the clearing, the path picks back up.
To your left, a rope ladder leads up to a tree house. """

def tree_house ():
	print """ This is not at all what you were expecting from the disarray in the clearing.
	This finished interior would be more fitting in an Ivy League library 
	than a makeshift building in the South Pacific.
	But the formerly beautiful room is in tatters.
	Some violence has happened here.
	Leatherbound books lay ripped apart and scorched on the dark, polished mahogany floor.
	A small side table with accompanying chess set lies overturned 
	next to a finely upholstered chair.
	This place must somehow be related to the compound.
	Could this have been Taymor's den? 
	Were you too late to respond to his letter?
	The room fills you with sadness,
	but if you're here to learn about your relative, this seems like a place to start.
	"""

def tree_house_inspect ():
	print """ Upon closer inspection, you notice a few things that seem out of the ordinary:
	The corner of a hardcover book peeking out from under the chair's cushion,
	The initials G.L. embossed on the back of the chair,
	and, gruesomely, scrawled in what looks like gore on the wall next to the opposite door
	THE END IS THE ONLY OUTCOME. WE WILL PREVAIL."""

def diary ():
	print """ The book is a diary. 
	A fine one, with a golden embossed G.L. on the cover,
	 that has seen much wear and tear.
	 Whoever G.L. was and whatever happened to him here are questions that cannot have pleasant answers.
	 But how can you know unless you ask?"""
	 

def open_diary ():
	print """ As soon as you open the cover, dust and ash drift out from between musty, 
	yellowing pages, and the spine creaks at the effort.
	It looks as though someone has carried it through a fire, 
	and smells as though it was dragged through a gutter right after.
	The odors of piss and smoke fill your nostrils, and it is deeply unpleasant.
	Do you try to read it for clues, or discard the worthless piece of garbage?"""

def read_diary ():
	#automatically take diary pages wheen you pick it up
	#these are the pages that you can look back to
	print """ Most of the pages have stuck together, are covered in illegible, bleeding ink, or been ripped out.
	The few pages you can make out can be folded into your notebook



	"""
def discard_diary ():
	print """ Your great grand-grandfather's initials weren't GL anyway.
	You're here for one reason and everything else is distraction."""

def rope_bridge ():
	#out the back door

##multiple things to inspect
#can find diary
#find redacted statement of purpose of initial brotherhood
#chair has embossed initials GL
#scrawled on wall, the same symbol as front door and message: we seek only one outcome. we will prevail

def path_right():
#rocky outcroppings and a path that diverges from the one that loops the wall, heads between the cliffs to a red beach
#the red sand is strange and unearthly in the same way that the stones making up the wall are
#footsteps are in the process of being washed away, but lead to an opening that is exposed at low tide
def path_left():the dock and shore.
#trees appear immediately (look up what trees would be in the South Pacific) 
#choice to follow the wall or head into the forest (you see a structure in the tallest tree there)

def forest_ruins():
#a bizarre thriving tree-dwelling community once lived here
#multiple tree platforms to explore
#clues to find: the diary of G. Leicester, a manifesto of splinter murex group (glory of the current man, we can use their secrets without calling them back)
#manifesto - the holy order does not have the improvement of our own lives at heart - they seek a greater power - we were lied to
#diary - the man is insane. our ships out were supposed to arrive days ago. we wait for some savior
#deeper into forest or return to path

def hermit_hollow():
#crazy ranting man (owner of the diary G. Leicester) - he walks you around in a circular conversation
#if asked about the diary he tells you that Taymor is a great man with a great number of secrets
#he enjoys eating seagulls
#veiled reference to the higher ups? greater race
#he clutches a ripped out page from the diary - they've come, our small band is lost
#go find the grotto. i am tired. i've been tired for so long. i'll stay sitting here. go ask the ones with the answers
#if you go deeper into the forest you get lost and find yourself back at the path

def follow_left_wall():
	# this wall is made of a stone you're unfamiliar with. you're no mason, but something is unusual, unearthly about it
	# some sort of climbing path built into the side of the wall
	# message at the bottom of ladder: show us mercy children of the forest. there is serious work being done inside. you have proved you do not understand. leave us to seek the future.
	# if you try to climb up, it breaks off halfway up the wall, like someone has demolished the rest of the steps


def walking_path_moment():
#maybe this can just be a constant option, but it's observe basically
#you see your ship retreating. The sea was flat and wind wouldn't catch for days. 
#But now you see the sails are full. They move with speed and firm intention far, far away from here.


#sanity hit after talking to the door with no knob? like if you take a second to reflect on it, 
#you feel your mind melt and decide to forge on, that the rules here are different than the ones you know
