from ownlib import clearTop
from colorama import Fore
import time
from playerInfo import *
from enemyInfo import *
from art import *

playerWarning = " Warning message"


def playerBox():
    print(" ")
    print(playerWarning)
    print("+" + 47 * '-' + "+")
    print(" ||" + Fore.RED + healthDisplay + remainingDisplay + Fore.WHITE + "|| " + Fore.RED + "HP " + str(health) + "/" + str(maxHealth) + Fore.WHITE)
    print(" ||" + Fore.BLUE + xpDisplay + remainingXpDisplay + Fore.WHITE + "|| " + Fore.BLUE + "XP " + str(xp) + "/" + str(maxxp) + Fore.WHITE)
    print("+" + 47 * '-' + "+")



def enemyBox():
    print(clearTop)
    print(cyclop)
    print(cyclop + " \n ||" + EhealthDisplay + str(EremainingDisplay) + "|| ")
    print("          " + Fore.RED + "Level " + str(npcLevel) + " " + "Cyclop" + Fore.WHITE)
    print(" ")


def frame():
    playerBox()


def main():
    frame()

    
if __name__ == "__main__":
    main()
