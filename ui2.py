# -*- coding: utf-8 -*-

# GPU
from ownlib import clearTop, printSlow
from colorama import Fore, Back, Style
import time
import random
from monsters import *

run = True


#Random Encounterasd

enemyShown = random.choice(monsterList)

randomLocation = random.choice(locationList)

lootChance = random.choice(lootList)

randomItem = random.choice(randomItemsList)

itemPower = 10

npcLevel = random.randint(1,2)

enemyName = " "
locationName = " "

loot = False

if randomLocation == locationList[0]:
	locationName = "Cavern"
elif randomLocation == locationList[1]:
	locationName = "Castle"

if lootChance == lootList[0]:
	loot = True

if enemyShown == monsterList[0]:
	enemyName = "Cyclop"
elif enemyShown == monsterList[1]:
	enemyName = "Spider"
elif enemyShown == monsterList[2]:
	enemyName = "Fairy"

#Random Encounter

fTop = "+---------------------------------+\n"
fBot = "+---------------------------------+"
fN = "|                                 |\n"

emptyFrame = fTop + (20 * fN) + fBot 


#############
clearTop = chr(27) + "[2J"

playerWarning = " "


############################# PLAYER INFO #################################

### Health ###
health = 280
maxHealth = 280
healthDashes = 31
# HP Logic
dashConvert = int(maxHealth/healthDashes)
currentDashes = int(health/dashConvert)
remainingHealth = healthDashes - currentDashes
# HP Bar
healthDisplay = '\033[1;31;40m+' * currentDashes
remainingDisplay = ' ' * remainingHealth
### Health ###


### Stats ###
# Attack
playerAtkMin = 55
playerAtkMax = 80
playerAtkMod = 1
playerAtk = random.randint(playerAtkMin, playerAtkMax)
# Defense
playerDef = 10
playerDefMin = 10
playerDefMax = 200
playerDefMod = 1
### XP ###
xp = 0
maxxp = 200
xpDashes = 31
#Logic
dashConvertxp = int(maxxp/xpDashes)
currentDashesxp = int(xp/dashConvertxp)
xpRemain = xpDashes - currentDashesxp
# Bar
xpDisplay = Fore.BLUE + "=" * currentDashesxp
remainingXpDisplay = ' ' * xpRemain



### XP ###

### Stats ###

############################# PLAYER INFO #################################

############################# ENEMY INFO #################################

### Health ###
Ehealth = 90
EmaxHealth = 350
Edashes = 31
# HP Logic
EdashConvert = int(EmaxHealth/Edashes)
EcurrentDashes = int(Ehealth/EdashConvert)
EremainingHealth = Edashes - EcurrentDashes
# HP Bar
EhealthDisplay = '\033[1;31;40m+' * EcurrentDashes
EremainingDisplay = ' ' * EremainingHealth
### Health ###

### Stats ###
# Attack
npcAtkMin = 1
npcAtkMax = 35
npcAtkMod = 1
npcAtk = random.randint(npcAtkMin, npcAtkMax)
# Defense
npcDef = 10
npcDefMod = 1
### Stats ###

# XP
xpGain = random.randint(9, 38)

############################# ENEMY INFO #################################



############################# ATTACKS #################################

def attkPlayer():
	global health, playerDef, playerDefMod, npcAtkMod, npcAtk

	npcAtk = random.randint(npcAtkMin, npcAtkMax)
	print(npcAtk)

	health = health - npcAtk

def attkNpc():
	global Ehealth, npcDef, npcDefMod, playerAtkMod, playerAtkMax, playerAtkMin, playerAtk

	playerAtk = random.randint(playerAtkMin, playerAtkMax)


	Ehealth = Ehealth -  playerAtk


############################# ATTACKS #################################

### FRAMES ###
def emptyF():
	print(clearTop)
	print(" ")
	print(playerWarning)
	print("+" + 47 * '\033[1;37;40m-' + "+")
	print(" ||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP " + str(health) + "/" + str(maxHealth) + Fore.WHITE)
	print(" ||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP " + str(xp) + "/" + str(maxxp) + Fore.WHITE)
	print("+" + 47 * '\033[1;37;40m-' + "+")

def emptyFr():
	print(clearTop)
	print(randomLocation)
	print(playerWarning)
	print("+" + 47 * '\033[1;37;40m-' + "+")
	print(" ||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP " + str(health) + "/" + str(maxHealth) + Fore.WHITE)
	print(" ||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP " + str(xp) + "/" + str(maxxp) + Fore.WHITE)
	print("+" + 47 * '\033[1;37;40m-' + "+")

