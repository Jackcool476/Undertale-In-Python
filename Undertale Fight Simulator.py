def main():
    import random
    PlayerHealth = 20
    FroggitHealth = 20
    FroggitDead = 0
    FroggitSpared = 0
    PlayerDead = 0
    FroggitCalmed = 0
    FroggitAngered = 0
    FroggitBurnt = 0
    MonsterCandy = 1
    BurnEnabled = 0
    PlayerArmour = 1
    print("You wake up in a dark and damp room.")
    print("Suddenly the lights turn on!")
    print("An ominous voice bellows from above.")
    print("???: 'There are some things in front of you.")
    print("You see two piles, one with weapons and one with armour.")
    print("???: 'You must take one of each to prepare.")
    print("You wonder what for, but decide not to question it.")
    input("You walk over to the pile of weapons and decide which one to pick.")
    input("Option A: Stick - A normal stick lying next to the other weapons. It won't do much, but it's better than nothing.")
    # * Normal Mode
    input("Option B: Burnt Pan - Hot to the touch. Lifting it, you feel enough weight to knock someone out.")
    # ? Easy Mode
    input("Option C: Toy Knife - Made of foam. It'll do next to nothing, but it might scare someone.")
    # ! Hard Mode
    WeaponList = ["a", "b", "c"]
    print("Which weapon do you want? A, B or C?")
    WeaponChoice = input().lower()
    if WeaponChoice not in WeaponList:
        WeaponChoice = random.choice(WeaponList)
        print("You can't decide which weapon to choose.")
        print("You close your eyes and pick out a random one.")
    if WeaponChoice == "a":
        PlayerMinDamage = 2
        PlayerMaxDamage = 5
        print("You choose the stick.")
        input("You wield the stick and feel like a kid. You realise that you don't even know how old you are.")
    elif WeaponChoice == "b":
        PlayerMinDamage = 5
        PlayerMaxDamage = 7
        BurnEnabled = 1
        print("You choose the pan.")
        input("You wield the pan and flip it in your hand. You might have been a chef before you came to this place.")
    elif WeaponChoice == "c":
        PlayerMinDamage = 0
        PlayerMaxDamage = 1
        print("You choose the toy knife.")
        input("You wield the toy and throw it into the air. You catch it easily and think about why you chose it. You can't find a good reason.")
    print("A Froggit bounces towards you.")
    print("It prepares for a fight!")

    while "According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyways. Because bees don't care what humans think is impossible.":
        if FroggitBurnt >= 1:
            print("The froggit was burnt and lost 2 HP.")
            FroggitHealth -= 2
            FroggitBurnt -= 1
            if FroggitHealth <= 0:
                FroggitDead = 1
                break
            if FroggitBurnt < 1:
                print("The froggit stopped burning.")
        print()
        print("HP =", PlayerHealth)
        print()
        print("Use FIGHT, ACT, ITEM or MERCY")
        BattleCommand = input().lower()
        if BattleCommand == "fight":
            PlayerDamage = int(random.randint(
                PlayerMinDamage, PlayerMaxDamage))
            FroggitHealth -= PlayerDamage
            if PlayerDamage <= 0:
                print("Your weapon didn't do any damage at all!")
            else:
                print("Froggit lost", PlayerDamage, "HP.")
            if BurnEnabled == 1 and FroggitBurnt <= 0:
                BurnChance = int(random.randint(1, 2))
                if BurnChance == 1:
                    FroggitHealth -= 2
                    print("The red-hot pan began to burn Froggit. It lost 2 HP.")
                    FroggitBurnt = 1
            if FroggitHealth <= 0:
                FroggitDead = 1
                break
        elif BattleCommand == "act":
            print("What do you want to do? INSPECT, FLIRT or THREAT?")
            ActCommand = input().lower()
            if ActCommand == "inspect":
                print("You closely inspect Froggit and learn some statistics.")
                print()
                print("Species = Frog")
                print("Height = 2 foot 5")
                print("Gender = Ribbit")
                if FroggitCalmed == 1:
                    print(
                        "Relationship Status = A single pringle and ready to mingle... ;)")
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
                    print("You have", MonsterCandy, "candies. (nuts :) )")
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
                print(
                    "You realise that, in fight simulators, there is nowhere to run to.")
            else:
                print("No time to run, Froggit is ready to fight!")
        else:
            print("While you were thinking, Froggit attacks out of nowhere!")
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
                FroggitDamage /= PlayerArmour
                FroggitDamage = round(FroggitDamage)
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
        print("Next time, try choosing between offence and defence and don't mess around.")
    elif FroggitDead == 1:
        print()
        print("YOU WIN?")
        print()
        if FroggitAngered == 1:
            print("At least you were defending yourself...")
        elif FroggitCalmed == 1:
            print("I mean come on. You were in a relationship! You disgust me.")
        else:
            print("Why would you kill an innocent creature! What did it ever do to you?!")
    elif FroggitSpared == 1:
        print()
        print("YOU WIN!")
        print()
        print("Well done for being a good person!")
    print("Would you like to restart?")
    Restart = input().lower()
    if Restart == "yes":
        print()
        main()


main()
