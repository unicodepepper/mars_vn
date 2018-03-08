# Welcome to this code. It's not great, but it's mine, and I'm proud of it.

# Message me at unicodepepper@gmail.com or at unicodepepper.tumblr.com/ask
# if you have any questions or want to let me know something, or even just to say hi.

# I appreciate human contact.



define n = Character("Eileen",what_outlines=[(1,"#888",0,0)])
define b = Character("Eileen",what_outlines=[(1,"#888",0,0)])
#define t = Character("Eileen",what_outlines=[(1,"#888",0,0)]0)
define a = Character("Eileen",what_outlines=[(1,"#888",0,0)])
define X = Character("Eileen",what_outlines=[(1,"#888",0,0)])




# The game starts here.
# I think I will go back and add narration to everything, so I don't relay so badly on images.


label start:
    python:
        returned = None # 1 if you return to look for [b_name] while underground, 0 otherwise
        follow = None # 1 if you followed the rover tracks after getting out from underground, 0 otherwise.
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
            $returned=0
            "What's the worst that could happen?"
            "I'm not in danger."
            "I don't want to run out of oxygen, so I should keep going if I want to find an exit sometime."
            "It's not like this place will magically poison me, right?"
            jump a_encounter
        "Go back.":
            $returned=1
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
    "I looked at them with a puzzled face."
    n "How can a machine take care of you?"
    n "Who takes care of it?"
    a "I don't know. They just do."
    a "I can do my job without problems, so I can't complain."
    n "What's your job?"
    a "I'm... a librarian."
    a "I take care of the information that's stored here until the day where humans on the surface have a safe and permanent place to stay."
    a "Until then, it's best for it all to be here."
    n "What kind of information is it?"
    "I unknowingly put my hand on a guard rail."
    a "I'll have to explain to you later. It's probably a lot."
    a "For now, try to stay away from the machines. They're radioactive."
    menu:
        "Radioactive?":
            n "Radioactive? What does that mean?"
            a "How to explain..."
            a "Basically, they work by breaking matter down at an incredibly tiny scale."
            a "What it means for you is that they'll slowly break you down from the inside if you stay too close, and then you'll die before you realize."
            a "And there's nothing we can do about it." 
            n "So ancient humans {i}did{/i} use magic after all..."
            #a giggles
            a "Oh, it's nothing like that."
            a "Just... very advanced science."
            n "Huh."
        "Machines?":
            a "Oh, yeah."
            a "That's where we get energy from."
            a "We have some minerals from the earth that break down with lots of energy. And we capture that to make energy."
            n "I see..."
            n "So ancient humans {i}did{/i} use magic after all..."
            n "That explains how the power cells could go back charged so quickly."
            a "Oh, it's nothing like that."
            a "These machines were built by normal people, just like you and me."
            n "Is that so?"
    "We keep walking silently, and go through another hallway."
    n "It still feels like magic to me."
    jump a_finds_b

label a_finds_b:
    a "Isn't that your friend?"
    "I look over. [b_name] is sitting inside the crashed rover, fiddling with its control panel."
    b "Oh, there you are."
    b "I was so worried about you."
    b "You haven't been replying to my radio messages."
    n "I didn't know I had a radio."
    #change b's expression"
    "[b_name] looks mildly annoyed."
    b "Who is your friend? Do they live here?"
    n "Oh, they are-{nw}"
    a "I'm an archivist."
    a "I'm keeping the legacy of humanity alive underground."
    a "I see you're one of the explorers from the surface, right?"
    a "[n_name] told me there hasn't been much progress."
    a "And based on the state you two are in, I have a guess as to way."
    #change b's expression
    "[b_name] looks even more annoyed."
    b "Hey, it's not our fault."
    b "Accidents happen to anyone."
    a "Don't sweat it."
    jump library  

