def pyramid_approach():
	print """
	It felt like a small island when you arrived,
	but as you take your first decisive steps toward
	this shining monument,
	you wonder how you could ever have associated
	small
	with this pillar of wonder.

	You take slow, straight steps toward the shell.
	It is the Murex now,
	no longer just the shining spire.
	You know because it whispers to you.
	
	You must get closer,
	there is some great knowledge there,
	inside the pyramid,
	that you must encounter.

	As you approach,
	a warm sensation,
	hot even,
	flows out over your skin,
	as if your blood was boiling over 
	and spilling out through your pores.
	It is an intense and unbearable feeling,
	that you cannot imagine bearing for long.

	Your concentration is broken with a sharp slap.

	You look down for the first time in 
	what might have been an hour
	to see a tiny, sharp-faced man
	in a torn and filthy purple robe.
	YOU'RE LATE
	the weasel croaks.

	How do you respond to this interruption?
	"""
def dobbins_attack():
	print """ Whoever this small and insignificant creature was
	has crumpled beneath a newly woken might.
	You feel strong as you step over the creature.
	As your eyes return to the Murex,
	it seems to adopt a faint lavender glow.

	The sun shines a faint orange 
	as it sets
	that pales next to the glowing spire

	A stone door lies ajar in front of you.
	Do you enter this beyond?
	"""

def dobbins_question():
	print """ 
	I AM HIS HUMAN EXCELLENCY THE HIGH PRIEST'S
	MOST TRUSTED SERVANT
	AND THE ONE WHO HAS BORNE THE BRUNT OF
	HIS FRUSTRATION AND IMPATIENCE
	AT YOUR DELAYED ARRIVAL.
	AT THE SIGHT OF YOU I FEEL BOTH RELIEF
	AND THE DESIRE TO STRIKE YOU ABOUT THE FACE
	AND BACK
	AND ANKLES
	AND BUTTOCKS
	AS I HAVE BEEN STRUCK
	ABOUT THE FACE AND BACK AND ANKLES AND BUTTOCKS.
	BUT I WILL RESIST THE URGE
	YOUR BLOOD IS NOT MINE TO SPILL.
	MY MASTER AND THE ONE WHOM WE BOTH SERVE
	AWAIT.
	"""
	#if violence, go to attack
	#if other, he forces you forward

def dobbins_taymor():
	print """ 
	THE HIGH PRIEST AWAITS YOU.
	YOU ARE LATE,
	AND IT IS MY PERSONAL WISH TO PUNISH YOU FOR IT,
	BUT YOUR TARDINESS MAY BE EXCUSED BY OUR MASTER,
	IF YOU HURRY NOW TO BEND THE KNEE.
	"""
	#IF violence go to attack
	#if something about approach, do that
	#if other, the hurry forward

def dobbins_other():
	print """ 
	This insolent man grabs your shoulders,
	and shoves you along,
	yelping 
	YOU ARE LATE,
	PROCEED TO THE RITUAL!

	You feel somewhere deep inside you,
	the knowledge that you are able
	to crush this fragile idiot,
	and the desire to do so.

	But the call of the Murex is stronger
	than your thirst for violence,
	and you follow his push without causing him harm.

	A stone door stands before you,
	ajar."""

def dobbins_hurry_forward():
	print """ 
	GET GOING!
	THE COMING IS COMING
	AND YOU MUSTN'T MISS IT!

	The man is nervous and simple.
	He senses the approaching greatness,
	but can articulate none of its glory.
	You feel a mix of pity and disgust.
	This creature will not reach a higher consciousness.

	You step past the ant without crushing it,
	towards a stone door to the pyramid
	that stands ajar,
	welcoming you home.
	""" 

def pyramid_approach():
	print """ 
	You step past the dirty fool
	towards destiny.

	A large stone door to the pyramid
	stands before you,
	ajar.
	"""

def pyramid_enter():
	print """ 
	A skylight at the peak of the pyramid
	exposes the inner labyrinth of the Murex,
	twisting upwards,
	beyond comprehension,
	and flooding the ritual chamber with a lavender light.

	Taymor, no older than you remember him,
	stands directly under the source of light,
	surrounded by the mummified remains of eleven men,
	suspended from the ceiling by silver chains.

	He smiles at you with bright eyes
	that remind you of a photo you remember from
	a textbook in elementary school
	of a young woman who has just seen her fiancee
	returning from war, 
	one of the old ones.
	And her face is so full 
	of confidence and relief and disbelief and love and hope.
	It is right next to elation but also on the edge of tears.
	Later in life you looked for the photo
	and the book you found it in with no luck.
	It was a beautiful expression
	that you have always remembered and longed to see again,
	and you are surpised to see it mirrored now.

	MY BLOOD,
	MY RELATION.
	HERE YOU ARE,
	AND JUST IN TIME TO WITNESS THE NEW WORLD.
	WON'T YOU COME AND HUG YOUR GREAT-GRANDFATHER?
	"""

def pyramid_other():
	print """ 
	A majestic moment like this is something
	that has perhaps been forever unknown to this world.
	You are right to bask in it.
	But soon, the call is too strong,
	and you find yourself pushing the stone door open.
	"""
	#leads into pyramid entrance

def taymor_hug(): #if hug
	print """ 
	His arms are tan and strong 
	like Charlton Heston's in The Ten Commandments.
	When they grip you tight you feel the endless potential
	of your bloodline,
	and briefly recall your mother's fear with scorn.

	IT FEELS SO GOOD TO FINALLY TOUCH YOU.
	I HAVE ALWAYS KNOWN THAT YOU WERE MEANT
	FOR HIS GLORY.
	TELL ME,
	HAVE YOU COME TO HELP YOUR GREAT-GRANDFATHER
	WITH HIS DIVINE WORK?
	"""

def hug_yes():
	pass

def hug_no():
	print """ 
	YOU'VE COME A LONG WAY TO HAVE SUCH A DANGEROUS ANSWER
	ON YOUR LIPS.
	ARE YOU SURE YOU ARE NOT HERE TO FURTHER
	THE SERVANTS' CAUSE?
	"""

def hug_second_no():
	print """ 
	He sighs.
	A lonely sound.

	I DID TRULY WISH FOR YOUR COMPANY.
	BUT IN TRUTH,
	IT IS JUST YOUR BLOOD I NEED.

	A golden flash and you are leaking lifeblood.
	Before your consciousness is complete,
	you see Taymor's smile flash 
	and glimpse a giant purple snail,
	larger than the island itself,
	with a glimmering Murex on its back,
	sliding over the horizon,
	swallowing everything in its path.

	You have let divinity pass you by.
	Mankind is eclipsed.
	No one will remember your name.
	"""

def taymor_question():
	pass

def taymor_attack():
	pass

def taymor_murex():
	pass

def taymor_other():
	pass

def pyramid_survey():
	pass

def taymor_speech():
	pass

def ritual_begin():
	pass

def ritual_interrupt():
	pass
