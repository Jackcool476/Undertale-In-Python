import random
FroggitAngry = 0
FroggitDead = 0
FroggitSpared = 0
FroggitReadySpared = 0
PlayerDead = 0
HaveMonsterCandy = 1
PlayerHealth = 20
FroggitHealth = 20
print("A lone Froggit bounces towards you.")
print("They prepare for a fight!")
# ? Make this not use variables since I don't think it needs them? Testing required
while FroggitDead == 0 or FroggitSpared == 0 or PlayerDead == 0:
    print("")
    print("HP =", PlayerHealth)
    print("")
    print("Use FIGHT, ACT, ITEM or MERCY")
    BattleCommand = input()
    if BattleCommand == "FIGHT" or BattleCommand == "fight":
        PlayerDamage = int(random.randint(2, 5))
        FroggitHealth = FroggitHealth - PlayerDamage
        if FroggitHealth == 0 or FroggitHealth < 0:
            FroggitDead = 1
            break
        else:
            print("Froggit took", PlayerDamage, "damage.")
    elif BattleCommand == "ACT" or BattleCommand == "act":
        print("What do you want to do? INSPECT, FLIRT or THREAT?")
        PlayerAct = input()
        if PlayerAct == "INSPECT" or PlayerAct == "inspect":
            print("You closely examine Froggit and learn some statistics.")
            print("")
            print("Species = Frog")
            print("Height = 2 foot 5")
            print("Gender = Ribbit")
            if FroggitReadySpared == "1":
                print("Relationship Status = A single pringle and ready to mingle... ;)")
            else:
                print("Relationship Status = Happily married with 2 children.")
            print("Health =", FroggitHealth)
        elif PlayerAct == "FLIRT" or PlayerAct == "flirt":
            if FroggitAngry == 1:
                print("Your flirt calmed Froggit, but it wasn't enough to woo it.")
                FroggitAngry = 0
            elif FroggitReadySpared == 1:
                print("Wait, do you want this to turn into a dating simulator? No!")
            else:
                print("Froggit blushes!")
                print("Froggit doesn't want to fight you anymore.")
                FroggitReadySpared = 1
        elif PlayerAct == "THREAT" or PlayerAct == "threat":
            if FroggitReadySpared == 1:
                print("Froggit lost its feelings for you, but didn't get angry.")
                FroggitReadySpared = 0
            elif FroggitAngry == 0:
                print("Froggit looks like it got angrier!")
                print("Froggit will now deal more damage!")
                FroggitAngry = 1
            else:
                print("Froggit is too angry to listen to anymore of your insults.")
        else:
            print("No time to do anything, Froggit is ready to fight!")
    elif BattleCommand == "ITEM" or BattleCommand == "item":
        if HaveMonsterCandy == 1:
            print("Do you want to eat your Monster Candy? (YES or NO)")
            UseMonsterCandy = input()
            if UseMonsterCandy == "YES" or "yes":
                PlayerHealth = PlayerHealth + 10
                if PlayerHealth > 20:
                    PlayerHealth = 20
                HaveMonsterCandy = 0
                print("You ate the candy and now have", PlayerHealth, "health.")
            else:
                #! Fix this at some point.
                print("You decide not to use your candy.")
        else:
            print("You have no items to use.")
    elif BattleCommand == "MERCY" or BattleCommand == "mercy":
        print("Do you want to SPARE Froggit or FLEE from the fight?")
        MercyCommand = input()
        if MercyCommand == "SPARE" or MercyCommand == "spare":
            if FroggitReadySpared == 1:
                print("Froggit was happy that things didn't escalate further.")
                FroggitSpared = 1
                break
            else:
                print("You'll need to woo it first. ;)")
        elif MercyCommand == "FLEE" or MercyCommand == "flee":
            print("You realise that, in fight simulators, there is nowhere to run to.")
        else:
            print("No time to run, Froggit is ready to fight!")
    else:
        print("While you were thinking, Froggit attacks out of nowhere!")
    if FroggitReadySpared == 0:
        FroggitAttacks = int(random.randint(1, 2))
        FroggitHits = int(random.randint(2, 5))
        if FroggitAngry == 1:
            FroggitHits *= 2
        print("Froggit gets ready to attack you. Will you dodge LEFT or RIGHT?")
        PlayerDodge = input()
        if PlayerDodge == "LEFT" or PlayerDodge == "left":
            PlayerDodged = 1
        elif PlayerDodge == "RIGHT" or PlayerDodge == "right":
            PlayerDodged = 2
        else:
            PlayerDodged = 3
            print("While you were choosing which way to go, Froggit attacked!")
        if FroggitAttacks == 1 and PlayerDodged == 1 or FroggitAttacks == 2 and PlayerDodged == 2 or PlayerDodged == 3:
            print("You took", FroggitHits, "damage.")
            PlayerHealth = PlayerHealth - FroggitHits
            if PlayerHealth == 0 or PlayerHealth < 0:
                PlayerDead = 1
                break
        elif FroggitAttacks == 1 and PlayerDodged == 2 or FroggitAttacks == 2 and PlayerDodged == 1:
            print("You dodged the attack.")
    else:
        print("Froggit looks like its waiting for you to do something.")
if PlayerDead == 1:
    print("")
    print("HP = 0")
    print("")
    print("GAME OVER")
    print("")
    print("Next time, try choosing between offence and defence and don't mess around.")
elif FroggitDead == 1:
    print("")
    print("YOU WIN?")
    print("")
    if FroggitAngry == 1:
        print("At least you were defending yourself...")
    elif FroggitReadySpared == 1:
        print("I mean come on. You were in a relationship! You disgust me.")
    else:
        print("Why did you kill such an innocent creature! What did it do ever to you?!")
elif FroggitSpared == 1:
    print("")
    print("YOU WIN!")
    print("")
    print("Well done for being a good person!")
