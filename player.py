### PLAYER ###
class player = 

# HP
player['HP'] = {}
player['HP']['health'] = 55
player['HP']['maxHealth'] = 55
player['HP']['healthDashes'] = 31
player['HP']['dashConvert'] = int(player['HP']['maxHealth']/player['HP']['healthDashes'])
player['HP']['currentDashes'] = int(player['HP']['health']/player['HP']['dashConvert'])

