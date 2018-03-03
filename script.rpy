define n = Character("Eileen",what_outlines=[(1,"#888",0,0)])
define b = Character("Eileen",what_outlines=[(1,"#888",0,0)])
#define t = Character("Eileen",what_outlines=[(1,"#888",0,0)]0)
define a = Character("Eileen",what_outlines=[(1,"#888",0,0)])
define X = Character("Eileen",what_outlines=[(1,"#888",0,0)])




# The game starts here.
# I think I will go back and add narration to everything, so I don't relay so badly on images.


label start:
    jump veggies

label veggies:
    #scene bg greenhouse
    #show b inside suit, serious

    b "And after you finish watering and cleaning the ground, it's just a matter of waiting until the next day."
    b "These are almost ripe, so we should check them out often so they don't spoil."
    n "Not really..."
    n "But I'm sure I'll get up to speed soon!"
    b "That's the attitude."
    b "We're a very small group, so every little bit of help is crucial."
    b "We can't waste any time, either; since we have limited resources."
    b "Meet me at the dining hall when you're ready, okay?"
    #b leaves
    "[b_name] made a satisfied sigh and left the greenhouse."
    "This is my first time doing something this serious, and it feels like such a jarring change."
    "I've lived all my life on the southern bunker."
    "But now, I've been chosen to help with the exploratory missions to find permanent water sources."
    "If what everyone says is right, then after we find a proper place to settle we won't need to live in bunkers or shelters anymore."
    "Until then, all I can do is work hard. {w}And I want to work hard."
    jump welcome

label welcome:
    #scene bg cafeteria / show b and n in inside clothes
    "The cafeteria in this shelter is small, yet it somehow feels very spacious and cozy."
    "There's someone who seems to be leading the process, preparing and serving everyone."
    "The food looks much more delicious than what I ate back in the bunkers."
    "I wonder if they've grown it right here..."
    b "Are you hungry?"
    n "Just a little. Are we going to eat right now?"
    b "In a bit. Just after a quick announcement."
    #Show announcer (?)
    "The leader stood up in front of the table, and everyone turned to them."
    X "Good evening, my children."
    X "As usual, our exporatory team has been working hard to map the territories around our shelters, especially the northern ones."
    X "Despite the unforgiving geography of the area, we believe it has a huge probability of harboring a safe haven for us to settle."
    X "The way they've risked their lives in this dangerous environment will not be in vain, since we're closer than ever to our goal."
    X "Today we have received a new member of our family, who will help you tomorrow on our exploratory missions."
    #Announcer turns to N
    "They turned to me."
    X "Do you have any words to share with everybody?"
    choice:
        "Try to be friendly":
            n "Hello everybody! My name is [n_name] and I'm really happy to be here!"
            n "I don't have a lot of experience with this kind of work, but I'll do my best!"
            "Everyone looks at me silently."
            "Some people are smiling at me. I try to smile back."
            "This kind of thing might not really be for me. But I really need to leave a good impression."
            X "I like your cheerfulness."
    n "I... I'm really glad to be able to work with all of you."
    X "Ah, I see you aren't a person of much words."
    X "That's okay. I'm sure you'll put all that energy and attention towards exploration out there."
    X "I've received compelling information regarding a possible settlement on the far north, so hopefully your stay won't be too long."
    X "With all that out of the way, let's get to eat, shall we?"
    #now everyone is eating
    n "How long has [announcer_name] been in charge of here?"
    b "I don't know. They were here back when I arrived last year."
    b "But we've had a lot of progress since then, you know? I'm sure they're a great leader."
    n "I hope I can be liked by everyone as well..."
    jump goodnight

label goodnight:
    #scene bg rooms
    #show everyone in their pajamas
    X "I'm sure you'll put all that energy and attention towards exploration out there."
    X "I've received compelling information regarding a possible settlement on the far north, so hopefully your stay won't be too long."
    X "With all that out of the way, let's get to eat, shall we?"
    #now everyone is eating
    "The looks of the food weren't lying."
    "This is easily one of the most delicious meals I've ever had, and I don't even know what it is."
    "I spend most of the dinner in silence, with everyone talking around me."
    "A little bored of it, I try to strike a conversation with [b_name]."
    n "How long has [announcer_name] been in charge of here?"
    b "I don't know. They were here back when I arrived last year."
    b "But we've had a lot of progress since then, you know? I'm sure they're a great leader."
    n "I hope I can be liked by everyone as well..."
    jump goodnight

label goodnight:
    #scene bg rooms
    #show everyone in their pajamas
    "The rooms weren't really what I expected."
    "They seemed to be very frugal, yet somehow they managed to look extremely comfortable."
    b "...And this is where you'll be sleeping."
    b "It's not the largest or coziest of places, but it's yours. Go nuts."
    b "You're lucky - a few months ago we just slept in a communal area. It was really hard to convince [announcer_name] to let us build them."
    n "I see..."
    #n blushes a bit
    n "Thank you for worrying about everyone, instead of getting carried away with just looking for something outside."
    #b blushes back
    "[b_name] blushed lightly. I don't think they're used to being complimented."
    b "Oh, it's nothing. A good morale helps everyone do their best, doesn't it?"
    b "By the way, I think you should go to sleep as soon as you can."
    b "We're waking up tomorrow earlier than usual for a field practice - just the two of us."
    b "I'll show you the ropes of how this exploration thing works."
    jump snzz

