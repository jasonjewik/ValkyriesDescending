###### Characters
define narrator = nvl_narrator
define adv = Character(None, kind=adv)

###### Menus
define advMenu = menu
define menu = nvl_menu
define quickMenu = True

###### Backgrounds
image bg alley = "images/bgs/alley.JPG"
image bg black = "images/bgs/black.jpg"
image bg red = "images/bgs/red.jpg"
image bg white = "images/bgs/white.jpg"

###### Computer Graphics
image cg dianthe van = "images/cgs/prologue_dianthe-van.png"

###### Characters
## Abra
image abra neutral left = "images/chars/abra/neutral_L.png"
image abra neutral right = "images/chars/abra/neutral_R.png"
## Dianthe
image dianthe neutral left = "images/chars/dianthe/neutral_L.png"
image dianthe neutral right = "images/chars/dianthe/neutral_R.png"
image dianthe shocked left = "images/chars/dianthe/shocked_L.png"
image dianthe shocked right = "images/chars/dianthe/shocked_R.png"
## Jobber
image jobber neutral left = "images/chars/jobber/neutral_L.png"
image jobber neutral right = "images/chars/jobber/neutral_R.png"
image jobber injured left = "images/chars/jobber/injured_L.png"
image jobber injured right = "images/chars/jobber/injured_R.png"
## Mook
image mook neutral left = "images/chars/mook/neutral_L.png"
image mook neutral right = "images/chars/mook/neutral_R.png"
image mook injured left = "images/chars/mook/injured_L.png"
image mook injured bloody left = "images/chars/mook/injured-bloody_L.png"

###### Title Screens
image tscn chapter = "images/title-screens/chapter.png"

###### Choices
# Van Interior Imagemap
define farWall = False
define sideWall = False
define floor = False
define imEnabled = True
# First Choice
define firstChoice = [False, False]

###### Text Variables
image chapterTitleText = ParameterizedText(xalign = 0.8, yalign = 0.9, font = gui.interface_text_font, size = gui.title_text_size)

# The game starts here.
label splashscreen:
    show splash
    pause 3.0
    return

label start:
    stop music

    $ quick_menu = False
    scene bg black
    show tscn chapter with fade
    show chapterTitleText "Prologue:\nApocryphal Provenance" with dissolve
    pause 3.0
    hide chapterTitleText with dissolve
    hide tscn chapter with dissolve
    $ quick_menu = True

    """
    I never really thought of myself as anything but ordinary. My story... No, it’s not one worth telling. Not at all. The paper it would be written on is worth more than the tale itself. At least, that’s how I feel. And yet, you’re here...

    Well, now that you are, you must want to know right? What this is all about? What happened to me? To all of us? Alright, if you say so...

    Where do we begin? Right before? Right after? Now? Then? Well, we need to begin at some point... Stories need both a beginning and an end, right? That’s what Mama always said. Ah, I know...

    Let me just warn you before we start that this story, if it could be called anything, it would undoubtedly, unmistakably, irrefutably be known as...

    Yes indeed, it would be known as a tragedy.
    """
    nvl clear

    scene bg white
    adv "{i}Dad... No...!{/i}"

    play sound "sounds/sfx/stabbing_spear.ogg"
    scene bg red
    pause 0.3

    scene bg black
    pause 1.0
    adv "{i}Mama...No, you can't...! Don't leave me alone, please!{/i}"

    play music "sounds/sfx/car_on_road.ogg" fadein 4.0

    """
    I am awakened by a cold, hard surface rubbing painfully into my back. I try to move my hands but encounter only resistance. They are tied up then, I conclude.

    Strange, I’m not compelled to struggle against my restraints at all. In fact, I don’t really mind it. There is something faintly familiar and comforting to the thin rope cutting into my wrists.

    {i}Where am I?{/i} Upon regaining consciousness, this is the only thought that occupies my mind. That and, {i}How do I escape?{/i}
    """
    nvl clear

    adv "\"Hey, I think she’s waking up. What do we do, Boss?\""

    """
    I panic. Someone else is in here with me? Looking at me? Who? My stomach churns at the idea that somebody is there and I am here, unable to see, to act. I can’t stand it, the idea that I may be at someone else’s mercy.
    """
    nvl clear

    adv "\"I’ll go ahead and take off her blindfold.\""
    adv "\"Are you sure, Boss?\""
    adv "\"Why not? It’s not like she’s a threat. Having a blindfold wrapped so tightly around her head doesn’t exactly look very comfortable anyway.\""
    stop music fadeout 4.0
    play music "sounds/sfx/car_on_road_muffled.ogg" fadein 4.0
    adv "{i}Voices: one woman, one man...{/i}"

    scene bg white with fade

    """
    The sudden brightness catches me off guard, forcing my eyes to close. When I finally manage to open them just a bit without searing my retinas, I spy a kind-looking face.
    """
    nvl clear
    window hide

    scene alley with dissolve
    show jobber neutral left

    adv "\"Hey there! You alright?\""
    adv "I blink once, confused. {i}She...{w=0.7} she kidnapped me, right?{/i}"
    adv "\"I-I’m fine.\" {i}She kidnapped me, right? Why is she acting so nice to me?{/i}"
    adv "\"Good, I was worried there for a second!\" she says, a huge grin across her face."

    """
    Why is she so concerned my well-being if she is the one who kidnapped me? Maybe hostages in good condition sell for more? Or could she be trying to keep my organs in working order?

	Good question: why was I kidnapped? I need to gather more information.

    First, I should figure out my surroundings.
    """
    jump van_interior

