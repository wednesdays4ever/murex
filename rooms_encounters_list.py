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
    remote areas of the world."""
    sleep(3)
    print """ He encouraged you, while out in the world, 
    to take a moment and listen to all that surrounds you."""
    sleep(2)
    print "You do this now, and your stomach sinks."
    sleep(2)
    print """This is a silent forest."""
    sleep(2)
    print """ You have left behind even the sound of the waves.
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

def tree_house():
    print """ This is not at all what you were expecting from the disarray in the clearing.
    This finished interior would be more fitting in an Ivy League library 
    than a makeshift building in the South Pacific.
    But the formerly beautiful room is in tatters.
    Some violence has happened here."""
    sleep(4)
    print"""
    Leatherbound books lay ripped apart and scorched on the dark, polished mahogany floor.
    A small side table with accompanying chess set lies overturned 
    next to a finely upholstered chair.
    This place must somehow be related to the compound.
    Could this have been Taymor's den?"""
    sleep(2)
    print """"
    Were you too late to respond to his letter?
    The room fills you with sadness,
    but if you're here to learn about your relative, this seems like a place to start.
    """

def tree_house_inspect():
    print """ Upon closer inspection, you notice a few things that seem out of the ordinary:
    The corner of a hardcover book peeking out from under the chair's cushion,
    The initials G.L. embossed on the back of the chair,
    and, gruesomely, scrawled in what looks like gore on the wall next to the opposite door
    THE END IS THE ONLY OUTCOME. WE WILL PREVAIL.\n"""
    sleep(6)
    print """ The book is a diary. 
    A fine one, thick as an encyclopedia, that has seen much wear and tear.
    G.L. is embossed in gold on the cover.
     Whoever G.L. was and whatever happened to him here are questions that cannot have pleasant answers.
     But how can you know unless you ask?"""

def open_diary():
    print """ As soon as you open the cover, dust and ash drift out from between musty, 
    yellowing pages, and the spine creaks at the effort.
    It looks as though someone has carried it through a fire, 
    and smells as though it was dragged through a gutter right after.
    The odors of piss and smoke fill your nostrils, and it is deeply unpleasant.
    Do you try to read it for clues, or discard the worthless piece of garbage?"""

def read_diary():
    #automatically take diary pages wheen you pick it up
    #these are the pages that you can look back to in notebook
    print """ Most of the pages have stuck together, are covered in illegible, bleeding ink, or been ripped out.
    The few pages you can make out can be folded into your notebook."""

def discard_diary():
    print """ Your great grand-grandfather's initials weren't GL anyway.
    You're here for one reason and everything else is distraction."""

def rope_bridge():
    print """ The door at the other side of the study opens straight onto a rope bridge.
    Across, you see a large, circular structure with a thatched roof. 
    It swings back and forth in the light breeze."""
    sleep(4)
    print """Do you venture forward for further investigation, or close the door and turn back?"""

def no_bridge():
    print """ You turn back into the sad, smelly little room.
    The ladder down and the door to the bridge are the only paths out."""

def cross_bridge():
    print"""The bridge swings wildly and forces you to take slow, careful steps.
    It is certainly treacherous, but something within you keeps fear at bay.
    To adventure, to address danger, feels natural here.
    Necessary. 
    At the other side, you stand at the wooden door to the thatched structure.
    A closed eye just like the one on the stone fortress is painted on the front."""

def second_sect_hq():
    print """ This eye does not open as you enter.
    The interior of the thatched hut has a dark, musty gravity.
    Serious things were discussed here by sad men.
    Secrets have seeped into the dust.
    A long mahogany table sits in the center, 
    the image of a huge, spiny seashell
    carved crudely into the beautiful wood.
    A dozen chairs line its sides with 
    one, large commanding seat at the head of the table.
    Behind it, a handwritten piece of paper is tacked to the wall.
    Another ladder leads down to the ground."""

def second_sect_manifesto():
    #the text of the page can be added to your notebook
    print """ You move across the room until you are close enough 
    to make out words on the tacked up page. 

    SECOND SECT OF THE SERVANTS OF THE MUREX
    A call to return to service.
    The task of our brotherhood was always 
    to invite divinity into our small and tainted world,
    to bring greatness close enough to man's touch that our race could glow 
    like the old ones who lived before us, and continue to live on, 
    beyond and outside of the constraints of our limited understanding.
    This path has been abandoned 
    by heretics who now hold the seat of our holy order hostage,
    but when the Great One comes to swallow us whole, 
    he will taste the difference between 
    the sour, vile and selfish opportunist 
    and the sweet purity of the true believer.

    That is all you can make out, 
    as the bottom has been ripped away
    and spattered with ink and blood.
    """

def ladder_down():
    print """ The ladder leads down 
    into a much smaller clearing than the first you encountered.
    A path leads back in what you believe to be the direction of the first large forest clearing, 
    but there are also signs that someone has walked further into the forest, 
    footsteps through a thicket. 
    Do you take the path, or continue your investigation?"""

def path_back():
    print """ This path winds back through the trees. 
    You find yourself at the first, large forest clearing that you encountered."""
    #then print first description again

def follow_steps():
    print """ You follow the footsteps into a thicket, 
    which opens up almost immediately to the entrance of a small cave.
    Do you enter the darkness?"""

