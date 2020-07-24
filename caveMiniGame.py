# -*- coding: utf-8 -*-

# GPU
from tabulate import tabulate
from ownlib import clearTop, printSlow
from colorama import Fore, Back, Style
import time
import random
import art
import deadScreen


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



deadArtRed = Fore.RED + """


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

""" + Fore.WHITE


deadArt ="""


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


caveArt = """
 ********************************************************************************
*                    /   \\              /'\\       _                              *
*\\_..           /'.,/     \\_         .,'   \\     / \\_                            *
*    \\         /            \\      _/       \\_  /    \\     _                     *
*     \\__,.   /              \\    /           \\/.,   _|  _/ \\                    *
*          \\_/                \\  /',.,''\\      \\_ \\_/  \\/    \\                   *
*                           _  \\/   /    ',../',.\\    _/      \\                  *
*             /           _/m\\  \\  /    |         \\  /.,/'\\   _\\                 *
*           _/           /MMmm\\  \\_     |          \\/      \\_/  \\                *
*          /      \\     |MMMMmm|   \\__   \\          \\_       \\   \\_              *
*                  \\   /MMMMMMm|      \\   \\           \\       \\    \\             *
*                   \\  |MMMMMMmm\\      \\___            \\_      \\_   \\            *
*                    \\|MMMMMMMMmm|____.'  /\\_            \\       \\   \\_          *
*                    /'.,___________...,,'   \\            \\   \\        \\         *
*                   /       \\          |      \\    |__     \\   \\_       \\        *
*                 _/        |           \\      \\_     \\     \\    \\       \\_      *
*                /                               \\     \\     \\_   \\        \\     *
*                                                 \\     \\      \\   \\__      \\    *
*                                                  \\     \\_     \\     \\      \\   *
*                                                   |      \\     \\     \\      \\  *
*                                                    \\            |            \\ *
 ********************************************************************************
 """





fTop = "+---------------------------------+\n"
fBot = "+---------------------------------+"
fN = "|                                 |\n"

emptyFrame = fTop + (20 * fN) + fBot

table = [[npcCyclop]]
cyclop = tabulate(table, tablefmt='grid')

enemyFrame = cyclop

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
Ehealth = 40
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

############################# ENEMY INFO #################################



############################# ATTACKS #################################

def attkPlayer():
	global health, playerDef, playerDefMod, npcAtkMod, npcAtk, npcAtkMin, npcAtkMax

	npcAtk = random.randint(npcAtkMin, npcAtkMax)

	health = health - npcAtk



def attkNpc():
	global Ehealth, npcDef, npcDefMod, playerAtkMod, playerAtkMax, playerAtkMin, playerAtk

	playerAtk = random.randint(playerAtkMin, playerAtkMax)


	Ehealth = Ehealth -  playerAtk


############################# ATTACKS #################################

### FRAMES ###
def emptyF():
	global playerWarning, xpDisplay, remainingXpDisplay

	print(clearTop) #Clear
	print(Back.RED + "                                   " + Back.BLACK)
	print(Back.RED + "              Cyclop               " + Back.BLACK) #Name
	print("||" + EhealthDisplay + str(EremainingDisplay) + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print(emptyFrame) #Enemy if any?

	print("||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print("||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP" + Fore.WHITE) #Health and xp bars
	print(Fore.WHITE + playerWarning)
	print(36 * '\033[1;37;40m-')

def enemyF():
	global playerWarning, xpDisplay, remainingXpDisplay, cyclop

	print(clearTop) #Clear
	print(Back.RED + "                                   " + Back.BLACK)
	print(Back.RED + "              Cyclop               " + Back.BLACK) #Name
	print("||" + EhealthDisplay + str(EremainingDisplay) + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print(cyclop) #Enemy if any?

	print("||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print("||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP" + Fore.WHITE) #Health and xp bars
	print(Fore.WHITE + playerWarning)
	print(36 * '\033[1;37;40m-')

def enemyFr():
	global playerWarning, xpDisplay, remainingXpDisplay

	print(clearTop) #Clear
	print(Back.RED + "                                   " + Back.BLACK)
	print(Back.RED + "              Cyclop               " + Back.BLACK) #Name
	print("||" + EhealthDisplay + str(EremainingDisplay) + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print(Fore.RED + cyclop + Fore.WHITE) #Enemy if any?

	print("||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print("||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP" + Fore.WHITE) #Health and xp bars
	print(Fore.RED + playerWarning + Fore.WHITE)
	print(36 * '\033[1;37;40m-')

	time.sleep(0.5)

def emptyFr():
	global playerWarning, xpDisplay, remainingXpDisplay

	print(clearTop) #Clear
	print(Back.RED + "                                   " + Back.BLACK)
	print(Back.RED + "              Cave                 " + Back.BLACK) #Name
	print(Back.RED + "                                   " + Back.BLACK)
	print(Fore.RED + emptyFrame + Fore.WHITE)

	print("||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print("||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP" + Fore.WHITE) #Health and xp bars
	print(Fore.RED + playerWarning + Fore.WHITE)
	print(36 * '\033[1;37;40m-')

	time.sleep(0.1)

def emptyFrr():
	global playerWarning, xpDisplay, remainingXpDisplay, clearTop, emptyFrame

	print(clearTop) #Clear
	print(Back.RED + "                                   " + Back.BLACK)
	print(Back.RED + "              Cave                 " + Back.BLACK) #Name
	print(Back.RED + "                                   " + Back.BLACK)
	print(emptyFrame)

	print("||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP" + Fore.WHITE)
	print("||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP" + Fore.WHITE) #Health and xp bars
	print(Fore.RED + playerWarning + Fore.WHITE)
	print(36 * '\033[1;37;40m-')

	time.sleep(0.1)
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
	global playerWarning, EremainingDisplay, remainingDisplay, run, npcAtk, xp , xpGain, remainingXpDisplay, emptyF, enemyF, enemyFr

	emptyF()
	time.sleep(0.1)
	enemyF()
	time.sleep(0.1)
	playerWarning = "Cyclop hits you for " + str(npcAtk) + " dmg!"
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
		deadScreen.deadScreen()



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

		playerWarning = Fore.YELLOW + "You killed the Cyclop!" + Fore.BLUE + " + " + str(xpGain) + " XP " + Fore.WHITE + "!"





	else:
		emptyF()
		time.sleep(0.1)
		enemyF()
		time.sleep(0.1)
		playerWarning = "You hit Cyclop for " + str(((playerAtk * playerAtkMod) - (npcDef * npcDefMod))) + " dmg!"
		enemyFr()
		enemyF()
		time.sleep(0.1)

	

### ANIMATION ###




print(clearTop)
print(caveArt)
printSlow("Entering cave.")
time.sleep(0.1)
print(clearTop)
print(caveArt)
printSlow("Entering cave..")
time.sleep(0.2)
print(clearTop)
print(caveArt)
printSlow("Entering cave...")
time.sleep(0.3)
print(clearTop)
print(caveArt)
printSlow("Entering cave.")
time.sleep(0.9)


playerWarning = Fore.YELLOW + "Exploring the cave for goods" + Fore.WHITE

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
playerWarning = "A Cyclop has seen you!"
enemyF()
playerWarning = " "






### Combat Loop ###


while run == True:
	if EhealthDisplay.count("+") < 1:
		emptyF()
		playerWarning = "Keep " + Fore.RED + "exploring " + Fore.WHITE + "the " + Fore.BLUE + "cave" + Fore.WHITE + " ?" + Fore.YELLOW + "   Yes" + Fore.WHITE + " / " + Fore.GREEN + "No " + Fore.WHITE
		emptyF()

		advanceAnswer = input().lower()
		if advanceAnswer == "yes" or advanceAnswer == "y":
			Ehealth = 300
			playerWarning = Fore.YELLOW + "Exploring the cave for goods" + Fore.WHITE

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
			playerWarning = "A Cyclop has seen you!"
			enemyF()
			time.sleep(1.3)

		elif advanceAnswer == "no" or advanceAnswer == "n":
			emptyF()
			time.sleep(0.4)
			print(clearTop)
			print(caveArt)
			printSlow("Leaving cave.")
			time.sleep(0.2)
			print(clearTop)
			print(caveArt)
			printSlow("Leaving cave..")
			time.sleep(0.1)
			print(clearTop)
			print(caveArt)
			printSlow("Leaving cave...")
			time.sleep(0.2)
			print(clearTop)
			print(caveArt)
			printSlow("Leaving cave.")
			time.sleep(0.3)
			print(clearTop)

			run = False





	attkPlayer()
	updateBars()
	EnemyAttacksPlayer()


	if healthDisplay.count("+") < 1 and run == True:
		combatAnswer = input(Fore.RED + "Press ENTER to quit " + Fore.WHITE).lower()
	else:
		combatAnswer = input(Fore.BLUE + "Press ENTER to attack " + Fore.WHITE).lower()


	if combatAnswer != False:
		attkNpc()
		updateBars()
		PlayerAttacksEnemy()
	else:
		playerWarning = "You need to attack!"



