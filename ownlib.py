import os, sys, subprocess, time
from sys import version_info


def py2py3():
	if version_info.major == 3:
        input = raw_input
    elif version_info.major == 2:
        raw_input = input
    else:
        print("Unknown python version - input function not safe")

def openFile(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

def lockMachine():
	os.system("osascript -e 'tell application \"System Events\" to keystroke \"q\" using {command down,control down}'")

def printSlow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.08)

clearTop = chr(27) + "[2J"