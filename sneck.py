
def move(num, currentCord):
	column, row=currentCord
	if num==6:
		column+=1
	elif num==4:
		column-=1
	elif num==2:
		row+=1
	elif num==8:
		row-=1
	else:
		return False
	return column,row

length=0 #Length of the snake
currentCords=[[0,0]]

# The map is a 10x10 2D list
mapCords=list()
for _ in range(10):
	mapCords.append(range(10))

import random
import time

currentDirection=6
spawn=[random.randInt(1,10),random.randInt(1,10)]
while True:
	currentCord=move(currentDirection,currentCords[-1])
	if currentCord!=False:

		#Check if tip is at the spawn
		if currentCord==spawn:
			length+=1
			currentCords.append(currentCord)
			spawn=[random.randInt(10),random.randInt(10)]
		else:
			del currentCords [0]
			currentCords.append(currentCord)
		time.sleep(1)
	else:
		break


