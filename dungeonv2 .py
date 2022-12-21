#import sys
#import cv2
import random
import time

#sets the floor (enemies to fight) to 1
floor = 1

#list of every available enemy and their stats
enemyOption = {
    1: {
        "enemyName": "Rock Golem",
        "enemyHealth": "50"
        },
    2: {
        "enemyName": "Big Snake",
        "enemyHealth": "25"
        },
    3: {
        "enemyName": "Weird Cow",
        "enemyHealth": "20"
        },
    4: {
        "enemyName": "Ghost",
        "enemyHealth": "10"
        },
    5: {
        "enemyName": "Minotaur",
        "enemyHealth": "30"
        },
    6: {
        "enemyName": "Fungus Creature",
        "enemyHealth": "15"
        },
    7: {
        "enemyName": "Old Machine",
        "enemyHealth": "40"
        },
    8: {
        "enemyName": "Slime",
        "enemyHealth": "25"
        },
    9: {
        "enemyName": "Living Wall",
        "enemyHealth": "45"
        },
    10: {
        "enemyName": "Large Dungeon Ant",
        "enemyHealth": "20"
        },
    11: {
        "enemyName": "Giant Hornet",
        "enemyHealth": "22"
        },
    12: {
        "enemyName": "Armed Skeleton",
        "enemyHealth": "25"
        },
    13: {
        "enemyName": "Dungeon Zombie",
        "enemyHealth": "15"
        },
    14: {
        "enemyName": "Crazed Knight",
        "enemyHealth": "35"
        },
    15: {
        "enemyName": "Anomalous Shark",
        "enemyHealth": "30"
        }
}

x = 1
#x = 1 is player 1, x = 2 is player 2

#default player health
playerhp1 = 100
playerhp2 = 100

#defines the guard status of each player
p1guardStatus = 0
p2guardStatus = 0

#resets the guard after the enemy attacks each turn, this resets the number
guardDefault = 0

#asks for name input
print("Welcome to the dungeon crawler game, what are your names?: ")
p1name = input("Player one is called... ")
p2name = input("Player two is called... ")

print("Ah, welcome challengers", p1name ,"and", p2name + ".")


#gives the player the option to see the tutorial, "y" = yes, any other input is a no
def tutorialreminder():

    print("Would you like a brief introduction into this game?")
    tutorialreminder = input("'y' for tutorial, 'n' or any other input to skip: ")

    if tutorialreminder == "y" or tutorialreminder == "Y":
        print("You will both be thrown into a dungeon with 15 floors of enemies that you must triamph over.")
        time.sleep(2) #these delays are so that both players can read before being thrown right into the game
        print("You have the options to fight, defend, use your inventory, or to flee and end the game like a coward.")
        time.sleep(2)
        print("Every enemy except for the last is random, i wish you luck in your journey.")
    else:
        print("Very well, and goodluck with your quest.")

tutorialreminder()

time.sleep(2)
print("Loading...")
time.sleep(3) #another delay so both players can be prepared

