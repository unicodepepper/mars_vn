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
    menu:
        "Try to be friendly":
            n "Hello everybody! My name is [n_name] and I'm really happy to be here!"
            n "I don't have a lot of experience with this kind of work, but I'll do my best!"
            n "I'm really glad to be able to work with all of you."
            "Everyone looks at me silently."
            "Some people are smiling at me. I try to smile back."
            "This kind of thing might not really be for me. But I really need to leave a good impression."
            X "I like your cheerfulness."
            X "I'm sure you'll work really hard out in the field."
        "Just get over with it.":
            n "Hey there."
            n "I'm happy to be here."
            X "Ah, I see you aren't a person of much words."
            X "That's okay. I'm sure you'll put all that energy and attention towards exploration out there."
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
    "And it's kind of tiresome to be standing here with this heavy suit on."
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
    "Every once in a while, [b_name] sticks a machine out and tells me where to head next."
    b "As you can see, we're following a trail that was already there, placed by another exploration team."
    b "The next time, we'll be making our own trail."
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
    "A worn-out, but large metal hatch sits on the ground. [b_name] steps on the edge, and it immediately opens."
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
    "It immediately goes down along the side of the shaft, like it was dropped."
    "I struggle not to get sucked inside because of the air flow."
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
    #scene bg bed and show n in their pajamas
    "I can't believe [b_name] really said that."
    "Is that how they really feel about me?"
    "I covered my face with the blanket."
    "I've only been here a few days, and yet things have gotten this awkward..."
    "No, wait a second. I can't keep thinking like that."
    "I'm going to do my best when working, and make them proud."
    "That way, if they... {w}if they really want to be something else, they'll ask me directly."
    "..."
    "I sound so dumb it's embarrassing."
    "I should probably just go to sleep. Tomorrow is another day, after all."
    "Important matters are best discussed with a pillow, after all."
    jump lost

label lost:
    #scene bg black
    "I wake up a little later than yesterday, but still quite early."
    #show bg outside here?
    "After I'm done suiting myself up, I go outside, only to find [b_name] dozing off outside. While still wearing their suit."
    "I gently kick nudge them with my foot, and they wake up with a jolt."
    #show b
    b "Oh, hey there!"
    b "Have you been there for long?"
    n "No, I just got here."
    "I can tell they've barely slept."
    b "We've got a large area to survey so let's get ready, shall we?"
    "I nod and we get into the rover."
    #scene bg rover"
    "After a few minutes of driving, I can tell [b_name] is falling asleep again."
    n "Hey, is it okay if I ask..."
    n "You didn't sleep well yesterday, did you?"
    "They seem to be a bit embarrassed about this question."
    b "Not really..."
    b "I was thinking about a lot of things."
    n "Is that so?"
    n "I wonder what's so important enough for you to lose your sleep."
    n "Or should I say who?"
    b "H-hey!"
    b "I think..."
    b "I think we should have this conversation some other time."
    b "Do you mind handling the radio as you drive? I think I'm gonna take a nap in the back."
    b "Wake me up if you get near the end of our map, okay?"
    b "We haven't explored most of the area that's far in this direction."
    "With that, they just laid down on the back of the rover."
    "I'd be surprised if they can catch any sleep with all this movement."
    "But it's not that bad. I really enjoy driving."
    "In fact, I could spend all day doing it."
    #scene sunset?
    "[b_name] wakes up, slightly agitated."
    b "Where are we?"
    b "I don't think this is anywhere near the map we had."
    n "Is that so?"
    n "It all looks the same to me."
    "[b_name] comes back to the front."
    b "Haven't you been checking the map?!"
    "I stop the vehicle immediately."
    n "I'm sorry, I forgot."
    "It doesn't feel like a valid excuse, even to me."
    b "It's getting late."
    b "How are we supposed to get back?"
    n "I... don't know."
    n "We could maybe turn around and follow the tracks?"
    "[b_name] seems surprised."
    b "That's... actually a good idea."
    "They start looking around trying to orient themselves, then quickly panic."
    b "We are not gonna make it."
    n "Huh?"
    b "My oxygen tank is at 30%%."
    "I check mine. It was at 25%%."
    n "Don't we have spare tanks?"
    b "Yeah, but just a single one."
    b "We'd have to go back as fast as we can, in a straight line, and even then..."
    b "It's just a slim chance that we make it."
    b "Especially if we are continuously sharing the tank."
    n "What?"
    "I felt my gut sinking inside me."
    "Are we going to die out here? Because of my own incompetence?"
    b "We have no time to lose."
    b "Try to remain calm, so we don't waste any oxygen."
    "I drive forward with all the power of the vehicle."
    "After a few seconds, a loud metallic bang stops us completely."
    b "What happened? Did you crash into something?"
    "I'm scared for my life."
    n "I did not!"
    "I wonder if we're stranded."
    "[b_name] gets out of the vehicle to check on it."
    b "The front wheel is bust."
    n "But we're out in the open. What could I have possible crashed into?"
    "[They wipe out some dust from the surface, revealing a metallic plate underneath."
    b "...I think you just crashed into a deposit hatch."
    "As soon as they finish saying this, the hatch drops. We're falling underground."
    jump fall

