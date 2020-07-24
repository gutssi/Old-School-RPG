
from colorama import Fore, Back, Style
import sys, time, random
from ownlib import clearTop
import art
import GUI
import deadScreen



health = 200.0
maxHealth = 200
minHealth = 1
healthDashes = 20

mana = 200.0
maxMana = 200
minMana = 0
manaDashes = 20

answer = " "
answerTwo = 0
answerBattle = 0


# player and npc stats

playerAtk = 10
plaeryAtkMax = 200
playerAtkMin = 1

playerDef = 10
playerMaxDef = 200
playerMinDef = 10

npcHealth = 200
npcMaxHealth = 200
npcMinHealth = 1

npcAtk = 10
npcDef = 10


 







"""enemyPresent = False"""
lootPresent = False
trapBox = 0

remainingDisplayMana = 0

randomItemOne = random.choice([" a small shank", " a toxic syringe", " few pistol bullets", " a paper clip"])
randomItemTwo = random.choice([" 5 skull tokens", " picture of loved ones", " 2 medkits", " a gun", " nothing else"])

caseNumber = random.randint(3333, 9999)

playerStory = "Hello subject " + str(caseNumber) + ",\n you woke up just in time.\n If you check your pockets, you will find: \n" + randomItemOne + " and" + randomItemTwo + "." "\n Try to survive"


##################################################################

# Map static
a = "             | | | |\n"
b = "             _______\n"

bf0 = "          "  +  "0F"  +  " _______ "
bf1 = "          "  +  "1F"  +  " _______ "
bf2 = "          "  +  "2F"  +  " _______ "

# Player
c = "             |\033[1;32;40mP\033[1;37;40m| | |\n"
d = "             | |\033[1;32;40mP\033[1;37;40m| |\n"
e = "             | | |\033[1;32;40mP\033[1;37;40m|\n"

# Encounter
x1 = "             |" + Back.RED + "E" + Style.RESET_ALL + "| | |\n"
x2 = "             | |" + Back.RED + "E" + Style.RESET_ALL + "| |\n"
x3 = "             | | |" + Back.RED + "E" + Style.RESET_ALL + "|\n"

z1 = "             |" + Fore.YELLOW + "L" + Style.RESET_ALL + "| | |\n"
z2 = "             | |" + Fore.YELLOW + "L" + Style.RESET_ALL + "| |\n"
z3 = "             | | |" + Fore.YELLOW + "L" + Style.RESET_ALL + "|\n"

y1 = random.choice([c, c, c, c, c, c, c, c, c, z1, x1])
y2 = random.choice([d, d, d, d, d, d, d, d, d, z2, x2])
y3 = random.choice([e, e, e, e, e, e, e, e, e, z3, x3])


# Map Display
emptyMap = b + a + b + a + b + a + bf0

roomOne = b + y1 + b + a + b + a + bf2
roomTwo = b + y2 + b + a + b + a + bf2
roomThree = b + y3 + b + a + b + a + bf2

roomFour = b + a + b + y1 + b + a + bf1
roomFive = b + a + b + y2 + b + a + bf1
roomSix = b + a + b + y3 + b + a + bf1

roomSeven = b + a + b + a + b + y1 + bf0
roomEight = b + a + b + a + b + y2 + bf0
roomNine = b + a + b + a + b + y3 + bf0



deadArt = """


                                                                _
                                                              _( (~\\
       _ _                        /                          ( \\> > \\
   -/~/ / ~\\                     :;                \\       _  > /(~\\/
  || | | /\\ ;\\                   |l      _____     |;     ( \\/    > >
  _\\)\\)\\)/ ;;;                  `8o __-~     ~\\   d|      \\      //
 ///(())(__/~;;\\                  "88p;.  -. _\\_;.oP        (_._/ /
(((__   __ \\   \\                 `>,% (\\  (\\./)8"         ;:'  i
)))--`.'-- (( ;,8 \\               ,;%%%:  ./V^^^V'          ;.   ;.
((\\  |   /)) .,88  `: ..,,;;;;,-::::::'_::\\   ||\\         ;[8:   ;
 )|  ~-~  |(|(888; ..``'::::8888oooooo.  :\\`^^^/,,~--._    |88::  |
 |\\ -===- /|  \\8;; ``:.      oo.8888888888:`((( o.ooo8888Oo;:;:'  |
 |_~-___-~_|   `-\\.   `        `o`88888888b` )) 888b88888P""'     ;
 ; ~~~~;~~         "`--_`.       b`888888888;(.,"888b888"  ..::;-'
   ;      ;              ~"-....  b`8888888:::::.`8888. .:;;;''
      ;    ;                 `:::. `:::OOO:::::::.`OO' ;;;''
 :       ;                     `.      "``::::::''    .'
    ;                           `.   \\_              /
  ;       ;                       +:   ~~--  `:'  -';
                                   `:         : .::/  
      ;                            ;;+_  :::. :..;;;  
                                   ;;;;;;,;;;;;;;;,;

"""
cyclopArt = """


           _......._
       .-'.'.'.'.'.'.`-.
     .'.'.'.'.'.'.'.'.'.`.
    /.'.'               '.\\
    |.'    _.--...--._     |
    \\    `._.-.....-._.'   /
    |     _..- .-. -.._   |
 .-.'    `.   ((@))  .'   '.-.
( ^ \\      `--.   .-'     / ^ )
 \\  /         .   .       \\  /
 /          .'     '.  .-    \\
( _.\\    \\ (_`-._.-'_)    /._\\)
 `-' \\   ' .--.          / `-'
     |  / /|_| `-._.'\\   |
     |   |       |_| |   /-.._
 _..-\\   `.--.______.'  |
      \\       .....     |
       `.  .'      `.  /
         \\           .'
          `-..___..-`


"""

