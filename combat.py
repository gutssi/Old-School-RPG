
import random
import curses
import os


playerAtk = 40
plaeryAtkMax = 200
playerAtkMin = 1
#####
health = 200

playerDef = 10
playerMaxDef = 200
playerMinDef = 10
playerAtkMod = 1
playerDefMod = 2

npcHealth = 200
npcMaxHealth = 200
npcMinHealth = 1

npcAtk = 50
npcDef = 10
npcAtkMod = 1
npcDefMod = 1

battleOutput = 0

##########
health = 200
maxHealth = 200
minHealth = 1
healthDashes = 20
#########






def npcAttacks():
	global health, playerDef, playerDefMod, npcAtkMod
	global npcAtk

	health = health - (npcAtk - (playerDef * playerDefMod))


def playerAttacks():
	global npcHealth, playerAtk, npcDef, npcDefMod

	npcHealth = npcHealth - (playerAtk - (npcDef * npcDefMod))








npcAttacks()
print("My Health: " + str(health))
playerAttacks()
print("NPC Health: " + str(npcHealth))
npcAttacks()
print("My Health: " + str(health))
playerAttacks()
print("NPC Health: " + str(npcHealth))
npcAttacks()
print("My Health: " + str(health))
playerAttacks()
print("NPC Health: " + str(npcHealth))
npcAttacks()
print("My Health: " + str(health))
playerAttacks()
print("NPC Health: " + str(npcHealth))



