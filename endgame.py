def pyramid_approach():
	print """
	It felt like a small island when you arrived,
	but as you take your first decisive steps toward
	this shining monument,
	you wonder how you could ever have associated
	small with this pillar of wonder.\n \n"""
	sleep(4)
	print"""
	You take slow, straight steps toward the shell.
	It is the Murex now,
	no longer just the shining spire.
	You know because it whispers to you. \n\n"""
	sleep(4)
	print"""
	You must get closer,
	there is some great knowledge there,
	inside the pyramid,
	that you must encounter.\n\n"""
	sleep(4)
	print"""
	As you approach,
	a warm sensation,
	hot even,
	flows out over your skin,
	as if your blood was boiling over 
	and spilling out through your pores.
	It is an intense and unbearable feeling,
	that you cannot imagine bearing for long.\n \n"""
	sleep(3)
	print"""
	Your concentration is broken with a sharp slap.\n"""
	sleep(3)
	print"""
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
	AND BUTTOCKS"""
	sleep(3)
	print """
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

def pyramid_second_approach():
	print """ 
	You step past the dirty fool
	towards destiny.

	A large stone door to the pyramid
	stands before you,
	ajar.
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

def pyramid_enter():
	print """ 
	A skylight at the peak of the pyramid
	exposes the inner labyrinth of the Murex,
	twisting upwards
	beyond comprehension,
	and flooding the ritual chamber with a lavender light."""
	sleep(6)
	print"""

	Taymor, no older than you remember him,
	stands directly under the source of light,
	surrounded by the mummified remains of eleven men
	who hang suspended from the ceiling by silver chains."""
	sleep(4)
	print"""

	He smiles at you with bright eyes
	that remind you of a photo you remember from
	a textbook in elementary school
	of a young woman who has just seen her fiancee
	returning from war, 
	one of the old ones."""
	sleep(4)
	print"""
	Her face is so full 
	of confidence and relief and disbelief and love and hope.
	It is right next to elation but also on the edge of tears.
	Later in life you looked for the photo
	and the book you found it in with no luck.
	It was a beautiful expression
	that you have always remembered and longed to see again,
	and you are surpised to see it mirrored now."""
	sleep(6)
	print"""

	MY BLOOD,
	MY RELATION.
	HERE YOU ARE,
	AND JUST IN TIME TO WITNESS THE NEW WORLD.
	WON'T YOU COME AND HUG YOUR GREAT-GRANDFATHER?
	"""

def taymor_hug():
	print """ 
	His arms are tan and strong 
	like Charlton Heston's in The Ten Commandments.
	When they grip you tight you feel the endless potential
	of your bloodline,
	and briefly recall your mother's fear with scorn."""
	sleep(5)
	print"""
	IT FEELS SO GOOD TO FINALLY TOUCH YOU.
	I HAVE ALWAYS KNOWN THAT YOU WERE MEANT
	FOR HIS GLORY.
	TELL ME,
	HAVE YOU COME TO HELP YOUR GREAT-GRANDFATHER
	WITH HIS DIVINE WORK?
	"""

def hug_yes():
	print """ 
	His embrace raises the temperature of your blood.
	To be in this room is to touch something vital.

	CHILD,
	YOU HAVE BEEN RAISED IN DARKNESS
	BUT IT IS YOUR DESTINY TO WALK TOWARDS THE LIGHT.
	TO TOUCH ME IS TO WARM YOURSELF ON THE SAND
	AND BELIEVE YOU KNOW WHAT IT IS LIKE TO
	WALK ON THE SUN.
	TELL ME YOU WILL EMBRACE THE GREAT ONE.

	Give in to Taymor's request,
	or recoil from the warmth?
	His grip makes it apparent that the choice
	is imminent.	
	"""
	#can lead to embrace divinity

def hug_no():
	print """ 
	Before you can finish refusing him,
	your great-grandfather has a strong grip on your arm.

	YOU'VE COME A LONG WAY TO HAVE SUCH A DANGEROUS ANSWER
	ON YOUR LIPS.
	ARE YOU SURE YOU ARE NOT HERE TO FURTHER
	THE SERVANTS' CAUSE?

	Accept the embrace or attempt escape?
	"""
	#can lead to embrace divinity