##################################################################

playerInventory = 0

if randomItemOne == " a small shank":
    playerInventory = "shank"
if randomItemOne == " a toxic syringe":
    playerInventory = "syringe"
elif randomItemOne == " few pistol bullets":
    playerInventory = " bullets"
elif randomItemOne == " a paper clip":
    playerInventory = " paper clip"

if randomItemTwo == " 5 skull tokens":
    playerInventory += " 5 tokens"
elif randomItemTwo == " picture of loved ones":
    playerInventory += " picture"
elif randomItemTwo == " 2 medkits":
    playerInventory += " 2xmedkit"
elif randomItemTwo == " a gun":
    playerInventory += " gun"
elif randomItemTwo == " mothing else":
    playerInventory += " bad luck omen"

currentFloor = 0

playerWarning = " "

playerBox = 7

gameOver = False

futurePosition = roomSeven
previousPosition = roomSeven


def gameReset():
    health = 200.0
    playerInventory = " empty"
    playerBox = 7
    futurePosition = roomFive
    previousPosition = roomFive
    gameOver = False

def printSlow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def printFast(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0001)


def easterEgg():
    printSlow(Back.RED + chr(27) + "[2J")
    printSlow("Konami code\n")
    printSlow(Back.RED + chr(27) + "[2J")
    updateFrame()

def battleScreen():
	global playerStory, healthDisplay, remainingDisplay, manaDisplay, remainingDisplayMana, playerInventory, playerWarning
	global remainingDisplay, remainingDisplayMana, deadArt

	dashConvert = int(maxHealth/healthDashes)
	dashConvertMana = int(maxMana/manaDashes)
	currentDashes = int(health/dashConvert)
	currentDashesMana = int(mana/dashConvertMana)
	remainingHealth = healthDashes - currentDashes
	remainingMana = manaDashes - currentDashesMana
	healthDisplay = '\033[1;31;40m+' * currentDashes
	manaDisplay = Fore.BLUE + "=" * currentDashesMana
	remainingDisplay = ' ' * remainingHealth

	print(Back.RED + chr(27) + "[2J")
	print(Style.RESET_ALL + " " + playerStory + "\n")
	print(Back.RED + "              Arena" + Style.RESET_ALL)
	print(deadArt)
	print(" ")
	print("     ||" + healthDisplay + remainingDisplay + "\033[1;37;40m||")
	print("     ||" + manaDisplay + str(remainingDisplayMana) + "\033[1;37;40m||")
	print("             \033[1;31;40mOrc " + "LVL 1" + "\n" + Style.RESET_ALL)
	print("     Inventory:" + str(playerInventory) + Style.RESET_ALL +"\n")
	playerWarning = " You can't move while enemy is present!"
	print(30 * '\033[1;37;40m-' + " " + playerWarning)


def getDamage():
	global health
	health -= 30

def getHealed():
	global health
	health += 30


def enemyPresent():

    global randomA
    global NPCrate

    """if randomA == NPCrate:
        enemyPresent = True
        return enemyPresent
    elif randomA != NPCrate:
        enemyPresent = False
        return enemyPresent"""

