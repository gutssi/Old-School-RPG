# -*- coding: utf-8 -*-

from ownlib import clearTop, printSlow
from colorama import Fore, Back, Style
import time
import random
from monsters import *


run = True

### Random Encounter ###
# Run only once
randomLocation = random.choice(locationList)
# Needs refresh
enemyShown = random.choice(monsterList)
lootChance = random.choice(lootList)
randomItem = random.choice(randomItemsList)
itemPower = random.randint(13, 24)

enemyName = None
locationName = None

loot = False


combatAnswer = None


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



############################# PLAYER INFO #################################

### Health ###
health = 250
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
playerAtkMin = 15
playerAtkMax = 44
playerAtkMod = 1
playerAtk = random.randint(playerAtkMin, playerAtkMax)
# Defense
playerDef = 10
playerDefMin = 10
playerDefMax = 200
playerDefMod = 1
### XP ###
xp = 110
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
npcLevel = random.randint(1,2)

### Stats ###

############################# PLAYER INFO #################################

############################# ENEMY INFO #################################

### Health ###
Ehealth = 150
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
npcAtkMax = 70
npcAtkMod = 1
npcAtk = random.randint(npcAtkMin, npcAtkMax)
# Defense
npcDef = 10
npcDefMod = 1
### Stats ###

# XP
xpGain = random.randint(9, 38)

playerWarning = " A " + enemyName + " has noticed you!"


### FRAMES ###
def attkPlayer():
	global health, playerDef, playerDefMod, npcAtkMod, npcAtk, playerWarning

	playerWarning = ""

	npcAtk = random.randint(npcAtkMin, npcAtkMax)

	health = health - npcAtk

def attkNpc():
	global Ehealth, npcDef, npcDefMod, playerAtkMod, playerAtkMax, playerAtkMin, playerAtk

	playerAtk = random.randint(playerAtkMin, playerAtkMax)


	Ehealth = Ehealth -  playerAtk

def emptyF():
	print(clearTop)
	print(" ")
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

def PlayerAttacksEnemy():
	global playerWarning, EremainingDisplay, remainingXpDisplay,remainingDisplay, run, xp, xpGain, currentDashesxp, dashConvertxp, xpRemain, xpDashes, maxxp, xpDisplay


	attkNpc()

	updateBars()

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

		playerWarning = Fore.YELLOW + "You killed the " + enemyName + "!" + Fore.BLUE + " + " + str(xpGain) + " XP " + Fore.WHITE + "!"
	elif Ehealth > 0:
		emptyF()
		time.sleep(0.1)
		enemyF()
		time.sleep(0.1)
		playerWarning = "You hit " + enemyName + " for " + str(((playerAtk * playerAtkMod) - (npcDef * npcDefMod))) + " dmg!"
		enemyFr()
		enemyF()
		time.sleep(0.1)

def EnemyAttacksPlayer():
	global EremainingHealth, EremainingDisplay, remainingDisplay, remainingXpDisplay, playerWarning, enemyName

	attkPlayer()

	updateBars()

	playerWarning = enemyName + " hits you for " + str(npcAtk) + " dmg!"

	if EremainingDisplay.count(" ") > 31:
		EremainingDisplay = " " * 31
	elif remainingDisplay.count(" ") > 31:
		remainingDisplay = " " * 31
	elif remainingXpDisplay.count(" ") > 31:
		remainingXpDisplay = " " * 31

	if healthDisplay.count("+") < 1:
		for i in range(8):

			print(chr(27) + "[2J")
			print(deadArt)
			time.sleep(0.1)
			print(chr(27) + "[2J")
			print(Fore.RED + deadArt + Fore.WHITE)
			time.sleep(0.1)

		print(clearTop)
		print(deadArt)
		printSlow(Fore.RED + "You Died!\n" + Fore.WHITE)
		exit()





	

			
def npc_animation():
	attkPlayer()
	updateBars()
	EnemyAttacksPlayer()