def cave_enter():
    print """ The low ceiling forces you to your knees.
    A dim, smoky light and a foul, sour smell come from deeper in.
    Your natural senses are repulsed, but secrets are rarely pleasant
    and you are here for discovery, so you crawl forward.
    Around a bend, you find the source of the light.
    A skinny, bearded man sits cross legged in a sea of candles, 
    wrapped in the tatters of a royal purple velvet robe, 
    emroidered across the breast with a golden G.L.
    He looks up at you as a dog who expects another kick.
    What do you say to the pitiful man?"""

def GL_introduce():
    print """ I AM GUY LEICESTER,
    HEAD OF THE ONE TRUE BROTHERHOOD OF THE MUREX. 
    WHY HAVE YOU ENTERED MY CHAMBER?"""

def GL_threaten():
    print """ He laughs before responding to your threat.
    IF YOU HAD KNOWN THE PAIN THAT ALREADY LIVES IN ME,
    YOU WOULD NOT HAVE EMBARRASSED YOURSELF 
    BY PRESUMING YOU WERE ABLE TO INFLICT MORE.
    I'LL FORGIVE IT ONCE.
    WHY ARE YOU HERE?"""

def GL_Taymor():
    print """YOU HAVE THE EYES OF THE MAN WHO TOOK IT ALL AWAY. 
    I CAN TELL ON SIGHT THAT YOU ARE RELATED. 
    I CAN ALSO SEE THAT IT IS NOT TOO LATE FOR YOU.
    EMBRACE THE TRUE NATURE OF THE ONE WE SERVE,
    AND MAYBE YOU CAN STEER THE LOST PRIEST BACK TO GREATNESS.
    DON'T YOU WANT TO SEE THE WORLD EVOLVE?"""

def GL_diary_show():
    print """ I DON'T KNOW WHAT YOU THINK YOU'VE LEARNED.
    REAL ANSWERS LIE INSIDE THE FORTRESS ON THE TEMPLE GROUNDS.
    WHY DID YOU COME HERE?
    DO YOU ASPIRE TO SERVICE?"""
    #IF YES, PURITY
    #IF NO, NO PATIENCE

def GL_purity():
    print """ TO SERVE THE GREAT ONE,
    YOU MUST PROVE YOUR PURITY.

    HAVE YOU EVER EXTINGUISHED LIFE?"""
    #no matter what, GL end me

def GL_no_patience():
    print """ He glares.
    JUST BECAUSE I HAVE WAITED FOR DECADES
    DOES NOT MEAN THAT MY TIME IS WORTHLESS.
    TELL ME WHY YOU ARE HERE 
    OR I WILL MAKE YOU LEAVE."""
    #if mentions anything to do with temple or taymor, go to gl_end_me
    #elif GL_no_kill

def GL_end_me():
    print """HORRIBLE THINGS I'VE BEEN MADE TO WITNESS.
    I AM NO LONGER USEFUL AS HIS SERVANT ON THIS PLANE.
    BUT I CAN PUT MY HOPE IN YOU.
    I KNOW THAT I CANNOT ASK FOR GUARANTEES,
    BUT I HOPE THAT WHEN YOU SEE THE TRUTH, THE HORROR,
    YOU WILL REALIZE WHAT YOU MUST DO.

    END ME, AND THE ACT WILL GRANT YOU ENTRANCE TO THE TEMPLE GROUNDS.

    He produces a thin, golden dagger, which he hands gently to you.

    YORHAM WILL SMELL MY BLOOD ON YOUR HANDS 
    AND KNOW YOUR PURITY. 

    His eyes water as he looks up at you with a toothless smile.
    Do you end this miserable life? """

def GL_dead():
    print """ His life leaves its broken vessel easily.
    Blood pours freely, extinguishing many of the candles,
    and soaking your clothes.
    The smell is horrible,
    but the peaceful, powerful smile of a man at rest
    warms the room, making it feel less gruesome
    than it might otherwise.

    You have killed. 
    It is time to test the blood."""

def GL_no_kill():
    print """He cackles at you.
    TO CONTINUALLY BELIEVE THAT THERE IS ANOTHER, 
    MORE PLEASANT PATH 
    IS A PARTICULARLY HUMAN FANTASY.
    THERE IS MORE WEAKNESS IN YOU THAN I EXPECTED.
    BE GONE BEFORE I SPILL YOUR BLOOD INSTEAD."""

def GL_no_kill_leave():
    print""" The man is crazed and willing to kill,
    you see it in his eyes and flee.
    You find yourself at the entrance to the cave,
    no closer to the truth."""

def GL_no_kill_stay():
    print """ You have faltered as an investigator,
    and Leicester follows through with his promise.

    IMPURITY CANNOT BE TOLERATED IN HIS HOUSE.

    You find the golden dagger buried deep in your stomach.
    As you close your eyes,
    you enter a vision,
    like a dream,
    of thumbing through a book thousands of pages of long,
    in a language you do not recognize.
    So much knowledge.
    An endless universe of truths 
    that you will never begin to understand."""
    #respawn at dock?

def path_right():
#rocky outcroppings and a path that diverges from the one that loops the wall, heads between the cliffs to a red beach
#the red sand is strange and unearthly in the same way that the stones making up the wall are
#footsteps are in the process of being washed away, but lead to an opening that is exposed at low tide
def path_left():the dock and shore.
#trees appear immediately (look up what trees would be in the South Pacific) 
#choice to follow the wall or head into the forest (you see a structure in the tallest tree there)

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