label snzz:
    #scene bg bed
    #show n lying down (maybe as a cg?) in pajamas
    "Today was a slower day than I was expecting."
    "It should not be a surprise, though, since it's just my first day."
    "I wonder if I'll be able to keep up with it once it gets harder, later on."
    "If it gets much harder, after all."
    #n smiles maybe
    "but [b_name] is such a nice person to work with, and they seem to know a lot about this as well."
    "I'm sure I'll do great if I get to work by their side."
    jump riseandshine


label riseandshine:
    #scene bg rooms
    #show n in space suit
    "I'm really sleepy."
    "Did I wake up too early? [b_name] said they'd be there by now."
    "And it's kind of tiresome to be standing here with this heavy suit on.""
    #if you were bold during the introduction?
    # show b
    "Out of nowhere, [b_name] appears behind me."
    b "Oh, hey there, [n_name]."
    #show n surprised
    n "W-were you behind me all the time?"
    b "No, I got here just now."
    b "Have you ever gone outside of here, through the airlock?"
    n "Never in my life."
    b "Not even on the way here?"
    n "N-no... I was inside a sealed vehicle during transport. I couldn't even see outside."
    b "You're in for a pleasant surprise, then."
    b "Come with me."
    "[b_name] opens the airlock and we walk outside."
    #scene bg outside
    #show n and b in space suits
    "The landscape is enormous. I have never seen something so absurdly spacious. Not directly, at least. It could very well be infinite."
    b "So what do you think?"
    b "Pretty, isnt' it?"
    n "It's so wide... and red..."
    b "Oh, it wasn't always red. Or so I've heard."
    n "Is it like this everywhere?"
    b "We don't know. That's why we are still exploring."
    b "Do you know how to drive?"
    n "Drive?"
    b "That."
    #show rover
    "[b_name] points to a vehicle, much smaller than the one I came here in."
    "I've never in my life driven one of those."
    b "It's fairly straightforward."
    b "You just use your foot to go forward and turn with your arms."
    b "I want you to get the hang of it as soon as possible, so you can go exploring alone."
    b "Or even better, train more people."
    n "Why don't you drive instead?"
    b "I don't know if you've noticed, but my eyesight is pretty bad."
    b "I think it's best if you do it instead."
    b "Let's get on with it, okay?"
    n "Don't I need training for that?"
    "[b_name] ignores me, as we jump inside. I follow suit, because I really have no option."
    jump vroom

label vroom:
    #change scenes to the rover cg
    "The vehicle is much easier to handle than I expected, but still a bit difficult to steer."
    "I'm thankful that we're out here in the open, because otherwise I'm sure I'd have crashed into some obstacle."
    b "I have to say, you're doing surprisingly well, for someone who just grabbed this for the first time."
    n "I usually learn things much faster by doing them."
    n "And I always want to do my best, whenever I can."
    b "Has anyone told you before what a sweet person you are?"
    #n blushes
    "That comment caught me off guard."
    n "W-what?"
    b "Ah, nothing, nothing."
    b "Let's just focus on the focus."
    #another scene change to the cliff
    b "Hey."
    "[b_name] breaks my concentration."
    n "Huh?"
    b "Stop the rover."
    n "...Okay"
    "I press the brake lightly, until the vehicle rolls to a stop."
    b "Do you see that wall of rock all the way there?"
    "I raise my eyes and squint my vision. I can barely see it, but there is indeed a huge rock wall on the distance, stretching all over the horizon."
    b "It's not very noticeable from here, but if we were closer, you'd notice how large it is."
    b "That's as far as we have explored."
    b "We {i}could{/i} get past it, but it's so far away that there would be not enough oxygen to bring everyone across."
    b "I've heard there is a very habitable zone after that, which could mean that we won't need oxygen suits anymore."
    b "But it's a huge risk to take. And if we're wrong, we won't have enough to go back to the shelter, and everyone will die."
    b "In fact, you might have noticed that your tank is almost at 50%%."
    b "Let's return to the shelter, okay?"
    n "..."
    b "Is something wrong?"
    n "Oh, not at all."
    n "I'm sorry."
    "I start driving and turn the vehicle around."
    jump harvest

