##### Characters
define narrator = nvl_narrator
define advNarrator = Character(None, kind=adv)

##### Menus
define menu = nvl_menu
define quick_menu = True

##### Choices
## First Choice
define firstChoice = -1
define loop = 0
define WHERE_AM_I = 0
define WHERE_ARE_WE_HEADED = 1

###### Screens
image diantheCGsketch = "images/diantheCGsketch.png"
image chapterScreenMockup = "images/chapter_screen_mockup.png"

##### Sprites
## Jobber
image Jobber_L = "images/JobberL_Resized.png"
image Jobber_R = "images/JobberR_Resized.png"
image JobberIn_L = "images/JobberInjuredL.png"
image JobberIn_R = "images/JobberInjuredR.png"
## Dianthe
image Dianthe_L = "images/DiantheL_Resized.png"
image Dianthe_R = "images/DiantheR_Resized.png"
image DiantheShock_L = "images/DiantheL_shock_Resized.png"
image DiantheShock_R = "images/DiantheR_shock_Resized.png"
## Mook
image Mook_L = "images/MookL_Resized.png"
image Mook_R = "images/MookR_Reized.png"
image MookIn = "images/MookInjured_Resized.png"
image MookBlood = "images/MookBlood_Resized.png"
## Abra
image Abra_L = "images/AbraL_Resized.png"
image Abra_R = "images/AbraR_Resized.png"

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
    show chapterScreenMockup with fade
    show chapterTitleText "Prologue:\nApocryphal Provenance" with dissolve
    pause 3.0
    hide chapterTitleText with dissolve
    hide chapterScreenMockup with fade
    $ quick_menu = True

    """
    I never really thought of myself as anything but ordinary. My story... No, it’s not one worth telling. Not at all. The paper it would be written on is worth more than the tale itself. At least, that’s how I feel. And yet, you’re here...

    Well, now that you are, you must want to know right? What this is all about? What happened to me? To all of us? Alright, if you say so...

    Where do we begin? Right before? Right after? Now? Then? Well, we need to begin at some point... Stories need both a beginning and an end, right? That’s what Mama always said. Ah, I know...

    Let me just warn you before we start that this story, if it could be called anything, it would undoubtedly, unmistakably, irrefutably be known as...

    Yes indeed, it would be known as a tragedy.
    """
    nvl clear

    show white_bg
    advNarrator "{i}Dad... No...!{/i}"

    play sound "sounds/stabbing_spear.ogg"
    show red_bg
    pause 0.3

    show black_bg
    pause 1.0
    advNarrator "{i}Mama...No, you can't...! Don't leave me alone, please!{/i}"

    play music "sounds/car_on_road.ogg" fadein 4.0

    """
    I am awakened by a cold, hard surface rubbing painfully into my back. I try to move my hands but encounter only resistance. They are tied up then, I conclude.

    Strange, I’m not compelled to struggle against my restraints at all. In fact, I don’t really mind it. There is something faintly familiar and comforting to the thin rope cutting into my wrists.

    {i}Where am I?{/i} Upon regaining consciousness, this is the only thought that occupies my mind. That and, {i}How do I escape?{/i}
    """
    nvl clear

    advNarrator "\"Hey, I think she’s waking up. What do we do, Boss?\""

    """
    I panic. Someone else is in here with me? Looking at me? Who? My stomach churns at the idea that somebody is there and I am here, unable to see, to act. I can’t stand it, the idea that I may be at someone else’s mercy.
    """
    nvl clear

    advNarrator "\"I’ll go ahead and take off her blindfold.\""
    advNarrator "\"Are you sure, Boss?\""
    advNarrator "\"Why not? It’s not like she’s a threat. Having a blindfold wrapped so tightly around her head doesn’t exactly look very comfortable anyway.\""
    stop music fadeout 4.0
    play music "sounds/car_on_road_muffled.ogg" fadein 4.0
    advNarrator "{i}Voices: one woman, one man...{/i}"

    scene white_bg with fade

    """
    The sudden brightness catches me off guard, forcing my eyes to close. When I finally manage to open them just a bit without searing my retinas, I spy a kind-looking face.
    """
    nvl clear
    window hide

    scene alley with dissolve
    show Jobber_L
    show screen clickable_test

    advNarrator "\"Hey there! You alright?\""
    advNarrator "I blink once, confused. {i}She...{w=1.5} she kidnapped me, right?{/i}"
    advNarrator "\"I-I’m fine.\" {i}She kidnapped me, right? Why is she acting so nice to me?{/i}"
    advNarrator "\"Good, I was worried there for a second!\" she says, a huge grin across her face."

    hide screen clickable_test
    $ renpy.notify("You didn't accept the Korok seed. >:(")

    """
    Why is she so concerned my well-being if she is the one who kidnapped me? Maybe hostages in good condition sell for more? Or could she be trying to keep my organs in working order?

	Good question: why was I kidnapped? I need to gather more information. Seeing as my mouth is uncovered and my ability to speak is unimpeded, I ask...
    """