label b_encounter:
    "The layout here is rather confusing."
    "I try to go back on my steps, but I end up going through another passage."
    "I hear the sound of someone fiddling with keys from here, so I follow that."
    "I quickly find the broken rover, and inside of it, [b_name]"
    n "Hey."
    "They stop fiddling with the controls."
    b "Oh, [n_name]. I'm so relieved to know you're okay."
    "They stand up and give me a tight hug. My heart is racing at this point."
    n "T-thank you, I'm very relieved as well..."
    n "Are we inside the deposit thing? This doesn't seem like a library..."
    b "Well, I have heard that there's a library down here, though maybe it's somewhere else." 
    n "Maybe it's not the time to go looking for it."
    n "After all, we're running out of oxygen, and we need to return home."
    b "Yeah, but the rover is bust."
    b "We're going to need to walk anyways."
    jump b_talky

label b_talky:
    #show b and n in underground hallway
    "This place is a little scary..."
    n "Hey."
    "[b_name] turns to me."
    n "Is it okay if you hold my hand?"
    b "Y-yeah, sure!"
    "They grab my hand a bit tightly and we keep walking."
    n "I hope we don't get lost..."
    b "Don't be silly, that's impossible."
    b "How can we get lost if we already don't know where we are?"
    "Thinking about it that way is even scarier."
    n "Be honest with me."
    n "Do you think we're going to die here?"
    #b pauses
    b "..."
    b "That's a good question."
    b "But I'd like to believe we're not."
    b "After all, if we were going to die anyways, what do we lose for trying not to?"
    n "I guess."
    n "..."
    n "Is there anyone you'd like to say goodbye to?"
    b "I don't know."
    b "Goodbyes are sad."
    n "But they're better than nothing."
    b "I guess."
    b "..."
    b "Do you love me?"
    n "Eh?"
    #n blushes
    n "You're a very important person to me..."
    b "I know, but... {w}I've been thinking about you lately, and... {w}even though we havne't known each other for much, I... {w}I think I..."
    a "Who are you two?"
    "A voice interrupts us from behind."
    a "Are you lost?"
    "We turn around, and there's someone staring at us."
    a "You don't seem to be from around here."
    "I try to speak, but [b_name] interrupts me."
    b "No, we're from the surface."
    b "We fell here because of an accident, and we're trying to get back."
    b "Do you think you could help us?"
    a "Yeah, of course."
    a "Come with me."
    jump library



label library:
    #show a, n and b without their suits. Also show the inside of the library/archive.
    "[b_name] stops suddenly."
    b "I have a quick question."
    a "Huh?"
    b "How come you're breathing without a suit?"
    b "I thought the air outside was poisonous."
    a "Well, we are inside right now."
    #awkward looks
    b "I guess that makes sense."
    "[b_name] takes their helmet off. I follow suit."
    b "What are we here for in the first place?"
    a "I don't know... I think I was just curious about what life was like in the surface."
    a "I've always dreamed of getting back to it, you know?"
    a "I'm aware that they're not there anymore, but..."
    a "I'd like to see the trees, and the rain, and the birds, and the beach..." 
    a "All those precious human things that only exist in memories now."
    a "Not warm ones."
    a "Cold, hard, electric memories. But memories nonetheless."
    b "What do you mean?"
    a "I'm an archivist."
    a "You probably don't know, but human history goes much farther than it seems." 
    #start flashbacks
    a "We're now just a handful, but a long time ago, there were thousands of millions of humans in this planet."   
    a "Back when this planet was called Earth." 
    a "They were a very advanced civilization. They had the power to modify their bodies, cure illnesses, fight back death."
    a "They had the power to change the world, and they did. But instead of fighting death, they allied with her."
    a "They fought each other, with weapons stronger than anything either of us can imagine."
    a "Weapons so strong they turned the air into a smoldering fire, slowly breaking living flesh apart."
    a "That's why we can't breathe outside."
    a "That's why so few of us are left."
    a "We, the ones who remain, are the descendants of a very small group of people, who feared this could be the end of humanity."
    a "They harnessed this destructive force and used its energy to power everything we have today."
    a "And to make sure this didn't happen again, they designated me, as well as many others who are scattered on this underground, to preserve the legacy of humanity." 
    a "At least until the air is breathable again and you, the explorers, find a place where we can finally stay. 
    #end flashbacks
    b "..."
    b "I think I need a minute to think about all of this."
    n "How come none of us knew?"
    
    a "I don't know."
    "[a_name] chuckled a bit."    
    a "It's a little ironic."
    a "But I'm sure you'd have known eventually."
    a "The machines are watching, after all. They never forget, as long as there's someone to look after them."
    b "So what do we do now?"
    "[b_name] interrupted suddenly."
    b "Don't get me wrong, it has been amazing to talk to you, and I'd love to do it again sometime in the future."
    b "But everyone back at the shelter must be extremely worried about you."
    "Oh, no. I almost forgot about the shelter."
    b "Do you have any way we could go back to it quickly?"
    a "Hmmm... It depends."
    a "Do you know of any deposit hatch close to your shelter?"
    b "Yes, there's one."
    b "Do you think you could take us there?"
    a "Yeah, sure. Do you know which one? There's hundreds of them."
    b "..."
    b "I have no idea."
    a "There's not much I can do, then."
    a "..."
    n "Do you think this would help?"
    "I take out the map out of one of the pockets of my suit."
    "The very same map I failed to look at, before causing all of this."
    "[a_name] looks at it."
    a "I can work with it."
    a "Let's go."
    jump escape

