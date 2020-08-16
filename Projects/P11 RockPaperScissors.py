from random import randint
from time import sleep

choices = ["Paper","Scissor","Rock"]

p1win = False
p2win = False

while p1win != True and p2win != True:
	#Choices
	print("Choose \t\tRock(1)\t\tPaper(2)\t\tScissor(3)")
	p1choice = int(input(": "))
	p2choice = randint(1,3)
	p1choice_name = choices[p1choice-1]
	p2choice_name = choices[p2choice-1]
	print(f"\n\nYou Chose {p1choice_name}")
	sleep(1)
	print(f"Opponent Chose {p2choice_name}\n\n")
	sleep(1)
	
	
	#Conditions
	if abs(p1choice - p2choice)  == 1:
		if p1choice > p2choice: 
			p1win = True
		else:
			p2win = True
			
	elif p1choice == p2choice:
		print("\nSince You both chose the Same, its a Draw! Lets try that again.\n\n")
		
	else:
		if p1choice < p2choice:
			p1win = True
		else:
			p2win = True


#Final Result
print("\n"*5)
if p1win == True:
	print(f"Since You chose {p1choice_name} and Opponent chose {p2choice_name}, You Win!")
else:
	print(f"Since Opponent chose {p2choice_name} and You chose {p1choice_name}, You Lose!")

