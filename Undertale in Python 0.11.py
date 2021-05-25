MaxHP = 20
HP = MaxHP
print("Name the fallen human:")
Name = input()

if Name == "Chara":
    print("The true name.")
elif Name == "Flowey":
    print("???: 'Don't try anything funny, you clown!'")
elif Name == "Toriel":
    print("???: '*gasp* I am shocked, my child.'")
elif Name == "Jack":
    print("Jack: 'Are you the creator?'")
elif Name == "Elliot":
    print("Elliot: 'I am da main tester!'")
elif Name == "G" or Name == "Gaster":
    quit()
elif Name == "Sans":
    print("???: 'Do you wanna have a bad time?'")

print("Are you sure? Yes or No")
CheckName = input()

if CheckName == "No":
    print("Choose another name, this is your final chance!")
    Name = input()

print("You wake up on a field of flowers in a dark room.")
input("Your back stings but the flowers are comforting in such a scary place.")
print("Get up? Yes or No (which shall now be for every choice)")
FallingRoom = input()

if FallingRoom == "No":
    print("You lie there...")
    print("Try and get up again?")
    FallingRoom = input()

    if FallingRoom == "No":
        print("Umm...")
        input("I guess I'll tell you some lore.")
        print("Wanna hear?")
        LoreReading = input()

        if LoreReading == "Yes":
            print("Where to start...? I know! I'll tell you my name!")
            input("My name is...")
            input("Startled, you get up.")
        else:
            print("Feeling better after not hearing spoilers, you get up.")
input("You walk over to a large door with a symbol above it.")
input("As you enter, you see a small sunflower in the distance.")
print("Look closer?")
ExamineFlower = input()

if ExamineFlower == "No":
    print("A voice says, 'Don't run away,", Name)
input("As you step closer, it starts talking:")
input("???: 'Howdy! I'm Flowey, Flowey the Flower.'")
input("Flowey: 'You're new to the Underground, aren't cha?'")
input("'I guess I'll have to show you how things work around here!'")
input("You see a red heart in front of you.")
input("'That is your soul. Your SOUL starts of weak, but you can upgrade it with LV.'")
input("'What's LV? Why, it's LOVE of course! You want some LOVE, don'tcha?'")
input("'Down here, LOVE is shared through little white friendliness pellets.'")
print("It throws some white ovals at you. Dodge them?")
DodgeBullets = input()

if DodgeBullets == "Yes":
    print("'You know what's going on here, don't you.'")
    input("'To think you were them is stupid of me.'")
elif DodgeBullets == "No":
    print("The ovals hit you and you are hurt.")
    HP = 1
    input("HP =", HP)
input("'You idiot!'")
input("'Who would pass up an opportunity like this, huh?'")
input("'Toodle-oo, kiddo. DIE!'")
input("Ovals surround you, what will you do?")
input("A flame appears in front of you and hits Flowey.")
input("A figure resembling a goat walks up to you.")
input("???: 'What a miserable nasty creature torturing such poor innocent youth.'")
input("'Oh, my child, I am Toriel, caretaker of the RUINS.'")
if DodgeBullets == "No":
    input("Toriel: 'Oh, let me heal you.'")
    HP = MaxHP
    input("HP =", HP)
input("Toriel: 'Come and I will take you to my home.'")
print("Follow her?")
FollowToriel = input()

if FollowToriel == "No":
    print("'*sobs* My child... *sobs* Goodbye...")
    input("Toriel runs off, crying.")
    input("???: 'So, you're too stupid to follow Mom, huh?'")
    input("You turn around to see Flowey laughing maniacally.")
    input("Flowey: 'I had a back-up plan for this, Frisk.'")
    input("'Oh, you don't know? You're not them at all!'")
    input("'That's right, they were my best friend!'")
    input("'And you dare make our Mom mad!'")
    input("'Come on, let's kill Frisk once and for all!!!'")
    input("You feel a rumbling in the ground... wait why is my voice disappearing?")
    input("Well, um, see y-")
    input("And that's the end of that!")
    input("Jack: 'Picture you getting thrashed.'")
    input("YOU DEAD, SON!")
    input("Cause:")
    input("Getting thrashed by inhumanly beings (eg. a flower and a demon)")
if FollowToriel == "Yes":
    input("'Well then, let's get going!'")
    input("You follow Toriel into a room with a yellow star.")
    input("As you step towards it you feel a warmth in your 'SOUL'")
    input("'Are you coming or not, my child?'")
    input("You continue into a room with a Froggit in it.")
    input("Froggit bounces towards yo-")
    input("You hear a voice on the wind, Jack: 'Play Undertale Fight Simulator Beta for that, oooooooooooo'")
    input("'Link on the Gamejolt page! ohohohhoohohhoho'")
    input("You turn to face at a room of spikes.")
    input("'Look at this, my child, it is a puzzle! You probably shouldn't do that, not without me?'")
    print("Do it by yourself anyway?")
    SpikePuzzle = input()

    if SpikePuzzle == "Yes":
        print("'Ok, give it a try!'")
        input("You try and walk around the spikes.")
        input("YOU DIED!")
        input("Cause:")
        input("SPIKES, YOU IDIOT!")
    if SpikePuzzle == "No":
        print("'Ok then, my child!'")
        input("Toriel, looking as if she knew how to get through here of by heart, took you across.")
        input("'Onward!'")
        input("You enter a long hallway,")
        input("'Now, you must have a small test. Do not worry, it is only a test of independence.'")
        input("'You must walk across this hallway, by yourself. Easy enough, right?'")
        print("She runs off, should you follow her?")
        FollowToriel2 = input()

        if FollowToriel2 == "No":
            print("2 years later:")
            input()
            input("1 eternity later:")
            input()
            input("Well, this is boring!")
            input("YOU DIED")
            input("Cause:")
            input("Old age?")
        elif FollowToriel2 == "Yes":
            print("You walk along the hallway, and it's soooooooooooo boring!")
            input("How about I sing something for you!")
            print("Would you like that? *invisiblepuppydogeyes*")
            SingSong = input()

            if SingSong == "Yes":
                print("Let's go, child!")
                input("COLOURS WEAVE INTO A SPIRE O-")
                input("???: 'NOOOOOOOOOOOOOO!")
                input("You fall on the floor.")
                input("YOU DIED!")
                input("Cause:")
                input(
                    Name, "is rubbish at singing. So bad, they killed you. Well done. oh and also copyright issues.")
            if SingSong == "No":
                print("ahhhhh come on!")
                input("meanie")
                input("Fine, let's just get this over and done wi-")

input("???: 'Hello again! I see you've downloaded this for the 7th time. Well done to you. Oh yeah, I'm Jack btw.'")
input("Jack: 'I may have sort-of kind-of lied about leaving this project alone.'")
input("Jack: 'I just had a brain-wave at school in the middle of a boring lesson about ideas for this and the fight simulator.'")
input("Jack: 'I probably won't continue with this but I might come back to it. Maybe.'")
input("Jack: 'Well, you should go continue on with your day. You might be having fun. Unlike me. :('")
print("END")
