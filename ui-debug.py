# -*- coding: utf-8 -*-

# GPU
from tabulate import tabulate
from ownlib import printSlow
from colorama import Fore, Back, Style
import time
import random


run = True

npcCyclop ="""
\\           _......._
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


fTop = "+---------------------------------+\n"
fBot = "+---------------------------------+"
fN = "|                                 |\n"

emptyFrame = fTop + (20 * fN) + fBot

table = [[npcCyclop]]
cyclop = tabulate(table, tablefmt='grid')

enemyFrame = cyclop

#############
 

playerWarning = " "


############################# PLAYER INFO #################################

### Health ###
health = 500
maxHealth = 1000
healthDashes = 31
# HP Logic
dashConvert = int(maxHealth/healthDashes)
currentDashes = int(health/dashConvert)
remainingHealth = healthDashes - currentDashes
# HP Bar
healthDisplay = '\033[1;31;40m+' * currentDashes
remainingDisplay = ' ' * remainingHealth
### Health ###



### Health ###
XPPlayer = 500
XPGain = 400
XPMax = 1000
XPDashes = 31
# HP Logic
XPConvert = int(XPMax/XPDashes)
XPPlayer = XPPlayer + XPGain
XPCurrentDashes = int(XPPlayer/XPConvert)
XPRemaining = XPDashes - XPCurrentDashes
# HP Bar
XPDisplay = '\033[1;31;40m+' * XPCurrentDashes
XPRemainingDisplay = ' ' * XPRemaining

print("||" + XPDisplay + str(XPRemainingDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP" + Fore.WHITE)



if XPDashes.count("+") > 31:
		XPDashes = "+" * 31



XPConvert = int(XPMax/XPDashes)
XPPlayer = XPPlayer + XPGain
XPCurrentDashes = int(XPPlayer/XPConvert)
XPRemaining = XPDashes - XPCurrentDashes
# HP Bar
XPDisplay = '\033[1;31;40m+' * XPCurrentDashes
XPRemainingDisplay = ' ' * XPRemaining



print("||" + XPDisplay + str(XPRemainingDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP" + Fore.WHITE)
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
xp = 50
maxxp = 600
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
Ehealth = 300
EmaxHealth = 500
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
xpGain = 150

############################# ENEMY INFO #################################



############################# ATTACKS #################################

def attkPlayer():
	global health, playerDef, playerDefMod, npcAtkMod, npcAtk

	npcAtk = random.randint(npcAtkMin, npcAtkMax)
	print(npcAtk)

	health = health - npcAtk
	print(" attkplayer :" + str(health))



def attkNpc():
	global Ehealth, npcDef, npcDefMod, playerAtkMod, playerAtkMax, playerAtkMin, playerAtk

	playerAtk = random.randint(playerAtkMin, playerAtkMax)


	Ehealth = Ehealth -  playerAtk


############################# ATTACKS #################################

### FRAMES ###
def emptyF():
	global playerWarning

	print() #Clear
	print(Back.RED + "                                   " + Back.BLACK)
	print(Back.RED + "              Cyclop               " + Back.BLACK) #Name
	print("||" + EhealthDisplay + str(EremainingDisplay) + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print(emptyFrame) #Enemy if any?

	print("||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print("||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP" + Fore.WHITE) #Health and xp bars
	print(Fore.WHITE + playerWarning)
	print(36 * '\033[1;37;40m-')
	print("empty frame + xp" + str(xp))

def enemyF():
	global playerWarning, xpDisplay, remainingXpDisplay, xp

	print() #Clear
	print(Back.RED + "                                   " + Back.BLACK)
	print(Back.RED + "              Cyclop               " + Back.BLACK) #Name
	print("||" + EhealthDisplay + str(EremainingDisplay) + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print(cyclop) #Enemy if any?

	print("||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print("||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP" + Fore.WHITE) #Health and xp bars
	print(Fore.WHITE + playerWarning)
	print(36 * '\033[1;37;40m-')
	print("enemy frame + xp" + str(xp))

def enemyFr():
	global playerWarning

	print() #Clear
	print(Back.RED + "                                   " + Back.BLACK)
	print(Back.RED + "              Cyclop               " + Back.BLACK) #Name
	print("||" + EhealthDisplay + str(EremainingDisplay) + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print(Fore.RED + cyclop + Fore.WHITE) #Enemy if any?

	print("||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print("||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP" + Fore.WHITE) #Health and xp bars
	print(Fore.RED + playerWarning + Fore.WHITE)
	print(36 * '\033[1;37;40m-')
	print("enemy frame red + xp" + str(xp))

	time.sleep(0.5)

def enemyFd():
	global playerWarning

	print() #Clear
	print(Back.RED + "                                   " + Back.BLACK)
	print(Back.RED + "              Cyclop               " + Back.BLACK) #Name
	print("||" + EhealthDisplay + str(EremainingDisplay) + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print(Fore.RED + cyclop + Fore.WHITE) #Enemy if any?

	print("||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print("||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP" + Fore.WHITE) #Health and xp bars
	print(Fore.RED + playerWarning + Fore.WHITE)
	print(36 * '\033[1;37;40m-')
	print("enemty Fd + xp" + str(xp))

	time.sleep(0.5)
### FRAMES ###




### COMBAT LOGIC ###

def updateHealthBars():
	global currentDashes, health, dashConvert, remainingHealth, healthDashes, healthDisplay, remainingDisplay
	global EcurrentDashes, Ehealth, EdashConvert, EremainingHealth, Edashes, EcurrentDashes, EhealthDisplay, EremainingDisplay
	global currentDashesxp, dashConvertxp, xpRemain, xpDashes, dashConvertxp, xp

	### PLAYER ###
	# HP LOGIC
	currentDashes = int(health/dashConvert)
	remainingHealth = healthDashes - currentDashes
	# HP Bar
	healthDisplay = '\033[1;31;40m+' * currentDashes
	remainingDisplay = ' ' * remainingHealth

	# XP
	currentDashesxp = int(xp/dashConvertxp)
	xpRemain = xpDashes - currentDashesxp
	# XP Bar
	xpDisplay = Fore.BLUE + "=" * currentDashesxp
	remainingXpDisplay = ' ' * xpRemain


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
	global playerWarning, EremainingDisplay, remainingDisplay, run, npcAtk, xp ,xpGain

	emptyF()
	time.sleep(0.1)
	enemyF()
	time.sleep(0.1)
	playerWarning = "Cyclop attacked you for " + str(npcAtk) + " dmg!"
	enemyFr()
	enemyF()
	time.sleep(0.1)


	if EremainingDisplay.count(" ") > 31:
		EremainingDisplay = " " * 31
	elif remainingDisplay.count(" ") > 31:
		remainingDisplay = " " * 31

	if healthDisplay.count("+") < 1:
		playerWarning = "You Died!"
		run = False


def PlayerAttacksEnemy():
	global playerWarning, EremainingDisplay, remainingDisplay, run, xp, xpGain, currentDashesxp, dashConvertxp, xpRemain, xpDashes, maxxp




	if EremainingDisplay.count(" ") > 31:
		EremainingDisplay = " " * 31
	elif remainingDisplay.count(" ") > 31:
		remainingDisplay = " " * 31

	if healthDisplay.count("+") < 1:
		playerWarning = "You Died!"
		enemyFr()
		run = False
	elif EhealthDisplay.count("+") < 1:
		playerWarning = Fore.YELLOW + "You killed the Cyclop!" + Fore.BLUE + " + " + str(xpGain) + " XP " + Fore.WHITE + "!"
		# XP
		currentDashesxp = int(xp/dashConvertxp)
		xpRemain = xpDashes - currentDashesxp
	# XP Bar
		xpDisplay = Fore.BLUE + "=" * currentDashesxp
		remainingXpDisplay = ' ' * xpRemain
		xp = xp + xpGain
		print(str(xp) + " xp testare") 

		emptyF()
		enemyFr()
		time.sleep(0.3)
		enemyF()
		time.sleep(0.2)
		enemyFr()
		time.sleep(0.2)
		enemyF()
		time.sleep(0.2)

		

	

	else:
		emptyF()
		time.sleep(0.1)
		enemyF()
		time.sleep(0.1)
		playerWarning = "You attacked Cyclop for " + str(((playerAtk * playerAtkMod) - (npcDef * npcDefMod))) + " dmg!"
		enemyFr()
		enemyF()
		time.sleep(0.1)

	

### ANIMATION ###



### Combat Loop ###




while run == True:

	attkPlayer()
	print("life changes1" + str(xp))
	updateHealthBars()
	print("life changes2"  + str(xp))
	EnemyAttacksPlayer()
	print("life changes3"  + str(xp))


	combatAnswer = raw_input().lower()
	playerWarning = " "

	if combatAnswer != False:
		attkNpc()
		updateHealthBars()
		PlayerAttacksEnemy()
	else:
		playerWarning = "You need to attack!"