label .choice1_menu:
    menu:
        "Where am I?" if (firstChoice != WHERE_AM_I):
            python:
                firstChoice = WHERE_AM_I
        "Where are we going?" if (firstChoice != WHERE_ARE_WE_HEADED):
            python:
                firstChoice = WHERE_ARE_WE_HEADED

    python:
        if (loop == 0):
            renpy.say(advNarrator, "{i}Let's start with that{/i}, I decide.")
        else:
            renpy.say(advNarrator, "{i}I guess I might as well ask that next{/i}, I think.")

    if (firstChoice == WHERE_AM_I):
        jump .choice1_0
    elif (firstChoice == WHERE_ARE_WE_HEADED):
        jump .choice1_1

label .choice1_0:
    python:
        if (loop == 0):
            renpy.say(advNarrator, "The woman's smile grows wider, but her eyes are filled with a different emotion... Pity, maybe?")
        else:
            renpy.say(advNarrator, "Jobber's smile grows wider, but her eyes are filled with a different emotion... Pity, maybe?")
        renpy.say(advNarrator, "\"Don’t worry, you’re still in Moroes City. You woke up pretty quickly, to be honest. We’ve only just left your apartment; only an hour has passed, at most. I know you’re special, but even I’m impressed by how quickly you recover.\" She giggles.")
        renpy.say(advNarrator, "\"What’s so funny?\"")
        renpy.say(advNarrator, "\"This reminds me of one of my favorite legends. Do you know of the Celtic hero Cú Chulainn?\"")
        renpy.say(advNarrator, "\"He also woke up far too early when he was put under. That landed him in a spot of trouble... Well, I’m sure that nothing like that will happen here.\" On that ominous note, she stops talking.")
    if (loop == 0):
        $ loop = 1
        jump .choice1_menu
    else:
        jump .choice1_merge

label .choice1_1:
    python:
        renpy.say(advNarrator, "\"We’re heading to a private airfield where you can board a plane so that we can get you to our headquarters. That would be...\"")
        renpy.say(advNarrator, "She looks over at a man standing next to her. He is clad in a black trenchcoat, like the ones that the characters wore in that one movie about magic, flying, karate-wielding computer hackers. Had he been the one she had been talking to earlier?")
        renpy.say(advNarrator, "\"Where is it again? It’s on Alcatraz Island, right?\"")
        renpy.say(advNarrator, "The man sighs.")
        renpy.say(advNarrator, "\"With all due respect, Agent Jobber, you’re an American: you should at least know this much. Additionally, as an international agent, you would do well to learn where all of the regional bases of operation are.\"")
        renpy.say(advNarrator, "He sounds exasperated, as if he has to deal with this level of incompetence on a regular.")
        renpy.say(advNarrator,"\"But, all that aside, yes,\" he says, straightening his sunglasses in an effort to regain his composure, \"the American Mages’ Society headquarters is located on Alcatraz Island.\"")
        renpy.say(advNarrator, "\"There you have it!\" the woman, whose name I knew as Jobber, said, looking back at me, beaming. She did not seem even slightly fazed by the man’s exasperated tone.")
        renpy.say(advNarrator, "\"You heard the man! We’re headed to Alcatraz! Isn’t that exciting? It’s quite a popular tourist destination, you know. It’ll be fun, I promise!\"")
    if (loop == 0):
        $ loop = 1
        jump .choice1_menu
    else:
        jump .choice1_merge

