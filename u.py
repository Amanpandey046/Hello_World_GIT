x = int(input("Enter the Number :"))

for i in range(x+1):
	for j in range(x,i,-1):
		print("*",end = " ")
	print()