def hug_no_ascension():
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
	
	Your name will live as an embarrassment,
	a curse uttered almost without meaning,
	by future generations
	in far removed
	and greater
	worlds.

		               ,.
                      /-|
                     (--;
                    (,-';
                  _/_.-';
                _/-.__._<
             .-'`-.__   '\
           .'`---=___`===':
          /_..---' ___.--.'
         |` ___.--' __ .i|
         |-' ___.--'_.8:E|
         \,-'  __.-/88::E!
          `-.,' _.'|88::E|
             `;'../88:: E;
              |.'!88::E"/
             /.''!"iiE /
             `--'`._.-'  
	"""

def taymor_question():
	print """
	TO QUESTION THE PATH IS THE MISTAKE
	OF MANY HERETICS COME BEFORE
	AND FALLEN SINCE.

	I SENSE THAT YOUR BLOOD SINGS WITH TRUTH,
	AND HOPE THAT YOUR SOUL'S PULL TOWARD TOMORROW
	WILL OVERCOME
	YOUR HUMAN MIND'S FEEBLE ATTEMPTS TO RESIST.

	SPEAK NO MORE.
	HOLD MY HAND AND WELCOME THE NEW WORLD.

	Do you accept this strange offer from a man you have
	been warned against?

	Taymor's eyes leak lavender tears,
	the same color as the perfume bottle
	that your father's secretary kept on her desk.
	She was a pitiful woman.
	The bottle never emptied,
	and you always assumed she imagined it a sort of trophy.

	Do you flee this murderous island?


	Action is called for.
	Greatness is frequently determined at a moment's notice.
	Respond in one way or the other
	to the call.
	"""
	#can lead to embrace divinity

def taymor_attack():
	print """ 
	Your blow lands pitifully.
	His flesh is somehow more than flesh.

	He does not speak,
	but his smile lets you know that you must do more
	serious damage
	or bend your knee to a greater power.

	Do you now accept his hand or turn from him?
	"""
	#can lead to embrace divinity

def taymor_attack_again():
	print """ 
	Pain does not come immediately.

	First is the realization of your insignificance,
	followed by the knowledge that you have missed
	out on something much larger than the current
	scope of your comprehension.
	You are crushed completely before the physical
	pain arrives.

	But when the pain comes,
	it does come,
	it consumes you completely.

	In catechism, you always found the descriptions
	of hell to be vague,
	and struggled to understand the fear it arroused.
	As your immortal relative rips away
	at pieces you consider essential,
	you remember a teacher saying once,
	to another faculty member,
	HELL LIVES AROUND THE CORNER,
	WHEREVER IT IS IS WHEREVER I GO.

	Life slips from you in this unfriendly fashion.

	You witness none of the glory.

		               ,.
                      /-|
                     (--;
                    (,-';
                  _/_.-';
                _/-.__._<
             .-'`-.__   '\
           .'`---=___`===':
          /_..---' ___.--.'
         |` ___.--' __ .i|
         |-' ___.--'_.8:E|
         \,-'  __.-/88::E!
          `-.,' _.'|88::E|
             `;'../88:: E;
              |.'!88::E"/
             /.''!"iiE /
             `--'`._.-'  
	"""

def taymor_speech(): #if why
	print """ 
	WHY IS A HUMAN QUESTION
	AND IT IS BESIDE THE POINT OF ASCENSION.
	WE ARE HERE TO WORSHIP,
	BUT WE ARE ALSO HERE TO RISE.
	WE ARE HUNGRY
	AND WE MUST LEARN TO EAT OUR FILL.

	MY VEINS VIBRATE IN YOUR PRESENCE.
	TRUST ME, AND OUR LINE WILL LEAD
	A NEW WORLD GREATER THAN ANY YOU CAN IMAGINE.

	He holds his hands out to you,
	and his pale eyes shine
	with power and confidence.
	"""

def taymor_other():
	print """ 
	He looks at you quizically.

	I KNOW WHO YOU ARE.
	TO STAND THERE UNANNOUNCED IS AN INSULT TO YOUR BLOODLINE.
	EMBRACE YOUR HIGH PRIEST
	OR ACCEPT THE JUDGEMENT
	HE PASSES THROUGH ME.

	Taymor unsheathes a golden blade.
	Its weight appears comfortable in his hand.
	Make a choice now.

	Do you now accept his embrace or turn to violence?
	"""

def taymor_embrace_divinity():
	print """ 
	As your soul bends to the unknown,
	Taymor senses the shift in you and smiles.

	YOUR HAND, NOW.

	An urge to resist might have boiled up in 
	your past self,
	but something has overtaken you now.
	You reach your hand out to him,
	and do not flinch when his dagger cuts through
	your palm.

	YOUR BLOOD WOULD HAVE SPILLED WITH
	OR
	WITHOUT YOUR CHOICE.
	YOUR BEAUTIFUL DECISION WILL EARN HIS MERCY.

	As your blood splashes across the floor,
	the lavender light turns a deep purple
	and the heat runs through your bones.

	This is it, you think,
	as you and Taymor walk outside the pyramid.

	Before you, gliding across the horizon,
	a giant snail crawls along the South Pacific
	consuming all that is in its path.

	Islands, ocean, animal life,
	all disappear beneath it.

	Soon you too will be consumed,
	and nothing could make you happier.
	                   ,.
                      /-|
                     (--;
                    (,-';
                  _/_.-';
                _/-.__._<
             .-'`-.__   '\
           .'`---=___`===':
          /_..---' ___.--.'
         |` ___.--' __ .i|
         |-' ___.--'_.8:E|
         \,-'  __.-/88::E!
          `-.,' _.'|88::E|
             `;'../88:: E;
              |.'!88::E"/
             /.''!"iiE /
             `--'`._.-'  
	"""

#This should be in a Look Around when you first enter the pyramid.
def pyramid_survey():
	print """
	Taymor's skin glows healthily,
	and his presence fills the massive room.

	Angelic smiles light up all but one of the faces
	of the shrunken, suspended men. 
	His visage has been removed,
	and every finger and toe curls in what you recognize
	as physical misery.

	This room and the things that have happened in it
	are the source of your feelings of unease
	and the old man you encountered in the woods'
	madness.
	"""
