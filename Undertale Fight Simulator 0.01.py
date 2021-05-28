import random
BattleCommand = ""
FroggitDead = "No"
FroggitSpared = "No"
FroggitReadySpared = "No"
FroggitHit = 0
FroggitDamage1 = 1
FroggitDamage2 = 5
PlayerDead = "No"
PlayerDamage = ""
PlayerAct = ""
PLayerDodge = ""
HaveMonsterCandy = "Yes"
UseMonsterCandy = ""
MercyCommand = ""
PlayerHealth = 20
FroggitHealth = 20
print("Froggit bounces towards you.")
print("They prepare for a fight!")
while FroggitDead == "No" or FroggitSpared == "No" or PlayerDead == "No":
    print("HP =", PlayerHealth)
    BattleCommand = input("Use FIGHT, ACT, ITEM or MERCY")
    if BattleCommand == "FIGHT":
        PlayerDamage = int(random.randint(FroggitDamage1, FroggitDamage2))
        FroggitHealth = FroggitHealth - PlayerDamage
        if FroggitHealth == 0 or FroggitHealth < 0:
            FroggitDead = "Yes"
        else:
            print("Froggit took", PlayerDamage, "damage.")
    if BattleCommand == "ACT":
        PlayerAct = input("What will you do? FLIRT or THREAT?")
        if PlayerAct == "FLIRT":
            print("Froggit blushes!")
            print("Froggit doesn't want to fight you anymore.")
            FroggitReadySpared = "Yes"
        if PlayerAct == "THREAT":
            print("Froggit looks mad!")
            print("Froggit might be angrier now!")
            FroggitDamage1 = 2
            FroggitDamage2 = 10
    if BattleCommand == "ITEM":
        if HaveMonsterCandy == "Yes":
            UseMonsterCandy = input("Use a Monster Candy? (YES or NO)")
            if UseMonsterCandy == "YES":
                PlayerHealth = PlayerHealth + 10
                if PlayerHealth > 20:
                    PlayerHealth = 20
                HaveMonsterCandy = "No"
                print("You now have", PlayerHealth, "health.")
        elif HaveMonsterCandy == "No":
            print("You have no items to use.")
    if BattleCommand == "MERCY":
        MercyCommand = input(
            "Do you want to SPARE the enemy or FLEE from the fight?")
        if MercyCommand == "SPARE":
            if FroggitReadySpared == "Yes":
                FroggitSpared = "Yes"
            elif FroggitReadySpared == "No":
                print("Froggit won't be spared yet.")
        elif MercyCommand == "FLEE":
            print("You realise that, in fight sims, there is no overworld.")
    if FroggitReadySpared == "No":
        FroggitHit = int(random.randint(1, 2))
        PlayerDodge = input(
            "Froggit gets ready to attack you. Will you dodge LEFT or RIGHT?")
        if FroggitHit == 1 and PlayerDodge == "LEFT" or FroggitHit == 2 and PlayerDodge == "RIGHT":
            print("You got hit.")
            PlayerHealth = PlayerHealth - 5
            if PlayerHealth == 0 or PlayerHealth < 0:
                PlayerDead = "Yes"
        elif FroggitHit == 1 and PlayerDodge == "RIGHT" or FroggitHit == 2 and PlayerDodge == "LEFT":
            print("You dodge the attack.")
if PlayerDead == "Yes":
    print("GAME OVER")
elif FroggitDead == "Yes":
    print("You're a genocidal maniac!")
elif FroggitSpared == "Yes":
    print("Well done for being good!")
# It can't get to the above six lines for some reason? Plz help me fix it.
