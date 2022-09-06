x = int(input("Enter the Number :"))
a = 0
b = 1
sum = 0
count = 1
print("The Fibonacci series of ",x,"is :")
while(count<=x):
	print(sum,end= " ")
	count += 1
	a = b
	b = sum
	sum = (a+b)