label .choice1_merge:
    # merges back into the story
    nvl clear

    """
    She is a whimsical one, that much I can tell. She does not exactly seem great at her job. Is she really an adult? I always thought that adults would take their jobs much more seriously, have a stiff upper lip, and hate the very concept of \"fun\".

    Wait, before that, what were they even talking about? Agents? Mages’ Society? Alcatraz? What was going on?

    {i}Have... Have I managed to get kidnapped by real, actual psychos?!{/i}
    """
    nvl clear

    stop music
    play sound "sounds/car_screeching_to_halt.ogg"
    advNarrator"\"What happened?! What's wrong?!\" the man next to Jobber yells."
    advNarrator "A girl! She just jumped in front of-!"

    play sound "sounds/gunshot_assault_rifle.ogg"
    pause 1.0
    play sound "sounds/finger_snap.ogg"

    """
    The man standing next to Jobber raises his right hand, snapping his fingers. The patterns on his trenchcoat start to glow a faint blue. Jobber does the same. I feel the atmosphere shift a little. There is a slight buzzing in my ears, as if the air with getting filled with electricity, except not quite. A delightful shiver runs through my limbs, begging me to leap into action.
    """
    nvl clear

    advNarrator "\"Proceed with caution. We don’t know the—\""

    play sound "sounds/gunshot_assault_rifle.ogg"
    pause 0.25
    play sound "sounds/glass_shattering.ogg"

    advNarrator "\"Ugh, these bullets... They couldn’t have!\" the man grunts. He seems unharmed but is visibly shocked. \"How did they pierce—?!\""

    play sound "sounds/gunshot_assault_rifle.ogg"

    advNarrator "\"Gah!\""
    advNarrator "This time, the man doubles over in pain, a blotch of red spreading out from his stomach region. He hacks out a cough, spraying crimson all over himself, further staining his coat. The red on black... the contrast stirs something within me."

    play sound "sounds/heartbeat.ogg"

    advNarrator "\"Get down!\" Jobber yells as she roughly pushes me to the floor of the van. She is not a moment too soon; another bullet just barely grazes the top of my head. I think I can see the single strand of hair that was shredded in the incident falling before my eyes."
    advNarrator "Jobber puts her hand to the metal partition that separates the back of the van from the driver and passenger seats but pulls back abruptly with a yelp. She stares at her angry red palm in surprise. \"Heat?\" she whispers out. Her eyes widen in fear. \"Fire?\""

    play sound "sounds/metal_melting.ogg"
    $ renpy.transition(dissolve)
    show screen viewport_test
    pause