label escape:
    #show hallways underground
    "We walk for a while through the hallways."
    "This place is much larger and confusing than I had imagined." 
    "If what [a_name] said is right, then they're not the only one down there."
    "There must be many more archivists working with the machines, on the underground." 
    "But there's no time to meet them all. We have to go back to the surface."
    "After walking for a short time, we get to the bottom of another hatch."
    a "I'm sure this is the place you're looking for."
    #maybe a scene change?
    a "After you're up there, it will only be a short walk back to your home shelter."
    a "..."
    b "So this is goodbye, huh?"
    b "Do you think we'll ever see you again?"
    a "Maybe."
    a "But only if you work hard, and find a place where everyone can live."
    a "Once you do, I'll be sure to find you."
    "I'm holding back tears. Which is weird, because I've never been too emotional."
    if returned:
        "An alarm sounds in the distance."
        n "What's that?"
        a "I don't know, but don't worry about it."
        a "I'll take care of it once I know you two are safe up there."
    n "We still have so much to talk about, you know?"
    n "I'm going to miss you."
    a "I know, [n_name]. But it's for the best."
    a "You might want to lie down instead of standing up, by the way."
    "[b_name] and I comply, and recline in our backs on the platform."
    a "Do your best out there."
    jump surfacing

label surfacing:
    "Immediately, the platform starts moving upwards extremely fast."
    "I can feel my vision blurring."
    "Before I can lose my consciousness, we get to the surface."
    "I check my oxygen level. 15%."
    b "There's no time to lose."
    "[b_name] stands up before me and starts walking towards the shelter, which is visible in the distance."
    "I don't know why, but something about it feels odd."
    "I just walk as fast as I can."
    n "Hey, [b_name]..."
    "It's hard to keep the rhythm. I'm panting between words."
    n "What are we?"
    "[b_name] looks at me and stops for a second."
    b "We can talk about that later, okay?" 
    b "I just want to keep you safe."
    b "You... are very important to me." 
    "Without waiting for me to answer, they keep running along."
    #change of scenes."
    "We finally arrive to the shelter, and [b_name] goes to open the door."
    "But it doesn't budge."
    b "Hey, [n_name]..."
    b "I think the airlock is jammed."
    n "Is there no one inside?"
    "[b_name] walks around the walls of the shelter."
    b "Oh my god..."
    n "What happened?"
    #scene change
    b "This airlock... it's completely destroyed."
    n "Do you think there's anyone left inside?"
    b "..."
    b "The air is poisonous."
    b "If they had time to put on a suit, they'd be smart enough not to just stay inside."
    b "If they didn't have time..."
    b "They all would be dead."
    "We stared at the entrance in horror."
    menu:
        "Should we go inside?"
        "Go inside and see what remains":
            jump inside_endings
        "Go outside and look for survivors":
            jump outside_endings



label inside_endings:
    return

label outside_endings:
    return
    
    
    
    
    
    
    
