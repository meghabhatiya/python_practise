import random 
r=random.randint("rock,paper,scissors")

a=int(input("enter the number"))

a==p1:

p1 =	input("Player 1's turn:		\n").lower()
p2 =	input("Player 2's turn:		\n").lower()

if p1=="rock" or p1=="scissors" or p1=="paper":

	if p1==p2:
		print("its a tie..!!")

	if p1=="rock":
		if p2=="paper":
			print("p1 wins")
		elif p2=="scissors":
			print("p2 wins")
		else:
			print("something went wrong")

	if p1=="paper":
		if p2=="rock":
			print("p2 wins")
		elif p2=="scissors":
			print("p2 wins")
		else:
			print("something went wrong")

	if p1=="scissors":
		if p2=="rock":
			print("p1 wins")
		elif p2=="paper":
			print("p1 wins")
		else:
			print("something went wrong")

else:
	print("something went wrong")
