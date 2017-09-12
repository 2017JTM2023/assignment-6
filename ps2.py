###### this is the second .py file ###########

####### write your code here ##########
#the game board

print("Welcome to the Game")
print("Choose player 1 or player 2")
gameboard= [0,1,2,
	    3,4,5,
	    6,7,8]

def showboard():
	print gameboard[0],'|',gameboard[1],'|',gameboard[2]
	print "----------"
	print gameboard[3],'|',gameboard[4],'|',gameboard[5]
	print "----------"
	print gameboard[6],'|',gameboard[7],'|',gameboard[8]


showboard()

while True:
	position=input("select a spot:")
	position = int (position)

