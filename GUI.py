from ownlib import clearTop
from colorama import Fore
import time
from playerInfo import *
from enemyInfo import *
from art import *

playerWarning = " Warning message"


def playerBox():
    print(playerWarning)
    print("+" + 47 * '\033[1;37;40m-' + "+")
    print(" ||" + healthDisplay + remainingDisplay + "\033[1;37;40m|| " + Fore.RED + "HP " + str(health) + "/" + str(maxHealth) + Fore.WHITE)
    print(" ||" + xpDisplay + str(remainingXpDisplay) + "\033[1;37;40m|| " + Fore.BLUE + "XP " + str(xp) + "/" + str(maxxp) + Fore.WHITE)
    print("+" + 47 * '\033[1;37;40m-' + "+")



def enemyBox():
    print(clearTop)
    print(cyclop)
    print(cyclop + " \n ||" + EhealthDisplay + str(EremainingDisplay) + "\033[1;37;40m|| ")
    print("          " + Fore.RED + "Level " + str(npcLevel) + " " + "Cyclop" + Fore.WHITE)
    print(" ")


def frame():
    playerBox()


def main():
    frame()

    
if __name__ == "__main__":
    main()