def combat():
    global floor
    global enemyOption
    global playerhp1
    global playerhp2
    global p1name
    global p2name
    global p1guardStatus
    global p2guardStatus
    global guardDefault

    #the imread command sets the definition and path of these images, along with thier colour display settings
    while floor <= 15:
        randomencounter = random.randint(1, 15)
        if playerhp1 <= 0 and playerhp2 <= 0:
            fighting = False
            break
        else:
            print("")
            #randomencounter determines the enemy you fight against and the picture that will be displayed
            #picks a random choice from the nested dictionary and uses it for combat
            for x in enemyOption:
                if x == randomencounter:
                    enemyName = enemyOption[randomencounter]["enemyName"]
                    enemyHealth = enemyOption[randomencounter]["enemyHealth"]
                    enemyHealth = int(enemyHealth)
                    print("The", enemyName, "blocks your path")
                    print("with", enemyHealth, "health!")
                    fighting = True
                    
        #if this player gets to 0 or lower health, they will lose their ability to use their turn, otherwise it
        #continues as normal
        while fighting:                
            player1activity = True
            if playerhp1 <= 0:
                player1activity = False
            else:
                while player1activity:
                    #prints the available options
                    print(p1name + "'s turn!")
                    print("[ATTACK (1)] [DEFEND (2)] [HEAL (3)] [FLEE (4)]")
                    p1option = input()
                    if p1option == "1":
                        #randomises the damage the player deals
                        p1damage = random.randint(1, 15)
                        enemyHealth = int(enemyHealth) - int(p1damage)
                        time.sleep(1)
                        print("The", enemyName, "has taken", p1damage, "damage! They have", enemyHealth, "health remaining!")
                        #player1activity = False ends the turn of the player
                        player1activity = False
                        #if the enemy dies after a player's turn the floor ends early to prevent cheap hits after
                        #your opponent is downed
                        if enemyHealth <= 0:
                            floor = floor + 1
                            print("You have bested this floor's keeper, now onto floor number", floor)
                            time.sleep(1)
                            p1guardStatus = guardDefault
                            p2guardStatus = guardDefault
                            fighting = False
                            break
                        else:
                            print("")
                    #lets you have the option to guard, which has a 1/2 chance to block all damage
                    elif p1option == "2":
                        print(p1name, "readies their guard!")
                        p1guardStatus = p1guardStatus + 1
                        time.sleep(1)
                        player1activity = False
                    #heals the player from a number between 0-20
                    elif p1option == "3":
                        healPotionValue = random.randint(0, 20)
                        if healPotionValue > 0:
                            playerhp1 = playerhp1 + healPotionValue
                            print(p1name, "swigs a healing potion...")
                            time.sleep(1) #small delays are for dramatic effect
                            print(p1name, "has regained", healPotionValue, "health.")
                            time.sleep(1)
                            print(p1name, "is now at", playerhp1, "health.")
                            time.sleep(1)
                            player1activity = False
                        elif healPotionValue < 0:
                            print(p1name, "swigs a healing potion...")
                            time.sleep(1)
                            print(p1name, "has regained", healPotionValue, "health.")
                            time.sleep(1)
                            print("Huh... Someone must of failed their brewing classes...")
                            time.sleep(1)
                            player1activity = False
                    #this option lets you leave and end the game early
                    elif p1option == "4":
                        print(p1name, "entices their questing buddy", p2name, "to flee the tower...")
                        time.sleep(2)
                        print("!YOU HAVE FLED THE TOWER LIKE A WIMP!")
                        print("=============[GAME OVER]=============")
                        time.sleep(5)
                        #ends the loop and subsequently ends the game
                        break
                    else:
                        #punishes the player for not using an option between 1-4 or for using a non-integer
                        print("Congrats", p1name, "you wasted your turn!")
                        time.sleep(1)
                        player1activity = False


            if enemyHealth <= 0:
                fighting = False
                break
            player2activity = True
            
            if playerhp2 <= 0:
                player2activity = False
            else:
                while player2activity:
                    print(p2name + "'s turn!")
                    print("[ATTACK (1)] [DEFEND (2)] [HEAL (3)] [FLEE (4)]")
                    p2option = input()
                    if p2option == "1":
                        p2damage = random.randint(1, 15)
                        enemyHealth = int(enemyHealth) - int(p2damage)
                        time.sleep(1)
                        print("The", enemyName, "has taken", p2damage, "damage! They have", enemyHealth, "health remaining!")
                        player2activity = False
                        if enemyHealth <= 0:
                            cv2.destroyAllWindows()
                            floor = floor + 1
                            print("You have bested this floor's keeper, now onto floor number", floor)
                            time.sleep(1)
                            p1guardStatus = guardDefault
                            p2guardStatus = guardDefault
                            fighting = False
                            break
                        else:
                            print("")
                    elif p2option == "2":
                        print(p2name, "readies their guard!")
                        p2guardStatus = p2guardStatus + 1
                        time.sleep(1)
                        player2activity = False
                    elif p2option == "3":
                        healPotionValue = random.randint(0, 20)
                        if healPotionValue > 0:
                            playerhp2 = playerhp2 + healPotionValue
                            print(p2name, "swigs a healing potion...")
                            time.sleep(1)
                            print(p2name, "has regained", healPotionValue, "health.")
                            time.sleep(1)
                            print(p2name, "is now at", playerhp2, "health.")
                            time.sleep(1)
                            player2activity = False
                        elif healPotionValue < 0:
                            print(p2name, "swigs a healing potion...")
                            time.sleep(1)
                            print(p2name, "has regained", healPotionValue, "health.")
                            time.sleep(1)
                            print("Huh... Someone must of failed their brewing classes...")
                            time.sleep(1)
                            player2activity = False
                    elif p2option == "4":
                        print(p2name, "entices their questing buddy", p2name, "to flee the tower...")
                        time.sleep(2)
                        print("!YOU HAVE FLED THE TOWER LIKE A WIMP!")
                        print("=============[GAME OVER]=============")
                        time.sleep(5)
                        break
                    else:
                        print("Congrats", p2name, "you wasted your turn!")
                        time.sleep(1)
                        player1activity = False
                        player2activity = False
                        
            if enemyHealth <= 0:
                fighting = False
                break

            if playerhp1 <= 0 and playerhp2 <= 0:
                fighting = False
                break
            else:

                #randomly decides which player is targeted for an attack
                #1 = player 1, 2 = player 2
                playerTarget = random.randint(1, 2)
                
                if playerTarget == 1:
                    #checks if the player used the second option
                    if p1guardStatus == 1:
                        #has a 1/2 to determine if a block is successful
                        #0 = fail, 1 = success
                        p1guardSuccess = random.randint(0, 1)
                        if p1guardSuccess == 0:
                            #determines how much damage the enemy will inflict
                            enemyDamage = random.randint(0, 20) 
                            print(p1name, "tried to brace themselves but failed.")
                            playerhp1 = int(playerhp1) - int(enemyDamage)
                            print(p1name, "has recieved", enemyDamage, "damage from", enemyName + "!")
                            print(p1name, "has", playerhp1, "remaining.")
                            print(p2name, "has", playerhp2, "remaining.")
                            #resets the guard status to prevent code breakages or infinite guarding
                            p1guardStatus = guardDefault
                            p2guardStatus = guardDefault
                            time.sleep(1)

                        elif p1guardSuccess == 1:
                            print(p1name, "has successfully blocked the oncoming attack from", enemyName)
                            p1guardStatus = guardDefault
                            p2guardStatus = guardDefault
                            time.sleep(1)
                    elif p1guardStatus == 0:
                        enemyDamage = random.randint(0, 20) 
                        playerhp1 = int(playerhp1) - int(enemyDamage)
                        print(p1name, "has recieved", enemyDamage, "damage from", enemyName + "!")
                        print(p1name, "has", playerhp1, "remaining.")
                        print(p2name, "has", playerhp2, "remaining.")
                        p1guardStatus = guardDefault
                        p2guardStatus = guardDefault
                        time.sleep(1)
                        
                elif playerTarget == 2:
                    if p2guardStatus == 1:
                        p2guardSuccess = random.randint(0, 1)
                        if p2guardSuccess == 0:
                            enemyDamage = random.randint(0, 20) 
                            print(p2name, "tried to brace themselves but failed.")
                            playerhp2 = int(playerhp2) - int(enemyDamage)
                            print(p2name, "has recieved", enemyDamage, "damage from", enemyName + "!")
                            print(p1name, "has", playerhp1, "remaining.")
                            print(p2name, "has", playerhp2, "remaining.")
                            p1guardStatus = guardDefault
                            p2guardStatus = guardDefault
                            time.sleep(1)

                        elif p2guardSuccess == 1:
                                print(p2name, "has successfully blocked the oncoming attack from", enemyName)
                                p1guardStatus = guardDefault
                                p2guardStatus = guardDefault
                                time.sleep(1)
                    elif p2guardStatus == 0:
                        enemyDamage = random.randint(0, 20) 
                        playerhp2 = int(playerhp2) - int(enemyDamage)
                        print(p2name, "has recieved", enemyDamage, "damage from", enemyName + "!")
                        print(p1name, "has", playerhp1, "remaining.")
                        print(p2name, "has", playerhp2, "remaining.")
                        p1guardStatus = guardDefault
                        p2guardStatus = guardDefault
                        time.sleep(1)
            