label fall:
    #have a cutscene where the rover and/or characters are shown falling as silhouettes
    #after they fall, the screen blacks out a bit, and slowly comes back in a dizzy way. 
    "Where am I?"
    "My entire body hurts."
    "The last thing I remember is... I was exploring on the outside, and then we fell down a-"
    #n stands up suddenly
    "We fell down the deposit hatch!"
    "I am surprised I'm not dead."
    "I really hope [b_name] is okay."
    "It's probably a good idea to start looking for them."
    #n gets up and starts walking
    "This place is quite dark, and it seems really complex."
    "There is a faint cyan light to everything."
    "I walk up to one of the machines, and I see a very large symbol on it."
    "It's a symbol I've never seen before."
    #show radioactive picture
    "I wipe some of the dust that's covering it."
    "Should I keep going this way, or go back to look for [b_name]?"
    menu:
        "Should I keep going this way, or go back to look for [b_name]?"
        "Keep going.":
            "What's the worst that could happen?"
            "I'm not in danger."
            "I don't want to run out of oxygen, so I should keep going if I want to find an exit sometime."
            "It's not like this place will magically poison me, right?"
            jump a_encounter
        "Go back.":
            "There's something about this place I don't like."
            "It feels... dangerous."
            "I take a step back and return to where I was before."
            jump b_encounter

label a_encounter:
    "I didn't realize at first the scale of this place."
    "There's machines as far as the eye can see."
    "This is probably made from the ancient humans, isn't it?"
    "I think [b_name] mentioned something like that."
    "After a few minutes of walking, I find something that looks like a door, and I push it open."
    "There's someone inside."
    n "Hello?"
    "They seem, understandably, quite startled."
    a "Oh, hey."
    a "Did you get lost?"
    n "No?"
    n "Well... yes."
    n "I fell here from the surface."
    n "Do you think we can go back?"
    a "Oh, the surface!"
    a "I haven't seen anyone from there in such a long time."
    a "How is the exploration going?"
    n "As far as I know, we haven't found anything."
    n "But [announcername] said that we were close to finding something. So maybe we will."
    a "Ah, I see."
    a "You aren't alone here, are you?"
    a "If I recall correctly, all the exploration is done in teams."
    n "Yeah, there's someone else inside here, but..."
    n "I lost them after falling down."
    n "Do you think they'd be okay?"
    a "I'm sure of it. You're okay as well, after all."
    a "Let's go looking for them, shall we?"
    "[a_name] grabs a small device which opens a door, and then we walk out of it."
    jump a_talky

label a_talky:
    n "So..."
    n "Are you the mechanic who takes care of these machines?"
    "[a_name] thinks about it for a while."
    a "Not really."
    a "I'd say that the machines take care of me instead."
    return
label b_encounter:
    return

 
