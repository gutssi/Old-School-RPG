import random

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
npcLevel = random.randint(1,3)

############################# ENEMY INFO #################################