combat()

#game over screen for if both players have their health drop to 0 or below
if playerhp1 <= 0 and playerhp2 <= 0:
    print("Both players has fallen in combat.")
    print("===========[GAME OVER]===========")
else:
    print("")

def ending():
    global p1name
    global p2name
    global playerhp1
    global playerhp2

    #ending for if both players won while alive
    if playerhp1 > 0 and playerhp2 > 0:
        print("Congratulations to", p1name, "and", p2name, "on conquering all 15 floors!")
        time.sleep(3)
        print("===[YOU BOTH WIN]===")
        time.sleep(5)
    #ending for if player1 survives but player2 died
    elif playerhp1 > 0 and playerhp2 < 0:
        print(p1name, "has emerged victorious through all 15 floors, unfortunately their buddy", p2name, "failed during combat.")
        time.sleep(3)
        print("Good job! Now try and emerge with both of you alive!")
        time.sleep(5)
    #ending for if player2 survived but player1 died
    elif playerhp1 < 0 and playerhp2 > 0:
        print(p2name, "has emerged victorious through all 15 floors, unfortunately their buddy", p1name, "failed during combat.")
        time.sleep(3)
        print("Good job! Now try and emerge with both of you alive!")
        time.sleep(5)      

ending()

#randomencounter determines the enemy you fight against and the picture that will be displayed
#the equivalent number is equal to the image that is opened and displayed
#
#                    if randomencounter == 1:
#                        golem = cv2.imread("images/golem.png", cv2.IMREAD_ANYCOLOR)
#                        cv2.imshow("Rock Golem", golem)
#                        cv2.waitKey(0)
#                    elif randomencounter == 2:
#                        snake = cv2.imread("images/bigsnake.png", cv2.IMREAD_ANYCOLOR)
#                        cv2.imshow("Big Snake", snake)
#                        cv2.waitKey(0)
#                        cv2.destroyAllWindows()
#                    elif randomencounter == 3:
#                        cow = cv2.imread("images/weirdcow.png", cv2.IMREAD_ANYCOLOR)
#                        cv2.imshow("Weird Cow", cow)
#                        cv2.waitKey(0)
#                        cv2.destroyAllWindows()
#                    elif randomencounter == 4:
#                        ghost = cv2.imread("images/ghost.png", cv2.IMREAD_ANYCOLOR)
#                        cv2.imshow("Ghost", ghost)
#                        cv2.waitKey(0)
#                        cv2.destroyAllWindows()
#                    elif randomencounter == 5:
#                        minotaur = cv2.imread("images/minotaur.png", cv2.IMREAD_ANYCOLOR)
#                        cv2.imshow("Minotaur", minotaur)
#                        cv2.waitKey(0)
#                        cv2.destroyAllWindows()
#                    elif randomencounter == 6:
#                        fungus = cv2.imread("images/fungus.png", cv2.IMREAD_ANYCOLOR)
#                        cv2.imshow("Fungus Creature", fungus)
#                        cv2.waitKey(0)
#                        cv2.destroyAllWindows()
#                    elif randomencounter == 7:
#                        machine = cv2.imread("images/oldmachine.png", cv2.IMREAD_ANYCOLOR)
#                        cv2.imshow("Old Machine", machine)
#                        cv2.waitKey(0)
#                        cv2.destroyAllWindows()
#                    elif randomencounter == 8:
#                        slime = cv2.imread("images/slime.png", cv2.IMREAD_ANYCOLOR)
#                        cv2.imshow("Slime", slime)
#                        cv2.waitKey(0)
#                        cv2.destroyAllWindows()
#                    elif randomencounter == 9:
#                        livingwall = cv2.imread("images/livingwall.png", cv2.IMREAD_ANYCOLOR)
#                        cv2.imshow("Living Wall", livingwall)
#                        cv2.waitKey(0)
#                        cv2.destroyAllWindows()
#                    elif randomencounter == 10:
#                        ant = cv2.imread("images/ant.png", cv2.IMREAD_ANYCOLOR)
#                        cv2.imshow("Large Dungeon Ant", ant)
#                        cv2.waitKey(0)
#                        cv2.destroyAllWindows()
#                    elif randomencounter == 11:
#                        hornet = cv2.imread("images/22.png", cv2.IMREAD_ANYCOLOR)
#                        cv2.imshow("Giant Hornet", hornet)
#                        cv2.waitKey(0)
#                        cv2.destroyAllWindows()
#                    elif randomencounter == 12:
#                        skeleton = cv2.imread("images/skeleton.png", cv2.IMREAD_ANYCOLOR)
#                        cv2.imshow("Armed Skeleton", skeleton)
#                        cv2.waitKey(0)
#                    elif randomencounter == 13:
#                        zombie = cv2.imread("images/zombie.png", cv2.IMREAD_ANYCOLOR)
#                        cv2.imshow("Dungeon Zombie", zombie)
#                        cv2.waitKey(0)
#                        cv2.destroyAllWindows()
#                    elif randomencounter == 14:
#                        knight = cv2.imread("images/crazedknight.png", cv2.IMREAD_ANYCOLOR)
#                        cv2.imshow("Crazed Knight", knight)
#                        cv2.waitKey(0)
#                        cv2.destroyAllWindows()
#                    elif randomencounter == 15:
#                        shark = cv2.imread("images/shark.png", cv2.IMREAD_ANYCOLOR)
#                        cv2.imshow("Anomalous Shark", shark)
#                        cv2.waitKey(0)
#                        cv2.destroyAllWindows()
#
#broken code that i tried to make for images
