
for i in range(1,20):
	if i == 4 or i == 13:
		print(f"{i} is unlucky no.")
	elif i%2==0:
		print(f"{i} even number")
	elif i%2==1:
		print(f"{i} its odd number")
	else:
		print("Something went wrong...!!")