label harvest:
    #scene bg greenhouse
    "We went through the airlock fairly quickly after returning."
    "Despite having such a heavy suit on during the long trip, I didn't feel exhausted at all."
    "Probably because of how excited I am."
    b "What did you think about our small trip?"
    n "It was... beautiful."
    n "But also a bit scary."
    b "Don't worry, you get used to it."
    b "And I'll make sure you don't get hurt"
    #n blushes THIS TIME THE GOOD WAY
    #b giggles
    b "Remember those plants I showed you yesterday? The ones that were almost ripe."
    n "Yeah? Are they ready now?"
    b "Yes. And you'll help me harvest them."
    "[b_name] hands me a sharp tool."
    b "Remember to take them from the plant gently, since they're very sensitive and we don't want to damage them."
    b "They're our only source of oxygen, after all."
    b "I'll go get a bag."
    "While [b_name] returns, I carefully start cutting the fruits and vegetables out and placing them on the floor."
    "I could get used to this."
    #scene change? picking the food up. now the bags are shown.
    "[b_name] comes back with a bag full of bags, and pulls them all out."
    n "Isn't that a bit too many bags?"
    "I look at the pile of vegetables in the floor. It could easily fit in a single one."
    b "Oh, yeah - we are depositing the rest. There's a lot left to harvest, after all."
    n "Depositing?"
    b "Yeah, depositing."
    n "So you'll be able to eat them later?"
    b "Not really."
    b "I'll explain to you if you help me get them outside."
    "I grab a bag and start placing the plants I harvest in it."
    "It's a bit monotonous, but much easier than working outside."
    jump deposit

label deposit:
    #scene bg outside
    #show n and b in their space suits
    "After loading most of the bags in the rover and leaving some inside, we depart."
    "This time, we're heading on the opposite direction as this morning."
    b "Have you wondered how all the energy we use is generated?"
    b "You know, powering the rover, heating, air filtering and all that stuff."
    n "No? I have no idea. I thought you used solar panels, or something like that."
    b "I have no idea either. But I know where we get it from."
    "Suspicious."
    b "We just have to deposit our surplus food every week, along with the depleted power cells, and in a few minutes we'll get them back fully charged."
    n "Deposit where?"
    b "Right here."
    "I slowly press the brakes, and [b_name] steps out of the vehicle."
    #show cg hatch
    "A worn-out metal hatch sits on the ground. [b_name] steps on the edge, and it immediately opens."
    n "...That looks a little dangerous."
    # b chuckles
    b "Not that I'd be able to tell anyways."
    n "Do you have any idea of what's down there?"
    b "I don't know a lot, but from what I've heard, it's some sort of library."
    b "It was there when I came here, anyways."
    n "Why would a library be down there? And where would they get {i}their{/i} energy anyways?"
    b "..."
    b "That's a very good question."
    b "Who knows, maybe they get energy from the ground."
    b "I've heard the ancient humans could do that."
    n "Ancient humans?" #maybe turn this into a selection thing (were ancient humans magic? they were really close)
    menu:
        "Did ancient humans use magic?":
            b "Magic?"
            b "..."
            b "Who knows."
            b "I've heard lots of stuff about them, but never something like that."
            b "Now that you say so, it would explain a lot about them. They could do a lot of weird stuff."
        "How \"ancient\" do you mean?":
            b "I heard the ancient humans dissappeared centuries ago."
            b "Something about a great war."
            b "I've just heard the rumors that go around, so take it with a grain of salt."
    b "Anyways, can you help me put these in the cart?"
    b "Take care of not dropping them. They'd be ruined."
    "We finish loading the cart, and [b_name] presses a button."
    "It quickly goes down along the side of the shaft, like it was dropped."
    "After a few seconds, it comes back up, and only the power cells are in it."
    n "Huh? You said it would take a few minutes."
    b "Well... it varies. But aren't you glad we didn't have to sit around waiting?"
    n "Yeah, that's nice."
    "[b_name] finished loading the power cells back into the rover, and we drive back to the shelter."
    jump cafe

label cafe:
    "We go inside again, with our suits full of sand."
    "[b_name] goes to put the power cells away, while I get ready to eat."    
    "I enter the cafeteria, and everyone is already getting prepared to eat."
    X "Please feel treat yourself to a plentiful meal. This last harvest was extremely successful, and it's all thanks to you."
    "I just sit down, and start eating in silence."
    jump flirt

label flirt:
    #scene bg rooms and show b and n in pajamas
    "I leave the cafeteria, and find [b_name] in the hallway."
    n "Oh, hey."
    n "You seem exhausted."
    b "Yeah, I've been installing batteries all over the place."
    b "But don't worry, I already had something to eat."
    n "I... I wanted to say sorry for making you late today."
    n "It's probably a chore to be teaching me all the time."
    b "Oh, it's okay. It's not really a big deal?"
    b "Besides, I really like going exploring with you, you know?"
    b "And explaining things to you... {w}and talking to you... {w}and working with you.. {w}and.." #N blushes proggressively
    n "D-do you mean-"
    b "Eh?"
    "I can feel my ears getting warmer."
    b "Nonono it's not like that!"
    b "Well, I-"
    b "I think it's not, but... I don't know..."
    n "I..."
    n "It's okay."
    n "Let's work hard tomorrow, okay?"
    n "Y-yeah, let's do it!"
    "I practically run inside my room."
    jump sleeb

label sleeb:
    "
