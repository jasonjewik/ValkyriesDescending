# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = nvl_narrator
define advNarrator = Character(None, kind=adv)

define menu = nvl_menu

$ choice1 = 0

# The game starts here.

label start:
    stop music

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
    pause 0.2

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

    scene white_bg

    """
    The sudden brightness catches me off guard, forcing my eyes to close. When I finally manage to open them just a bit without searing my retinas, I spy a kind-looking face.
    """
    nvl clear

    scene alley with fade
    show hanamaru_05_03 at truecenter

    advNarrator "\"Hey there! You alright?\""
    advNarrator "I blink once, confused. {i}She...{w=1.5} she kidnapped me, right?{/i}"
    advNarrator "\"I-I’m fine.\" {i}She kidnapped me, right? Why is she acting so nice to me?{/i}"
    show hanamaru_05_01 at truecenter
    advNarrator "\"Good, I was worried there for a second!\" she says, a huge grin across her face."

    """
    Why is she so concerned my well-being if she is the one who kidnapped me? Maybe hostages in good condition sell for more? Or could she be trying to keep my organs in working order?

	Good question: why was I kidnapped? I need to gather more information. Seeing as my mouth is uncovered and my ability to speak is unimpeded, I ask...
    """

    menu:
        "Where am I?":
            $ choice1 = 0
        "Where are we going?":
            $ choice1 = 1

    nvl clear

    if (choice1 == 0):
        advNarrator "{i}Let's start with that{/i}, I decide."
        advNarrator "The woman's smile grows wider, but her eyes are filled with a different emotion... Pity, maybe?"
        jump .choice1_0
    else:
        advNarrator "{i}I guess I might as well ask that next{/i}, I decide."
        advNarrator "Jobber's smile grows wider, but her eyes are filled with a different emotion... Pity, maybe?"
        jump .choice1_1

    label .choice1_0:
        advNarrator "\"Don’t worry, you’re still in Moroes City. You woke up pretty quickly, to be honest. We’ve only just left your apartment; only an hour has passed, at most. I know you’re special, but even I’m impressed by how quickly you recover.\" She giggles."
        advNarrator "\"What’s so funny?\""
        advNarrator "\"This reminds me of one of my favorite legends. Do you know of the Celtic hero Cú Chulainn?\""
        advNarrator "\"He also woke up far too early when he was put under. That landed him in a spot of trouble... Well, I’m sure that nothing like that will happen here.\" On that ominous note, she stops talking."
        jump .choice1_c

    label .choice1_1:
        advNarrator "\"We’re heading to a private airfield where you can board a plane so that we can get you to our headquarters. That would be...\""
        advNarrator "She looks over at a man standing next to her. He is clad in a black trenchcoat, like the ones that the characters wore in that one movie about magic, flying, karate-wielding computer hackers. Had he been the one she had been talking to earlier?"
        advNarrator "\"Where is it again? It’s on Alcatraz Island, right?\""
        advNarrator "The man sighs."
        advNarrator "\"With all due respect, Agent Jobber, you’re an American: you should at least know this much. Additionally, as an international agent, you would do well to learn where all of the regional bases of operation are.\""
        advNarrator "He sounds exasperated, as if he has to deal with this level of incompetence on a regular."
        advNarrator "\"But, all that aside, yes,\" he says, straightening his sunglasses in an effort to regain his composure, \"the American Mages’ Society headquarters is located on Alcatraz Island.\""
        advNarrator "\"There you have it!\" the woman, whose name I knew as Jobber, said, looking back at me, beaming. She did not seem even slightly fazed by the man’s exasperated tone."
        advNarrator "\"You heard the man! We’re headed to Alcatraz! Isn’t that exciting? It’s quite a popular tourist destination, you know. It’ll be fun, I promise!\""
        jump .choice1_c

    label .choice1_c:
        # remerges the choices

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

    """
    A girl. Through the melted pool of steel and aluminum lying at the floor of the van steps a girl. Something about her captivated me. Her eyes, purple like amethysts. Purple? Is having purple eyes even naturally possible?

    It was not just her eyes, either. Everything about her struck me as odd and out of place. She could not have possibly been much older than me but her aura… it just felt like she had lived several more lifetimes than me.

    She enters without a sound. Her walking is so graceful that it almost did not seem like she was walking at all. Floating, no, hovering almost. It would not surprise me at all if this girl is just some ephemeral hallucination of mine.
    """
    nvl clear

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

    advNarrator "The smell of spent gunpowder fills the air. The sounds of the wind grow louder, no doubt because of the holes that now pepper the back of the van."

    return
