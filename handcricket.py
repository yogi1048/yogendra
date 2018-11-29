print("Welcome to Hand Cricket Game")
import random
a=int(input("enter value for the toss "))
u=random.randint(1,10)
print(u)

p=True

if((a+u)%2==0):
	print("player start playing")
else:
	print("computer start playing")
	p = False
counter=0

computer=0
score=0
while True:
	if counter==2:
		break
	if(p):
		while True:
			c=int(input("enter value : "))
			r=random.randint(1,6)
			score=score+c
			print(" player score is",score)
			print("computer hits",r)
			if(computer!=0):
					if(score>computer):
						print("player wins",score)
						exit()
			if(c==r):
				print("player stops playing")

				score=score-c
				print(score)
				p=False
				counter=counter+1
				break	
				
				

			
	else:
		while True:
			r1=random.randint(1,6)
			a1=int(input("enter value"))
			computer=computer+r1
			print("computer hits",r1)
			print("computer score is",computer)
			print("player hits",a1)
			if(score!=0):
					if(computer>score):
						print("computer wins",computer)
						exit()

			if(r1==a1):
				print("computer stops playing")
				computer=computer-r1
				print(computer)
				p=True
				counter=counter+1
				break
				

	
if(score>computer):
	print("player wins the game",score)
elif(computer>score):
	print("computer wins the game",computer)
else:
	print("it is a tie")		
		
		
	
		