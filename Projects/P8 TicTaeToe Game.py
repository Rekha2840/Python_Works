
from time import sleep
from random import randint
box = [["-"]*3 for ctr in range(3)]
p2_win, p1_win = False, False
draw = False
choices = []

def sp(x=1):
	for ctr in range(x):
		print("\n")
		
def get_box(box):
	for row in range(3):
		print("|",end="")
		for col in range(3):
			print(" ",box[row][col]," ",end="")
			if col == 0 or col == 1:
				print("|",end="")
		print("|",end="")
		sp()
			
def add_box(pos,type="X"):
	global box
	row = int(pos / 3) 
	col = int(pos % 3)
	box[row][col] = str(type)
	
def check(box):
	def breaker(arr):
		global p2_win, p1_win 
		for iter_list in arr:
			if iter_list == ["X"]*3:
				p1_win = True
			elif iter_list == ["O"]*3:
				p2_win = True		
			
	#Across
	breaker(box)	
	
	#Down
	down = [['-']*3 for i in range(3)]
	for x in range(3):
		for y in range(3):
			down[x][y] = box[y][x]
	breaker(down)		
	
	#Diagonal				
	line = [['-']*3 for i in range(2)]
	ind1,ind2 = 0,2
	for x in range(2):
		for y in range(3):
			if x == 0:
				line[x][y] = box[ind1][ind1]
				ind1+=1
			else:
				if ind1 == 3:
					ind1 = 0
				line[x][y] = box[ind1][ind2]	
				ind1 += 1
				ind2 -= 1
	breaker(line)
	
	#Filled
	count = 0
	global draw
	for x in range(3):
		for y in range(3):
			if box[x][y] == "-":
				count += 1
	if count == 0:
		draw = True
		
def get_pos():
	pos = randint(1,9)
	global choices 
	if not pos in choices: #tile unfilled
		choices.append(pos)
		return pos
	else: #tile filled
		return 0		


sp(2)
ctr = 0
sleep(0.5)
print("Game Started!")
sleep(0.6)
sp(2)
get_box(box)	
sp(2)


while p1_win == False and p2_win == False and draw == False:	
	while True:
		pos = get_pos()
		if pos != 0:
			break
			
	if ctr % 2 ==0:
		print("Player1 Ticked "+str(pos))
		add_box(pos-1,"X")
	else:
		print("Player2 Ticked "+str(pos))	
		add_box(pos-1,"O")	
		
	
	get_box(box)
	check(box)
	sleep(1.5)
	ctr+=1
	sp(3)
	
sp(2)
if p1_win:
	print("Player 1 Won!")
elif p2_win:
	print("Player 2 Won!")
else:
	print("It Was a draw! ")
	




										