label postDianthe:
    show diantheCGsketch

    """
    A girl. Through the melted pool of steel and aluminum lying at the floor of the van steps a girl. Something about her captivated me. Her eyes, purple like amethysts. Purple? Is having purple eyes even naturally possible?

    It was not just her eyes, either. Everything about her struck me as odd and out of place. She could not have possibly been much older than me but her aura... it just felt like she had lived several more lifetimes than me.

    She enters without a sound. Her walking is so graceful that it almost did not seem like she was walking at all. Floating, no, hovering almost. It would not surprise me at all if this girl is just some ephemeral hallucination of mine.
    """
    nvl clear

    scene alley with dissolve
    show Jobber_R

    advNarrator "The girl casually waves the assault rifle she is carrying in my direction. \"I’m here for her,\" she says in a soft, monotone voice."
    advNarrator "She speaks. Even her voice sounds like an illusion!"
    advNarrator "Jobber tightens her grip on my shoulder. \"Not happening. She’s under my protection.\""
    advNarrator "Jobber sees her too. Guess that rules out me going insane."
    advNarrator "\"Please,\" the girl says, raising the barrel of the rifle to point at Jobber without a hint of emotion in her voice."
    advNarrator "\"No,\" Jobber replies resolutely."
    advNarrator "The girl sweeps the barrel of her assault rifle in a wide arch."

    play sound "sounds/gunshot_assault_rifle.ogg"
    pause 0.1
    play sound "sounds/gunshot_assault_rifle.ogg"
    pause 0.1
    play sound "sounds/gunshot_assault_rifle.ogg"
    pause 0.1
    play sound "sounds/gunshot_assault_rifle.ogg"
    hide Jobber_R
    show Dianthe_R

    advNarrator "The smell of spent gunpowder fills the air. The sounds of the wind grow louder, no doubt because of the holes that now pepper the back of the van."
    advNarrator "\"Please,\" the girl asks again, punctuating the request by pointing the rifle at Jobber."
    advNarrator "Jobber lets out a long, dramatic sigh. She slowly raises her hands to the air. \"Alright, you win. Take her.\""
    advNarrator "At first, I feel just a bit betrayed. Didn’t she say I was under her protection? She’s just going to give me up so easily? Then, it hit me: Something’s not right. That was too hammed up, too theatrical."
    advNarrator "The girl motions with her gun. \"Help her up.\""
    advNarrator "Jobber stoops down and lowers her hands slowly, still indicating that she is unarmed and non-hostile. Once her mouth is right next to my ear, she whispers, \"Close your eyes.\""
    advNarrator "I do not know why, but I do as she tells me to."

    show white_bg

    advNarrator "Even with my eyes pressed shut, the flash is blinding, like an instant sunrise. I feel myself being violently pulled by my collar backward. I hear a surprised yelp followed shortly by an explosion. \"You aren’t hurt, are you? Get up!\""

    scene alley with dissolve
    show Jobber_R

    advNarrator "\"I’m fine,\" I manage to groan out. It is a complete and utter lie: my throat feels as if it were crushed from getting pulled back so suddenly with such force."
    advNarrator "Jobber smiles. \"That’s a relief. I was worried that I pulled too hard on your collar.\""
    advNarrator "\"You did. You totally did. In fact, I can still feel the pressure around my neck as we speak.\""
    advNarrator "\"But if you say you’re fine, then I’m sure that you’re fine!\""
    advNarrator "I let it go. \"Where are we?\" I wheeze out raspily, rubbing my neck with my hand. I can still feel a slight indentation in the flesh, feel the pumping under my skin as blood rushes to return to the region. I hope this isn’t permanent."
    advNarrator "\"An alleyway. I’m sorry, it looks like someone is after you.\""
    advNarrator "\"After me?\""
    advNarrator "\"Yes, after you. It’s to be expected: you’re under our protection for a reason. But to think that they would strike so early, so soon after your extraction...\""
    advNarrator "\"But... why?\""
    advNarrator "Jobber glances over her shoulder for a second and, after scanning the area, looks back at me. \"You’re... special. You’ve got something, something very rare and valuable.\""
    advNarrator "\"So these people want to take that something from me?\""
    advNarrator "Jobber shakes her head. \"No, it’s not something they can take from you, per se. It’s a part of you, something that makes you, well, you.\""
    advNarrator "I still do not understand, which Jobber seems to understand after seeing my face."
    advNarrator "\"It’s complicated,\" she continues. \"Your past... it gives you the potential. Whether or not you manifest it completely depends on your actions from here on out.\" Jobber motions toward a flaming pile of unrecognizable wreckage with her chin."
    advNarrator "I realize that it must have been the van that we had just been riding in. \"How will you live your life now that people who are willing to do that are after you?\""
    advNarrator "Something is in Jobber’s expression as she looks at the flames, something I cannot recognize. Is it... fear? Almost, but not quite."
    advNarrator "Anger? No, that isn’t right either. It isn’t pain, I knew that. Whatever it is, it makes her face look truly ominous as the light of the flames danced across her visage."
    advNarrator "\"Fire?\" Something about the way she had said that... I cannot get it out of my mind. The way she had whispered that word, it had a tone, a tone that went with this face, this expression. What is it? What emotion could Jobber be feeling right now?"
    advNarrator "\"Miss Jobber?\""
    advNarrator "\"Agent Jobber,\" she corrects automatically, eyes still fixed on the burning wreckage."
    advNarrator "\"Agent Jobber, are you scared of fire?\""
    advNarrator "That catches her attention. She turns and stares at me for a second, then closes her eyes and chuckles."
    advNarrator "\"You really are a perceptive one, aren’t you?\""
    advNarrator "\"I just wanted to know. Sorry, if it’s too hard to talk about, then...\""
    advNarrator "\"No, no, it’s fine!\" Jobber reassures me, waving her hands in front of her quickly. \"Well,\" she starts slowly, \"I’m not sure. Fire and I have... well, the two of us go way back. I think that’s a good way to put it. It’s given, it’s taken. Really, it’s—\""
    advNarrator "\"It’s just beautiful, isn’t it?\""

    show Jobber_R at left
    show Abra_L at right

    advNarrator "Both Jobber and I turn, searching for the source of the voice. A woman stands there, smirking."
    advNarrator "Jobber scowls. \"You!\""
    advNarrator "\"Yup, it’s me. I’m here!\" The woman points her finger directly at me. \"Specifically, here for you!\""
    advNarrator "Her upbeat voice is throwing me for a loop. It feels so... off, like a hollow imitation of real happiness. It is the middle of the night, practically pitch black, and there is a burning car close by that encases at least two charred corpses and yet this woman looks as if she is as happy as can be."
    advNarrator "\"You... You... You traitor! Witch! Heretic!\" Jobber stutters out, spitting verbal venom. This expression, unlike so many of her other ones, I recognize instantly: pure, unadulterated fear and anger. \"What do you think you’re doing?!\""
    advNarrator "\"Saving her, of course. You and your crew did kidnap her, after all. It’s only natural to want to rescue her and bring her back to where she belongs.\""
    advNarrator "A shiver runs through me. Back... to where I belong?"
    advNarrator "\"Although,\" she continues, \"now that she doesn’t have a home to return to, I guess I’ll just have to offer her the next best thing.\""
    advNarrator "\"I’m not going to let you take her,\" Jobber growls."
    advNarrator "\"I usually get what I want.\" The woman takes a step toward me."
    advNarrator "Jobber raises her right hand in front of her and points a finger at the woman. The patterns on her coat begin to glow a soft blue. I feel it again: a tingling running down my spine like electricity, making my blood pump faster, my muscles tense up. \"Over my dead body.\""
    advNarrator "\"Fine then. Have it your way.\""

    play sound "sounds/finger_snap.ogg"
    pause 0.2
    play sound "sounds/bone_breaking.ogg"

    hide Jobber_R
    show JobberIn_R at left

    advNarrator "The woman snaps her fingers, causing Jobber to lower her hand with a yelp."
    advNarrator "Jobber clutches her right hand with her left. That sound, it had been as clear as day: her hand is broken, that I know without a doubt. Even without hearing the bones break, the way she held her hand made it obvious."
    advNarrator "Jobber lets go of her crippled hand, letting it hang uselessly at her side. She lifts up her left hand, but the movement is slow, unsteady. The woman snaps her fingers again."

    play sound "sounds/finger_snap.ogg"
    pause 0.2
    play sound "sounds/bone_breaking.ogg"

    advNarrator "Now both of Jobber’s hands are broken. She is disarmed (quite literally), out of options. Her eyes, however, are no less ferocious."
    advNarrator "The woman sighs. \"Honestly, you’re beginning to bore me. I was expecting a lot more out of you.\" Once again, the woman snaps her fingers. This time, however, something feels different."

    play sound "sounds/finger_snap.ogg"

    advNarrator "Jobber cries out. It sounds as if she is in extreme pain. She didn’t even make these sounds when her hands were being broken."
    advNarrator "\"No...\" Jobber mutters. \"Not like this...\" She gingerly raises her hands and stares down at them in disbelief. I watch in morbid interest as all of her skin begins taking on an unhealthy shade of red."

    advNarrator "\"Please, stop it...\" Small lumps begin forming all over her hands and face. I realize in horror that they are boils, the kind that are caused by severe burns."

    advNarrator "\"Please! Help me!\" Jobber is whimpering now. She is trying her hardest to scream but her throat sounds raspy, as if she has been smoking all her life. \"Please... Not this again...\""

    hide Jobber_L

    advNarrator "I will my body to move, to help her, but I can only sit there, frozen in shock and fascination."
    advNarrator "It happens so suddenly. Her skin bursts open like sausages over an open flame. Leaking out of every crack in her skin emerges a flame, licking and lapping at Jobber’s body, consuming her."

    play sound "sounds/fire_burning.ogg"

    hide JobberIn_R
    hide Abra_L
    show Abra_R

    advNarrator "The woman clicks her tongue. \"Such a shame. Her life really did start and end in the flames.\""
    advNarrator "As I sit there, speechless from the horror of it all, the woman turns her attention toward me. She bends down and offers me a hand, smiling."

    advNarrator "This smile... This one is genuine. It isn’t like the one she had been wearing earlier... No, that was nothing but a mask. This... This is her real smile."
    advNarrator "\"So, what do you say? You have nowhere to turn to. The Mages’ Society has been dealt with and your home has abandoned you. Will you allow me to nurture you, pamper you, to tend to your every need and want? If you say it, you will be mine and I will be yours."
    advNarrator "So, tell me..."
    advNarrator "\"Will you accept me as your mother?\""

    jump .end

label .end:
    stop sound
    stop music
    show end
    pause 2.0

    return