label van_interior:
    python:
        if (sideWall == False or floor == False or farWall == False):
            imEnabled = True
            renpy.show_screen("viewport_imagemap", scn = "prologue")
            renpy.pause()

    $ renpy.transition(dissolve)
    hide screen viewport_imagemap
    nvl clear
    """
    I have an idea of my surroundings. As I suspected from the sounds, I’m inside of a car. It looks like the back of a van. It’s... familiar somehow, this setting that is. I feel like I’ve been somewhere like this before.

    I struggle against my restraints again to no avail. Every time I move, the rope just cuts deeper and deeper into my flesh. I feel something warm trickle down the side of my hand.

    If I can’t escape by myself, then I need to delay whatever is going to happen to me as long as possible. I need to distract these people in front of me. Seeing as my mouth is uncovered and my ability to speak is unimpeded, I ask...
    """
    jump first_choice_menu

label side_wall:
    $ imEnabled = False
    if sideWall == False:
        """
        No windows... I can’t tell if it’s day or night or even where I am. The walls look reinforced too... Looks that I can’t get out that way.
        """
        $ sideWall = True
    else:
        """
        I already checked the side wall.
        """
    window hide
    jump van_interior

label floor:
    $ imEnabled = False
    if floor == False:
        """
        Cold, hard, and terribly uncomfortable to sit on. My legs are going numb from the constant vibrations.
        """
        $ floor = True
    else:
        """
        I already checked the floor.
        """
    window hide
    jump van_interior

label far_wall:
    $ imEnabled = False
    if farWall == False:
        """
        Looks like that wall is solid metal... It won’t be easy to break through it. That’s one route gone.
        """
        $ farWall = True
    else:
        """
        I already checked the far wall.
        """
    window hide
    jump van_interior

label first_choice_menu:
    menu:
        "Where am I?" if (firstChoice[0] == False):
            $ firstChoice[0] = True
            python:
                if (firstChoice[1] == True):
                    renpy.say(adv, "{i}I guess I might as well ask that next{/i}, I think.")
                else:
                    renpy.say(adv, "{i}Let's start with that{/i}, I decide.")
            jump first_choice_0
        "Where are we going?" if (firstChoice[1] == False):
            $ firstChoice[1] = True
            python:
                if (firstChoice[0] == True):
                    renpy.say(adv, "{i}I guess I might as well ask that next{/i}, I think.")
                else:
                    renpy.say(adv, "{i}Let's start with that{/i}, I decide.")
            jump first_choice_1