def emptyFrr():
	print(clearTop)
	print(randomLocation)
	print(playerWarning)
	print("+" + 47 * '\033[1;37;40m-' + "+")
	print(" ||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP " + str(health) + "/" + str(maxHealth) + Fore.WHITE)
	print(" ||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP " + str(xp) + "/" + str(maxxp) + Fore.WHITE)
	print("+" + 47 * '\033[1;37;40m-' + "+")

def lootFrame():
	print(clearTop)
	print(Fore.YELLOW + lootBoxArt + Fore.WHITE)
	print(playerWarning)
	print("+" + 47 * '\033[1;37;40m-' + "+")
	print(" ||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP " + str(health) + "/" + str(maxHealth) + Fore.WHITE)
	print(" ||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP " + str(xp) + "/" + str(maxxp) + Fore.WHITE)
	print("+" + 47 * '\033[1;37;40m-' + "+")

def enemyF():
	print(clearTop)
	print(enemyShown + " ||" + EhealthDisplay + str(EremainingDisplay) + "\033[1;37;40m|| ")
	print("           " + Fore.RED + "Level " + str(npcLevel) + " " + enemyName + Fore.WHITE)
	print(" ")
	print(playerWarning)
	print("+" + 47 * '\033[1;37;40m-' + "+")
	print(" ||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP " + str(health) + "/" + str(maxHealth) + Fore.WHITE)
	print(" ||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP " + str(xp) + "/" + str(maxxp) + Fore.WHITE)
	print("+" + 47 * '\033[1;37;40m-' + "+")

def enemyFr():
	print(clearTop)
	print(Fore.RED + enemyShown + Fore.WHITE + " ||" + EhealthDisplay + str(EremainingDisplay) + "\033[1;37;40m|| ")
	print("           " + Fore.RED + "Level " + str(npcLevel) + " " + enemyName + Fore.WHITE)
	print(" ")
	print(playerWarning)
	print("+" + 47 * '\033[1;37;40m-' + "+")
	print(" ||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP " + str(health) + "/" + str(maxHealth) + Fore.WHITE)
	print(" ||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP " + str(xp) + "/" + str(maxxp) + Fore.WHITE)
	print("+" + 47 * '\033[1;37;40m-' + "+")



### FRAMES ###




### COMBAT LOGIC ###

def updateBars():
	global currentDashes, health, dashConvert, remainingHealth, healthDashes, healthDisplay, remainingDisplay, remainingXpDisplay
	global EcurrentDashes, Ehealth, EdashConvert, EremainingHealth, Edashes, EcurrentDashes, EhealthDisplay, EremainingDisplay, xpGain

	xpGain = random.randint(9, 38)

	### PLAYER ###
	# HP LOGIC
	currentDashes = int(health/dashConvert)
	remainingHealth = healthDashes - currentDashes
	# HP Bar
	healthDisplay = '\033[1;31;40m+' * currentDashes
	remainingDisplay = ' ' * remainingHealth
	### ENEMY ###
	# EHP Logic
	EcurrentDashes = int(Ehealth/EdashConvert)
	EremainingHealth = Edashes - EcurrentDashes
	# EHP Bar
	EhealthDisplay = '\033[1;31;40m+' * EcurrentDashes
	EremainingDisplay = ' ' * EremainingHealth

	if EremainingDisplay.count(" ") > 31:
		EremainingDisplay = " " * 31
	elif remainingDisplay.count(" ") > 31:
		remainingDisplay = " " * 31
	elif remainingXpDisplay.count(" ") > 31:
		remainingXpDisplay = " " * 31

### COMBAT LOGIC ###


