import random

def main():
    PlayerHealth = 20
    FroggitHealth = 20
    PlayerDead = 0
    FroggitDead = 0
    FroggitSpared = 0
    FroggitCalmed = 0
    FroggitAngered = 0
    FroggitBurnTime = 0
    BurnEnabled = 0
    WeaponList = ["a", "b", "c"]
    ArmourList = ["a", "b", "c"]
    print("You wake up in a dark and damp room.")
    print("Suddenly, the lights turn on!")
    print("You notice some items in front of you, a few weapons and some pieces of armour.")
    print("An ominous voice bellows at you from above.")
    print("???: 'You must take one of each to prepare.")
    print("You wonder what for, but decide not to question it.")
    input("You look down at the weapons and think about which to pick.")
    input("Option A: Stick - Only being small, it won't do much, but it's better than nothing.")
    input("Option B: Burnt Pan - Hot to the touch. Lifting it, it feels heavy enough to knock someone out.")
    input("Option C: Toy Knife - Made of foam. It'll do next to nothing, but it might scare someone.")
    print("Which weapon do you want? A, B or C?")
    WeaponChoice = input().lower()
    if WeaponChoice not in WeaponList:
        WeaponChoice = random.choice(WeaponList)
        print("You can't decide which weapon to choose.")
        print("The voice speaks again.")
        print("???: 'You really can't choose? Fine. Take Option", WeaponChoice.upper())
        DumbLevel = 1
    if WeaponChoice == "a":
        PlayerMinDamage = 2
        PlayerMaxDamage = 5
        print("You pick up the stick.")
    elif WeaponChoice == "b":
        PlayerMinDamage = 5
        PlayerMaxDamage = 7
        BurnEnabled = 1
        print("You pick up the pan.")
    elif WeaponChoice == "c":
        PlayerMinDamage = 0
        PlayerMaxDamage = 1
        print("You pick up the toy knife.")
    print()
    print("???: 'Good, now pick something to defend yourself with.'")
    input("You take a closer look at the armour in front of you.")
    input("Option A: Faded Ribbon - A red ribbon that has long lost its lustre. You'd look cute enough to not attack with it on.")
    input("Option B: Manly Bandana - A small bandana that has some abs drawn on. With it on, you'll have protection from its sheer manliness.")
    input("Option C: Bandage - An old, worn piece of cloth that won't protect you from anything.")
    print("Which piece of armour do you want? A, B or C?")
    ArmourChoice = input().lower()
    if ArmourChoice not in ArmourList:
        ArmourChoice = random.choice(ArmourList)
        if DumbLevel == 1:
            print("*no thoughts, head empty*")
            print("???: 'Again! Really, are you that stupid?! Ok, fine. Take Option", ArmourChoice.upper())
        else:
            print("You can't decide what piece of armour to choose.")
            print("???: 'Fine, I'll pick. Take Option", ArmourChoice.upper())
        DumbLevel += 1
    if ArmourChoice == "a":
        PlayerArmourLevel = 1
        print("You put on the ribbon.")
    elif ArmourChoice == "b":
        PlayerArmourLevel = 2
        print("You put on the bandana.")
    elif ArmourChoice == "c":
        PlayerArmourLevel = 0
        print("You apply the bandage.")
    print()
    print("You notice a monster candy in the corner of the room.")
    print("Do you want to pick it up?")
    ChooseItem = input().lower()
    if ChooseItem == "yes":
        print("You pick up the candy and put it in your back pocket.")
        MonsterCandy = 1
    else:
        print("You decide not to.")
        MonsterCandy = 0
    print()
    print("???: 'Great. Now you're ready.'")
    print("'Ready for what?' You wonder, but before you can say anything -")
    print("A Froggit bounces towards you.")
    print("It prepares for a fight!")

    while "According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyways. Because bees don't care what humans think is impossible.":
        if FroggitBurnTime >= 1:
            print("The froggit was burnt and lost 2 HP.")
            FroggitHealth -= 2
            FroggitBurnTime -= 1
            if FroggitHealth <= 0:
                FroggitDead = 1
                break
            if FroggitBurnTime < 1:
                print("The froggit stopped burning.")
        print()
        print("HP =", PlayerHealth)
        print()
        print("Use FIGHT, ACT, ITEM or MERCY")
        BattleCommand = input().lower()
        if BattleCommand == "fight":
            PlayerDamage = int(random.randint(PlayerMinDamage, PlayerMaxDamage))
            FroggitHealth -= PlayerDamage
            if PlayerDamage <= 0:
                print("Your weapon did no damage!")
            else:
                print("Froggit lost", PlayerDamage, "HP.")
            if BurnEnabled == 1 and FroggitBurnTime <= 0 and int(random.randint(1, 2)) == 1:
                FroggitHealth -= 2
                print("The red-hot pan began to burn Froggit. It lost 2 HP.")
                FroggitBurnTime = 1
            if FroggitHealth <= 0:
                FroggitDead = 1
                break
        elif BattleCommand == "act":
            print("What do you want to do? INSPECT, FLIRT or THREAT")
            ActCommand = input().lower()
            if ActCommand == "inspect":
                print("You closely inspect Froggit and learn some statistics.")
                print()
                print("Species = Frog")
                print("Height = 2'5")
                print("Gender = Ribbit")
                if FroggitCalmed == 1:
                    print("Relationship Status = A single pringle and ready to mingle. ;)")
                else:
                    print("Relationship Status = Happily married with 2 children.")
                print("HP =", FroggitHealth)
            elif ActCommand == "flirt":
                if FroggitAngered == 1:
                    print("Your flirt calmed Froggit, but it wasn't enough to woo it.")
                    FroggitAngered = 0
                elif FroggitCalmed == 1:
                    print("Wait, do you want this to turn into a dating simulator? No!")
                else:
                    print("Froggit blushes!")
                    print("Froggit doesn't want to fight you anymore.")
                    FroggitCalmed = 1
            elif ActCommand == "threat":
                if FroggitCalmed == 1:
                    print("Froggit lost its feelings for you, but it didn't get angry.")
                    FroggitCalmed = 0
                elif FroggitAngered == 0:
                    print("Froggit looks like it got angrier!")
                    print("Froggit will now deal more damage!")
                    FroggitAngered = 1
                else:
                    print("Froggit is too angry to listen to anymore of your insults.")
            else:
                print("No time to do anything, Froggit is ready to fight!")
        elif BattleCommand == "item":
            if MonsterCandy > 0:
                if MonsterCandy == 1:
                    print("You have one candy.")
                else:
                    print("You have", MonsterCandy, "candies. nuts :)")
                print("Do you want to eat a Monster Candy? (YES or NO)")
                ItemCommand = input().lower()
                if ItemCommand == "yes":
                    PlayerHealth += 10
                    if PlayerHealth > 20:
                        PlayerHealth = 20
                    MonsterCandy -= 1
                    print("You ate a candy and now have", PlayerHealth, "HP.")
                else:
                    print("You decide not to use a candy.")
            else:
                print("You have no items to use.")
        elif BattleCommand == "mercy":
            print("Do you want to SPARE Froggit or FLEE from the fight?")
            MercyCommand = input().lower()
            if MercyCommand == "spare":
                if FroggitCalmed == 1:
                    print("Froggit was happy that things didn't escalate further.")
                    FroggitSpared = 1
                    break
                else:
                    print("You'll need to woo it first. ;)")
            elif MercyCommand == "flee":
                print("You realise that, in fight simulators, there is nowhere to run to.")
            else:
                print("No time to run, Froggit is ready to fight!")
        else:
            print("While you were thinking, Froggit attacks!")
        if FroggitCalmed == 0:
            FroggitAttackPos = int(random.randint(1, 2))
            FroggitDamage = int(random.randint(2, 5))
            if FroggitAngered == 1:
                FroggitDamage *= 2
            print("Froggit gets ready to attack you. Will you dodge LEFT or RIGHT?")
            DodgeCommand = input().lower()
            if DodgeCommand == "left":
                PlayerDodgePos = 1
            elif DodgeCommand == "right":
                PlayerDodgePos = 2
            else:
                PlayerDodgePos = 3
                print("While you were choosing which way to go, Froggit attacked!")
            if FroggitAttackPos == PlayerDodgePos or PlayerDodgePos == 3:
                FroggitDamage -= PlayerArmourLevel
                PlayerHealth -= FroggitDamage
                print("You lost", FroggitDamage, "HP.")
                if PlayerHealth == 0 or PlayerHealth < 0:
                    PlayerDead = 1
                    break
            elif FroggitAttackPos != PlayerDodgePos:
                print("You dodged the attack.")
        else:
            print("Froggit looks like it's waiting for you to do something.")
    if PlayerDead == 1:
        print()
        print("HP = 0")
        print()
        print("GAME OVER")
        print()
        print("???: 'Next time, try choosing between offence and defence.'")
    elif FroggitDead == 1:
        print()
        print("YOU WIN?")
        print()
        if FroggitAngered == 1:
            print("???: 'At least you were defending yourself...'")
        elif FroggitCalmed == 1:
            print("???: 'I mean, come on. You were in a relationship! You disgust me.'")
        else:
            print("???: 'Why would you kill an innocent creature! What did it ever do to you?!'")
    elif FroggitSpared == 1:
        print()
        print("YOU WIN!")
        print()
        print("???: 'Well done for being a good person!'")
    print("Would you like to restart?")
    RestartCommand = input().lower()
    if RestartCommand == "yes":
        print()
        main()

main()
