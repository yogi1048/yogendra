import random 
while True:
	a=input("Enter r to roll a dice:")
	if(a=="r"):
		godson=random.randint(1,6)
		print(godson)
	else:
		print("Bye")
		break