def updateFrame():

	global health
	global playerInventory
	global futurePosition
	global previousPosition
	global gameOver
	global answerTwo
	global playerStory
	global playerWarning
	global spaceX
	global randomNPC
	global NPCrate
	global a, b, c, d, e
	global emptyMap
	global roomOne
	global roomTwo
	global roomThree
	global roomFour
	global roomFive
	global roomSix
	global roomSeven
	global roomEight
	global roomNine
	global randomA
	global currentFloor
	global enemyPresent, lootPresent
	global maxHealth, healthDashes
	global currentDashes
	global bf0, bf1, bf2, x1, x2, x3, y1, y2, y3, z1, z2, z3
	global encounterBox, getHealed, getDamage
	global mana, maxMana, minMana, manaDashes
	global answer, trapBox, battleScreen

	y1 = random.choice([c, c, c, c, c, c, c, c, c, z1, x1])
	y2 = random.choice([d, d, d, d, d, d, d, d, d, z2, x2])
	y3 = random.choice([e, e, e, e, e, e, e, e, e, z3, x3])

	if y1 == x1 or y2 == x2 or y3 == x3:
		enemyPresent = True

		if enemyPresent == True:
			trapBox = 1
			randomN = random.randint(1,101)
			health -= randomN
			playerWarning = "Enemy attacked you! for " + str(randomN) + " damage"

	if y1 == z1 or y2 == z2 or y3 == z3:
		lootPresent = True

		if lootPresent == True:
			randomN = random.randint(1,101)
			health += randomN
			playerWarning = "You found a chest! and healed " + str(randomN) + " health"

	if health > 200:
		health = 200

	roomOne = b + y1 + b + a + b + a + bf2
	roomTwo = b + y2 + b + a + b + a + bf2
	roomThree = b + y3 + b + a + b + a + bf2
	roomFour = b + a + b + y1 + b + a + bf1
	roomFive = b + a + b + y2 + b + a + bf1
	roomSix = b + a + b + y3 + b + a + bf1
	roomSeven = b + a + b + a + b + y1 + bf0
	roomEight = b + a + b + a + b + y2 + bf0
	roomNine = b + a + b + a + b + y3 + bf0



	dashConvert = int(maxHealth/healthDashes)
	dashConvertMana = int(maxMana/manaDashes)
	currentDashes = int(health/dashConvert)
	currentDashesMana = int(mana/dashConvertMana)
	remainingHealth = healthDashes - currentDashes
	remainingMana = manaDashes - currentDashesMana
	healthDisplay = '\033[1;31;40m+' * currentDashes
	manaDisplay = Fore.BLUE + "=" * currentDashesMana
	remainingDisplay = ' ' * remainingHealth
	remainingDisplayMana = ' ' * remainingMana
	percent = str(int((health/maxHealth)*100)) + "%"
	percentMana = str(int((mana/maxMana)*100)) + "%"

	if health < 0.1 and trapBox == 1:
		print(chr(27) + "[2J")
		print(deadArt)
		printSlow("You Died!\n")
		printSlow("Do you want to play again? yes/no\n")
		answerTwo = input("\033[1;37;40m > ").lower()
		if answerTwo == "no":
			gameOver = True
		elif answerTwo == "yes":
			health = 200.0
			trapBox = 0
			playerInventory = " empty"
			playerBox = 7
			futurePosition = roomSeven
			previousPosition = roomSeven
			gameOver = False



          #########Frame#########



	while trapBox == 1:
		playerWarning = " Do you want to enter ?"
		trapBoxAnswer = input().lower()

		if trapBoxAnswer == "yes":
			exec(open("/Users/amihaianuc/Desktop/old-school-rpg/caveMiniGame.py").read())
			updateFrame()
		
		else:
			trapBox = 0
			updateFrame()

	print(clearTop)
	print(futurePosition)
	GUI.frame()

	playerWarning = " "




print(chr(27) + "[2J")
print(30 * '-')
print("")
print(Fore.RED + "             Arena" + Fore.WHITE)
print("")
print("")
print("""type "help" for known commands""")
print("")
print(30 * '-')
print ("")

# Debug
# debugMap()


