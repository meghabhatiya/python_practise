import random 
r=random.randint(1,10)

a=int(input("enter the number"))

if a==r:
	print("its equal")
elif a>r:
	print("its too high")
elif a<r:
	print("its too low")