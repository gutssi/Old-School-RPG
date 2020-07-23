player = {}
player['location'] = {'Xaxis' : 0, 'Yaxis' : 0}
player['HP'] = 200

print("Enter the value of row : ")
X=int(input())

print("Enter the value of column : ")
Y=int(input())
'''
a=[[0 for row in range(0,x)] for col in range(0,y)]

print("Enter elements of first matrix : ")
z = input('>')
for i in range(y):
         for j in range(x):
             a[i][j] = z

print("Elements of First matrix is : " )
for row in a:
     print(row)
'''
print('###########################')

a=[[ '_' for row in range(0,X)] for col in range(0,Y)]

def map():
	print('#' * X * 5)
	for row in a:
		print(row)
	print('#' * X * 5)

def resetmap():
	global a
	a=[[ '_' for row in range(0,X)] for col in range(0,Y)]

##############MOVEMENT############################
def position(i, j):
	resetmap()
	a[i-1][j-1] = "X"
	player['location']['Xaxis'] = i
	player['location']['Yaxis'] = j
	print("te afli la coord x: {0} si y: {1}".format(i,j))



def move_up():
		x = player['location']['Xaxis']
		y = player['location']['Yaxis'] 
		if x > 1:
			position(x-1, y)
		else:
			print("you cant go up")	

def move_down():
		x = player['location']['Xaxis']
		y = player['location']['Yaxis']
		if x < Y:
			position(x+1, y)
			print(x)
		else:
			print("you cant go down")
			print(x)
		
def move_right():
		x = player['location']['Xaxis']
		y = player['location']['Yaxis']
		if y < X:
			position(x, y+1)
		else:
			print("you cant go right")
		
def move_left():
		x = player['location']['Xaxis']
		y = player['location']['Yaxis'] 
		if y > 1:
			position(x, y-1)
		else:
			print("you cant go left")
		
#starting position 
#position(1,1)

# position max
#position(y,x)

########################################

position(1,1), map() #starting point

print(player["HP"])
print(player)




while player['HP'] > 0:
	answer = input('where do you want to go?up, down, right or left?')
	if answer == "up":
		move_up(), map()
	elif answer == "down":
		move_down(), map()
	elif answer == "right":
		move_right(), map()
	elif answer == "left":
		move_left(), map()
else:
	print("you died")

