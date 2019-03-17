a=int(input("enter the number\n"))
b=int(input("enter the number\n"))
c=int(input("enter the number\n"))
if a>b:
	if a>c:
		print(f"{a} is greatest")
	elif c>a:
		print(f"{c} is greatest")
elif b>c:
	print(f"{b} is greatest")
else:
	print(f"{c} is greatest")