while trapBox == 0:
	from GUI import frame
	answer = input("\033[1;37;40m > ").lower()
	if answer == "help":
	    print(" ")
	    printSlow(" you can use the following commands: h, q, d, m, s, f, debug, up")
	    print(" ")
	elif answer == "q":
	    printSlow(chr(27) + "[2J")
	    print("\n")
	    break
	elif answer == "h":
		getHealed()
		updateFrame()
	elif answer == "debug":
	    print("\nplayerBox is " + str(playerBox))
	    print("\nfuturePosition is \n" + str(futurePosition))
	elif answer == "upupdowndownleftrightleftrightselectstart":
		easterEgg()
	elif answer == "new game":
		updateFrame()
	elif answer == 'w' and playerBox == 5:
		futurePosition = roomTwo
		playerBox = 2
		updateFrame()
	elif answer == "s" and playerBox == 5:
		futurePosition = roomEight
		playerBox = 8
		updateFrame()
	elif answer == "d" and playerBox == 5:
		futurePosition = roomSix
		playerBox = 6
		updateFrame()
	elif answer == "a" and playerBox == 5:
		futurePosition = roomFour
		playerBox = 4
		updateFrame()
	elif answer == "w" and playerBox == 2:
		futurePosition = roomTwo
		playerBox = 2
		playerWarning = "You can't go up. There's a wall."
		updateFrame()
	elif answer == "s" and playerBox == 2:
		futurePosition = roomFive
		playerBox = 5
		updateFrame()
	elif answer == "d" and playerBox == 2:
		futurePosition = roomThree
		playerBox = 3
		updateFrame()
	elif answer == "a" and playerBox == 2:
		futurePosition = roomOne
		playerBox = 1
		updateFrame()
	elif answer == "w" and playerBox == 8:
		futurePosition = roomFive
		playerBox = 5
		updateFrame()
	elif answer == "s" and playerBox == 8:
		futurePosition = roomEight
		playerBox = 8
		playerWarning = "You can't go down. There's a wall."
		updateFrame()
	elif answer == "d" and playerBox == 8:
		futurePosition = roomNine
		playerBox = 9
		updateFrame()
	elif answer == "a" and playerBox == 8:
		futurePosition = roomSeven
		playerBox = 7
		updateFrame()
	elif answer == "w" and playerBox == 1:
		futurePosition = roomOne
		playerBox = 1
		playerWarning = "You can't go up. There's a wall."
		updateFrame()
	elif answer == "s" and playerBox == 1:
		futurePosition = roomFour
		playerBox = 4
		updateFrame()
	elif answer == "d" and playerBox == 1:
		futurePosition = roomTwo
		playerBox = 2
		updateFrame()
	elif answer == "a" and playerBox == 1:
		futurePosition = roomOne
		playerBox = 1
		playerWarning = "You can't go left. There's a wall."
		updateFrame()
	elif answer == "w" and playerBox == 3:
		futurePosition = roomThree
		playerBox = 3
		playerWarning = "You can't go up. There's a wall."
		updateFrame()
	elif answer == "s" and playerBox == 3:
		futurePosition = roomSix
		playerBox = 6
		updateFrame()
	elif answer == "d" and playerBox == 3:
		futurePosition = roomThree
		playerBox = 3
		playerWarning = "You can't go right. There's a wall."
		updateFrame()
	elif answer == "a" and playerBox == 3:
		futurePosition = roomTwo
		playerBox = 2
		updateFrame()
	elif answer == "w" and playerBox == 4:
		futurePosition = roomOne
		playerBox = 1
		updateFrame()
	elif answer == "s" and playerBox == 4:
		futurePosition = roomSeven
		playerBox = 7
		updateFrame()
	elif answer == "d" and playerBox == 4:
		futurePosition = roomFive
		playerBox = 5
		updateFrame()
	elif answer == "a" and playerBox == 4:
		futurePosition = roomFour
		playerBox = 4
		playerWarning = "You can't go left. There's a wall."
		updateFrame()
	elif answer == "w" and playerBox == 6:
		futurePosition = roomThree
		playerBox = 3
		updateFrame()
	elif answer == "s" and playerBox == 6:
		futurePosition = roomNine
		playerBox = 9
		updateFrame()
	elif answer == "d" and playerBox == 6:
		futurePosition = roomSix
		playerBox = 6
		playerWarning = "You can't go right. There's a wall."
		updateFrame()
	elif answer == "a" and playerBox == 6:
		futurePosition = roomFive
		playerBox = 5
		updateFrame()
	elif answer == "w" and playerBox == 7:
		futurePosition = roomFour
		playerBox = 4
		updateFrame()
	elif answer == "s" and playerBox == 7:
		futurePosition = roomSeven
		playerBox = 7
		playerWarning = "You can't go down. There's a wall."
		updateFrame()
	elif answer == "d" and playerBox == 7:
		futurePosition = roomEight
		playerBox = 8
		updateFrame()
	elif answer == "a" and playerBox == 7:
		futurePosition = roomSeven
		playerBox = 7
		playerWarning = "You can't go left. There's a wall."
		updateFrame()
	elif answer == "w" and playerBox == 9:
		futurePosition = roomSix
		playerBox = 6
		updateFrame()
	elif answer == "s" and playerBox == 9:
		futurePosition = roomNine
		playerBox = 9
		playerWarning = "You can't go down. There's a wall."
		updateFrame()
	elif answer == "d" and playerBox == 9:
		futurePosition = roomNine
		playerBox = 9
		playerWarning = "You can't go right. There's a wall."
		updateFrame()
	elif answer == "a" and playerBox == 9:
		futurePosition = roomEight
		playerBox = 8
		updateFrame()
	elif answer == "take key" and playerBox == 1:
		futurePosition = roomOne
		playerBox = 1
		playerInventory = 'key'
		playerWarning = "You got a small key."
		updateFrame()

	elif answer == "start":
	    updateFrame()

	elif answer == "d":
	    getDamage()

	elif answer == "s":
		playerWarning = "Game is saved."
		updateFrame()

	else:
		print("Not a valid command!")