def player_animation():
	attkNpc()
	updateBars()
	PlayerAttacksEnemy()

def searchingForGoods():
	global playerWarning

	randomItem = random.choice(randomItemsList)
	lootChance = random.choice(lootList)


	playerWarning = " "

def enemyAlert():
	global playerWarning

	lootChance = random.choice(lootList)

	for i in range(3):
		playerWarning = Fore.RED + " A " + enemyName + " has noticed you!" + Fore.WHITE
		emptyF()
		time.sleep(0.2)
		playerWarning = Fore.WHITE + " A " + enemyName + " has noticed you!" + Fore.WHITE
		emptyF()
		time.sleep(0.2)

	playerWarning = " "

	EnemyAttacksPlayer()

def enteringPlace():
	print(clearTop)
	print(randomLocation)
	printSlow("Entering " + locationName.lower() + ".")
	time.sleep(0.1)
	print(clearTop)
	print(randomLocation)
	printSlow("Exploring " + locationName.lower() + "..")
	time.sleep(0.2)

def checkLoot():
	global playerAtk, itemPower


	if loot == True:
		print(clearTop)
		print(Fore.YELLOW + lootBoxArt + Fore.WHITE)
		print("You found a " + Fore.YELLOW + "chest" + Fore.WHITE + "!\n")
		raw_input("Press ANY key to " + Fore.YELLOW + "OPEN" + Fore.WHITE + " it ")

		print(clearTop)
		print(Fore.YELLOW + lootBoxArt + Fore.WHITE)
		print("There was a " + Fore.BLUE + randomItem + Fore.WHITE + " inside!")
		raw_input("Press ANY key to " + Fore.BLUE + "EQUIP" + Fore.WHITE + " it ")

		print(clearTop)
		print(Fore.YELLOW + lootBoxArt + Fore.WHITE)
		print("You have " + Fore.BLUE + "EQUIPED" + Fore.WHITE + " the " + Fore.BLUE + randomItem + Fore.WHITE + " and " + Fore.BLUE + "increased " + Fore.WHITE + "your attack by " + Fore.BLUE + str(itemPower) + Fore.WHITE + "!")
		raw_input("Press ANY key to further " + Fore.YELLOW + "EXPLORE " + Fore.WHITE + "the " + locationName + " ")
		playerAtk = playerAtk + itemPower

def exploringPlace():
	print(clearTop)
	print(randomLocation)
	time.sleep(0.1)
	print(clearTop)
	print(randomLocation)
	playerWarning = "Exploring " + locationName.lower() + ".."
	time.sleep(0.2)

	checkLoot()
	searchingForGoods()
	enemyAlert()



def checkDeath():

	if EhealthDisplay.count("+") < 1:
		pass



### Start of Loop

enteringPlace()
exploringPlace()

if healthDisplay.count("+") > 1 and EremainingDisplay.count("+") > 1:

	combatAnswer = raw_input("Press ANY key to ATTACK! ")

	while combatAnswer  != False:
		combatAnswer = raw_input("Press ANY key to ATTACK! ")
		PlayerAttacksEnemy()
		EnemyAttacksPlayer()

		if EremainingDisplay.count("+") < 1:

			advanceAnswer = raw_input().lower()
			if advanceAnswer == "yes" or advanceAnswer == "y":

				enemyShown = random.choice(monsterList)

				if enemyShown == monsterList[0]:
					enemyName = "Cyclop"
				elif enemyShown == monsterList[1]:
					enemyName = "Spider"

				Ehealth = 300
				playerWarning = Fore.YELLOW + "While searching for goods" + Fore.WHITE
				exploringPlace()

				lootChance = random.choice(lootList)

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




				emptyF()
				time.sleep(0.2)
				enemyF()
				time.sleep(0.2)

				enemyFr()
				time.sleep(0.2)
				enemyF()
				time.sleep(0.2)