### ANIMATION ###
def EnemyAttacksPlayer():
	global playerWarning, EremainingDisplay, remainingDisplay, run, npcAtk, xp , xpGain, remainingXpDisplay

	emptyF()
	time.sleep(0.1)
	enemyF()
	time.sleep(0.1)
	playerWarning = " " + enemyName + " hits you for " + str(npcAtk) + " dmg!"
	enemyFr()
	enemyF()
	time.sleep(0.1)

	if EremainingDisplay.count(" ") > 31:
		EremainingDisplay = " " * 31
	elif remainingDisplay.count(" ") > 31:
		remainingDisplay = " " * 31
	elif remainingXpDisplay.count(" ") > 31:
		remainingXpDisplay = " " * 31

	if healthDisplay.count("+") < 1:
		print(chr(27) + "[2J")
		print(deadArt)
		time.sleep(0.1)
		print(chr(27) + "[2J")
		print(Fore.RED + deadArt + Fore.WHITE)
		time.sleep(0.1)
		print(chr(27) + "[2J")
		print(deadArt)
		time.sleep(0.1)
		print(chr(27) + "[2J")
		print(Fore.RED + deadArt + Fore.WHITE)
		print(chr(27) + "[2J")
		print(deadArt)
		time.sleep(0.1)
		print(chr(27) + "[2J")
		print(Fore.RED + deadArt + Fore.WHITE)
		time.sleep(0.1)
		print(chr(27) + "[2J")
		print(deadArt)
		time.sleep(0.1)
		print(chr(27) + "[2J")
		print(Fore.RED + deadArt + Fore.WHITE)
		print(chr(27) + "[2J")
		print(deadArt)
		time.sleep(0.1)
		print(chr(27) + "[2J")
		print(Fore.RED + deadArt + Fore.WHITE)
		time.sleep(0.1)
		print(chr(27) + "[2J")
		print(deadArt)
		time.sleep(0.1)
		print(chr(27) + "[2J")
		print(Fore.RED + deadArt + Fore.WHITE)
		print(chr(27) + "[2J")
		print(deadArt)
		time.sleep(0.1)
		print(chr(27) + "[2J")
		print(Fore.RED + deadArt + Fore.WHITE)
		time.sleep(0.1)
		print(chr(27) + "[2J")
		print(deadArt)
		time.sleep(0.1)
		print(chr(27) + "[2J")
		print(Fore.RED + deadArt + Fore.WHITE)
		print(Fore.RED + "You Died!" + Fore.WHITE)

def PlayerAttacksEnemy():
	global playerWarning, EremainingDisplay, remainingXpDisplay,remainingDisplay, run, xp, xpGain, currentDashesxp, dashConvertxp, xpRemain, xpDashes, maxxp, xpDisplay


	if EremainingDisplay.count(" ") > 31:
		EremainingDisplay = " " * 31
	elif remainingDisplay.count(" ") > 31:
		remainingDisplay = " " * 31
	elif remainingXpDisplay.count(" ") > 31:
		remainingXpDisplay = " " * 31

	if healthDisplay.count("+") < 1:
		print(chr(27) + "[2J")
		print(deadArt)
		print("You Died!")
		run = False
	elif EhealthDisplay.count("+") < 1:
		playerWarning = " "



		emptyF()
		enemyFr()
		time.sleep(0.3)
		enemyF()
		time.sleep(0.2)
		enemyFr()
		time.sleep(0.2)
		enemyF()
		time.sleep(0.2)

		xp = xp + xpGain

		# PLAYER XP LOGIC
		currentDashesxp = int(xp/dashConvertxp)
		xpRemain = xpDashes - currentDashesxp

		# PLAYER XP Bar
		xpDisplay = Fore.BLUE + "=" * currentDashesxp
		remainingXpDisplay = ' ' * xpRemain

		

		if enemyShown == monsterList[2] and EhealthDisplay.count("+") < 4:
			playerWarning = Fore.YELLOW + enemyName + " panicked and ran away!" + Fore.BLUE + " + " + str(xpGain) + " XP " + Fore.WHITE + "!"

		else:
			playerWarning = Fore.YELLOW + " You killed the " + enemyName + "!" + Fore.BLUE + " + " + str(xpGain) + " XP " + Fore.WHITE + "!"





	else:
		emptyF()
		time.sleep(0.1)
		enemyF()
		time.sleep(0.1)
		playerWarning = " You hit " + enemyName + " for " + str(((playerAtk * playerAtkMod) - (npcDef * npcDefMod))) + " dmg!"
		enemyFr()
		enemyF()
		time.sleep(0.1)

	

### ANIMATION ###




print(clearTop)
emptyFrr()
playerWarning = "Entering " + locationName.lower() + "."
time.sleep(0.1)
print(clearTop)
emptyFrr()
playerWarning = "Exploring " + locationName.lower() + ".."
time.sleep(0.2)


def searchingForGoods():
	global playerWarning

	playerWarning = Fore.YELLOW + "\n While searching for goods" + Fore.WHITE

	emptyF()
	time.sleep(0.1)
	emptyF()
	time.sleep(0.1)
	emptyFrr()
	time.sleep(0.1)
	emptyFr()
	time.sleep(0.1)
	emptyFrr()
	time.sleep(0.1)
	emptyFr()
	time.sleep(0.1)
	emptyFrr()
	time.sleep(0.1)

	playerWarning = " "