label first_choice_0:
    adv "The woman's smile grows wider, but her eyes are filled with a different emotion... Pity, maybe?"
    adv "\"Don’t worry, you’re still in Moroes City. You woke up pretty quickly, to be honest. We’ve only just left your apartment; only an hour has passed, at most. I know you’re special, but even I’m impressed by how quickly you recover.\" She giggles."
    adv "\"What’s so funny?\""
    adv "\"This reminds me of one of my favorite legends. Do you know of the Celtic hero Cú Chulainn?\""
    adv "\"He also woke up far too early when he was put under. That landed him in a spot of trouble... Well, I’m sure that nothing like that will happen here.\" On that ominous note, she stops talking."

    python:
        if False in firstChoice:
            renpy.jump("first_choice_menu")
        else:
            renpy.jump("first_choice_merge")

label first_choice_1:
    adv "\"We’re heading to a private airfield so we can get you to headquarters. That would be...\""
    adv "She looks over at a man standing next to her. He is clad in a black trenchcoat, like the ones that the characters wore in that one movie about magic, flying, karate-wielding computer hackers. Had he been the one she had been talking to earlier?"
    adv "\"Where is it again? It’s on Alcatraz Island, right?\""
    adv "The man sighs."
    adv "\"With all due respect, Agent Jobber, you’re an American: you should at least know this much. Additionally, as an international agent, you would do well to learn where all of the regional bases of operation are.\""
    adv "He sounds exasperated, as if he has to deal with this level of incompetence on a regular."
    adv"\"But, all that aside, yes,\" he says, straightening his sunglasses in an effort to regain his composure, \"the American Mages’ Society headquarters is located on Alcatraz Island.\""
    adv "\"There you have it!\" the woman, whose name I knew as Jobber, said, looking back at me, beaming. She did not seem even slightly fazed by the man’s exasperated tone."
    adv "\"You heard the man! We’re headed to Alcatraz! Isn’t that exciting? It’s quite a popular tourist destination, you know. It’ll be fun, I promise!\""

    python:
        if False in firstChoice:
            renpy.jump("first_choice_menu")
        else:
            renpy.jump("first_choice_merge")

