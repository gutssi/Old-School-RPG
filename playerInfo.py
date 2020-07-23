import random
from colorama import Fore

############################# PLAYER INFO #################################

class player(object):

    def __init__(self, name, health, maxHealth, healthDashes, dashConvert, currentDashes, remainingHealth, atkMin, atkMax, atkMod, atk, deff, xp, maxxp, xpDashes, dashConvertxp, currentDashesxp, xpRemain, xpDisplay, remainingXpDisplay):
        self.name = "Test name"
        self.health = 100
        self.maxHealth = 100
        self.healthDashes = 31
        self.dashConvert = int(self.maxHealth/self.healthDashes)
        self.currentDashes = int(self.health/self.dashConvert)
        self.remainingHealth = self.healthDashes - self.currentDashes
        self.healthDisplay = '\033[1;31;40m+' * self.currentDashes
        self.remainingDisplay = " " * self.remainingHealth
        self.atkMin = 55
        self.atkMax = 65
        self.atkMod = 1
        self.atk = random.randint(atkMin, atkMax)
        self.deff = 10
        self.xp = 0
        self.maxxp = 100
        self.xpDashes = 31
        self.dashConvertxp = int(self.maxxp/self.xpDashes)
        self.currentDashesxp = int(self.xp/self.dashConvertxp)
        self.xpRemain = xpDashes - currentDashesxp
        self.xpDisplay = Fore.BLUE + "=" * currentDashesxp
        self.remainingXpDisplay = ' ' * xpRemain


print()