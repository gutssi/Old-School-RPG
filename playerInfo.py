import random
from colorama import Fore

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