def checkLoot():
	global playerAtk, itemPower


	if loot == True:
		playerWarning = " You found a " + Fore.YELLOW + "chest" + Fore.WHITE + "!"
		lootFrame()
		raw_input(" Press ANY key to " + Fore.YELLOW + "OPEN" + Fore.WHITE + " it ")

		playerWarning = " There was a " + Fore.BLUE + randomItem + Fore.WHITE + " inside!"
		lootFrame()
		raw_input(" Press ANY key to " + Fore.BLUE + "EQUIP" + Fore.WHITE + " it ")

		playerWarning = "You have " + Fore.BLUE + "EQUIPED" + Fore.WHITE + " the " + Fore.BLUE + randomItem + Fore.WHITE + " and " + Fore.BLUE + "increased " + Fore.WHITE + "your attack by " + Fore.BLUE + str(itemPower) + Fore.WHITE + "!"
		lootFrame()
		raw_input(" Press ANY key to further " + Fore.YELLOW + "EXPLORE " + Fore.WHITE + "the " + locationName + " ")

		playerAtk = playerAtk + itemPower


		playerWarning = "Exploring " + locationName.lower() + ".."
		emptyFrr()
		time.sleep(0.2)

	else:
		searchingForGoods()
		playerWarning = " A " + enemyName + " has noticed you!"

playerWarning = " "

searchingForGoods()
checkLoot()




### Combat Loop ###


while run == True:

	randomItem = random.choice(randomItemsList)

	if EhealthDisplay.count("+") < 1:
		emptyF()
		time.sleep(1)
		playerWarning = " Keep " + Fore.RED + "exploring " + Fore.WHITE + "the " + Fore.BLUE + locationName.lower() + Fore.WHITE + " ?"
		emptyF()


		if enemyShown == monsterList[2]:
			playerWarning = " The Fairy restored all your health!"

			health = maxHealth

			updateBars()

			enemyF()
			time.sleep(0.2)
			emptyF()
			time.sleep(0.2)
			enemyF()
			time.sleep(0.2)
			emptyF()



		advanceAnswer = raw_input(" Press ENTER to CONTINUE ").lower()
		if advanceAnswer == "yes" or advanceAnswer == "y" or advanceAnswer != False:

			enemyShown = random.choice(monsterList)

			if enemyShown == monsterList[0]:
				enemyName = "Cyclop"
			elif enemyShown == monsterList[1]:
				enemyName = "Spider"
			elif enemyShown == monsterList[2]:
				enemyName = "Fairy"

			Ehealth = 300
			npcLevel = random.randint(1,2)
			playerWarning = Fore.YELLOW + " While searching for goods" + Fore.WHITE

			lootChance = random.choice(lootList)

			emptyFrr()
			time.sleep(0.1)
			emptyFr()
			time.sleep(0.1)
			emptyFrr()
			time.sleep(0.1)
			emptyFr()
			time.sleep(0.1)
			emptyFrr()
			time.sleep(0.1)
			emptyFr()
			time.sleep(0.1)
			emptyFrr()
			time.sleep(0.1)
			checkLoot()
			searchingForGoods()
			playerWarning = " A " + enemyName + " has noticed you!"
			emptyF()
			time.sleep(1.3)

		elif advanceAnswer == "no" or advanceAnswer == "n":
			emptyF()
			time.sleep(0.4)
			print(clearTop)
			print(randomLocation)
			printSlow("Returning to entrance")
			time.sleep(0.2)
			print(clearTop)
			print(randomLocation)
			printSlow("Leaving " + locationName.lower() + "..")
			time.sleep(0.2)
			print(clearTop)

			exit()

		else:
			advanceAnswer = raw_input().lower()
			emptyF()
			playerWarning = "Yes or No"





	attkPlayer()
	updateBars()
	EnemyAttacksPlayer()


	if healthDisplay.count("+") < 1:
		combatAnswer = raw_input(Fore.RED + "Press ANY key to EXIT " + Fore.WHITE).lower()
	else:
		combatAnswer = raw_input(Fore.BLUE + " Press ENTER to ATTACK " + Fore.WHITE).lower()


	if combatAnswer != False:
		attkNpc()
		updateBars()
		PlayerAttacksEnemy()
	else:
		playerWarning = " You need to attack!"