label first_choice_merge:
    nvl clear

    """
    She is a whimsical one, that much I can tell. She does not exactly seem great at her job. Is she really an adult? I always thought that adults would take their jobs much more seriously, have a stiff upper lip, and hate the very concept of \"fun\".

    Wait, before that, what were they even talking about? Agents? Mages’ Society? Alcatraz? What was going on?

    {i}Have... Have I managed to get kidnapped by real, actual psychos?!{/i}
    """
    nvl clear

    stop music
    play sound "sounds/sfx/car_screeching_to_halt.ogg"
    adv"\"What happened?! What's wrong?!\" the man next to Jobber yells."
    adv "A girl! She just jumped in front of-!"

    play sound "sounds/sfx/gunshot_assault_rifle.ogg"
    pause 1.0
    play sound "sounds/sfx/finger_snap.ogg"

    """
    The man standing next to Jobber raises his right hand, snapping his fingers. The patterns on his trenchcoat spark to life, glowing a faint blue. Jobber does the same. I feel the atmosphere shift a little. There is a slight buzzing in my ears, as if the air with getting filled with electricity, except not quite. A delightful shiver runs through my limbs, begging me to leap into action.
    """
    nvl clear

    adv "\"Proceed with caution. We don’t know the—\""

    play sound "sounds/sfx/gunshot_assault_rifle.ogg"
    pause 0.25
    play sound "sounds/sfx/glass_shattering.ogg"

    adv "\"Ugh, these bullets... They couldn’t have!\" the man grunts. He seems unharmed but is visibly shocked. \"How did they pierce—?!\""

    play sound "sounds/sfx/gunshot_assault_rifle.ogg"

    adv "\"Gah!\""
    adv "This time, the man doubles over in pain, a blotch of red spreading out from his chest region. He hacks out a cough, spraying crimson all over himself, further staining his coat. The red on black... the contrast stirs something within me."

    play sound "sounds/sfx/heartbeat.ogg"

    adv "\"Get down!\" Jobber yells as she roughly pushes me to the floor of the van. She is not a moment too soon; another bullet just barely grazes the top of my head. I think I can see the single strand of hair that was shredded in the incident falling before my eyes."
    adv "Jobber puts her hand to the metal partition that separates the back of the van from the driver and passenger seats but pulls back abruptly with a yelp. She stares at her angry red palm in surprise. \"Heat?\" she whispers out. Her eyes widen in fear. \"Fire?\""

    play sound "sounds/sfx/metal_melting.ogg"
    show cg dianthe van with dissolve
    pause

    """
    A girl. Through the melted pool of steel and aluminum lying at the floor of the van steps a girl. Something about her captivates me. Her eyes, purple like amethysts. Purple? Is having purple eyes even naturally possible? I wouldn’t be surprised if it wasn’t. They look so mesmerizing... I just want to stare into them forever. The look in her eyes… it is like that of an angel. Just looking at her provides me with a feeling of calm.

    It was not just her eyes either. Everything about her struck me as otherworldly and fantastical. She could not have possibly been much older than me but her aura... it just felt like she had lived several more lifetimes than me.

    She enters without a sound. Her walking is so graceful that it almost did not seem like she was walking at all. Floating, no, hovering almost. It would seriously not surprise me at this point if this girl is just some stress-induced ephemeral hallucination of mine. That has to be it: I must be completely delirious.
    """
    nvl clear

    scene bg alley with dissolve
    show jobber neutral right

    adv "The girl casually waves the muzzle of the assault rifle she is carrying in my direction. \"I’m here for her,\" she says in a soft, monotone voice."
    adv "She speaks. Even her voice sounds like an illusion!"
    adv "Jobber tightens her grip on my shoulder. \"Not happening. She’s under my protection.\""
    adv "Jobber sees her too. Guess that rules out me going insane."
    adv "\"Please,\" the girl says, raising the barrel of the rifle to point at Jobber without a hint of emotion in her voice."
    adv "\"No,\" Jobber replies resolutely."
    adv "The girl sweeps the barrel of her assault rifle in a wide arch."

    play sound "sounds/sfx/gunshot_assault_rifle.ogg"
    pause 0.1
    play sound "sounds/sfx/gunshot_assault_rifle.ogg"
    pause 0.1
    play sound "sounds/sfx/gunshot_assault_rifle.ogg"
    pause 0.1
    play sound "sounds/sfx/gunshot_assault_rifle.ogg"
    hide jobber
    show dianthe neutral right

    adv "The smell of spent gunpowder fills the air. The sounds of the wind grow louder, no doubt because of the holes that now pepper the back of the van."
    adv "\"Please,\" the girl asks again, punctuating the request by pointing the rifle at Jobber."
    adv "Jobber lets out a long, dramatic sigh. She slowly raises her hands to the air. \"Alright, you win. Take her.\""
    adv "At first, I feel just a bit betrayed. Didn’t she say I was under her protection? She’s just going to give me up so easily? Then, it hit me: Something’s not right. That was too hammed up, too theatrical."
    adv "The girl motions with her gun. \"Help her up.\""
    adv "Jobber stoops down and lowers her hands slowly, still indicating that she is unarmed and non-hostile. Once her mouth is right next to my ear, she whispers, \"Close your eyes.\""
    adv "I do not know why, but I do as she tells me to."

    scene bg white

    adv "Even with my eyes pressed shut, the flash is blinding, like an instant sunrise. I feel myself being violently pulled by my collar backward. I hear a surprised yelp followed shortly by an explosion. \"You aren’t hurt, are you? Get up!\""

    scene bg alley with dissolve
    show jobber neutral right

    adv "\"I’m fine,\" I manage to groan out. It is a complete and utter lie: my throat feels as if it were crushed from getting pulled back so suddenly with such force."
    adv "Jobber smiles. \"That’s a relief. I was worried that I pulled too hard on your collar.\""
    adv "\"You did. You totally did. In fact, I can still feel the pressure around my neck as we speak.\""
    adv "\"But if you say you’re fine, then I’m sure that you’re fine!\""
    adv "I let it go. \"Where are we?\" I wheeze out raspily, rubbing my neck with my hand. I can still feel a slight indentation in the flesh, feel the pumping under my skin as blood rushes to return to the region. I hope this isn’t permanent."
    adv "\"An alleyway. I’m sorry, it looks like someone is after you.\""
    adv "\"After me?\""
    adv "\"Yes, after you. It’s to be expected: you’re under our protection for a reason. But to think that they would strike so early, so soon after your extraction...\""
    adv "\"But... why?\""
    adv "Jobber glances over her shoulder for a second and, after scanning the area, looks back at me. \"You’re... special. You’ve got something, something very rare and valuable.\""
    adv "\"So these people want to take that something from me?\""
    adv "Jobber shakes her head. \"No, it’s not something they can take from you, per se. It’s a part of you, something that makes you, well, you.\""
    adv "I still do not understand, which Jobber seems to understand after seeing my face."
    adv "\"It’s complicated,\" she continues. \"Your past... it gives you the potential. Whether or not you manifest it completely depends on your actions from here on out.\" Jobber motions toward a flaming pile of unrecognizable wreckage with her chin."
    adv "I realize that it must have been the van that we had just been riding in. \"How will you live your life now that people who are willing to do that are after you?\""
    adv "Something is in Jobber’s expression as she looks at the flames, something I cannot recognize. Is it... fear? Almost, but not quite."
    adv "Anger? No, that isn’t right either. It isn’t pain, I knew that. Whatever it is, it makes her face look truly ominous as the light of the flames danced across her visage."
    adv "\"Fire?\" Something about the way she had said that... I cannot get it out of my mind. The way she had whispered that word, it had a tone, a tone that went with this face, this expression. What is it? What emotion could Jobber be feeling right now?"
    adv "\"Miss Jobber?\""
    adv "\"Agent Jobber,\" she corrects automatically, eyes still fixed on the burning wreckage."
    adv "\"Agent Jobber, are you scared of fire?\""
    adv "That catches her attention. She turns and stares at me for a second, then closes her eyes and chuckles."
    adv "\"You really are a perceptive one, aren’t you?\""
    adv "\"I just wanted to know. Sorry, if it’s too hard to talk about, then...\""
    adv "\"No, no, it’s fine!\" Jobber reassures me, waving her hands in front of her quickly. \"Well,\" she starts slowly, \"I’m not sure. Fire and I have... well, the two of us go way back. I think that’s a good way to put it. It’s given, it’s taken. Really, it’s—\""
    adv "\"It’s just beautiful, isn’t it?\""

    show jobber neutral right at left
    show abra neutral left at right

    adv "Both Jobber and I turn, searching for the source of the voice. A woman stands there, smirking."
    adv "Jobber scowls. \"You!\""
    adv "\"Yup, it’s me. I’m here!\" The woman points her finger directly at me. \"Specifically, here for you!\""
    adv "Her upbeat voice is throwing me for a loop. It feels so... off, like a hollow imitation of real happiness. It is the middle of the night, practically pitch black, and there is a burning car close by that encases at least two charred corpses and yet this woman looks as if she is as happy as can be."
    adv "\"You... You... You traitor! Witch! Heretic!\" Jobber stutters out, spitting verbal venom. This expression, unlike so many of her other ones, I recognize instantly: pure, unadulterated fear and anger. \"What do you think you’re doing?!\""
    adv "\"Saving her, of course. You and your crew did kidnap her, after all. It’s only natural to want to rescue her and bring her back to where she belongs.\""
    adv "A shiver runs through me. Back... to where I belong?"
    adv "\"Although,\" she continues, \"now that she doesn’t have a home to return to, I guess I’ll just have to offer her the next best thing.\""
    adv "\"I’m not going to let you take her,\" Jobber growls."
    adv "\"I usually get what I want.\" The woman takes a step toward me."
    adv "Jobber raises her right hand in front of her and points a finger at the woman. The patterns on her coat begin to glow a soft blue. I feel it again: a tingling running down my spine like electricity, making my blood pump faster, my muscles tense up. \"Over my dead body.\""
    adv "\"Fine then. Have it your way.\""

    play sound "sounds/sfx/finger_snap.ogg"
    pause 0.2
    play sound "sounds/sfx/bone_breaking.ogg"

    hide jobber
    show jobber injured right at left

    adv "The woman snaps her fingers, causing Jobber to lower her hand with a yelp."
    adv "Jobber clutches her right hand with her left. That sound, it had been as clear as day: her hand is broken, that I know without a doubt. Even without hearing the bones break, the way she held her hand made it obvious."
    adv "Jobber lets go of her crippled hand, letting it hang uselessly at her side. She lifts up her left hand, but the movement is slow, unsteady. The woman snaps her fingers again."

    play sound "sounds/sfx/finger_snap.ogg"
    pause 0.2
    play sound "sounds/sfx/bone_breaking.ogg"

    adv "Now both of Jobber’s hands are broken. She is disarmed (quite literally), out of options. Her eyes, however, are no less ferocious."
    adv "The woman sighs. \"Honestly, you’re beginning to bore me. I was expecting a lot more out of you.\" Once again, the woman snaps her fingers. This time, however, something feels different."

    play sound "sounds/sfx/finger_snap.ogg"

    adv "Jobber cries out. It sounds as if she is in extreme pain. She didn’t even make these sounds when her hands were being broken."
    adv "\"No...\" Jobber mutters. \"Not like this...\" She gingerly raises her hands and stares down at them in disbelief. I watch in morbid interest as all of her skin begins taking on an unhealthy shade of red."

    adv "\"Please, stop it...\" Small lumps begin forming all over her hands and face. I realize in horror that they are boils, the kind that are caused by severe burns."

    adv "\"Please! Help me!\" Jobber is whimpering now. She is trying her hardest to scream but her throat sounds raspy, as if she has been smoking all her life. \"Please... Not this again...\""

    adv "I will my body to move, to help her, but I can only sit there, frozen in shock and fascination."
    adv "It happens so suddenly. Her skin bursts open like sausages over an open flame. Leaking out of every crack in her skin emerges a flame, licking and lapping at Jobber’s body, consuming her."

    play sound "sounds/sfx/fire_burning.ogg"

    hide jobber injured right
    show abra neutral right at center

    adv "The woman clicks her tongue. \"Such a shame. Her life really did start and end in the flames.\""
    adv "As I sit there, speechless from the horror of it all, the woman turns her attention toward me. She bends down and offers me a hand, smiling."

    adv "This smile... this one is genuine. It isn’t like the one she had been wearing earlier... No, that was nothing but a mask. This... this is her real smile."
    adv "\"So, what do you say? You have nowhere to turn to. The Mages’ Society has been dealt with and your home has abandoned you. Will you allow me to nurture you, pamper you, to tend to your every need and want? If you say it, you will be mine and I will be yours."
    adv "So, tell me..."
    adv "\"Will you accept me as your mother?\""

    $ menu = advMenu
    menu:
        "Yes":
            """
            I try to respond, but my voice gets caught in my throat. I can’t speak. My head is absolutely killing me. The last thing I see before everything fades to black is the woman’s face, still smiling down on me.
            """
        "No":
            """
            I try to respond, but my voice gets caught in my throat. I can’t speak. My head is absolutely killing me. The last thing I see before everything fades to black is the woman’s face, still smiling down on me.
            """

    jump end

label end:
    $ quick_menu = False
    stop sound
    stop music
    scene bg black with fade
    pause 2.0

    return
