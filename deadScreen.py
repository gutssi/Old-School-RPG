import time
from colorama import Fore
from art import deadArt
from ownlib import printSlow, clearTop

def deadScreen():
    for i in range(6):
        print(clearTop)
        print(deadArt)
        time.sleep(0.1)
        print(clearTop)
        print(Fore.RED + deadArt + Fore.WHITE)
        time.sleep(0.1)

    print(clearTop)
    printSlow(Fore.RED + "You Died!\n" + Fore.WHITE)
    exit()



def main():
    deadScreen()

if __name__ == "__main__":
    main()
