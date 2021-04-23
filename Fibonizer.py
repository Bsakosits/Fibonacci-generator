import math
def Fibonizer(n):
	a=0
	b=1
	counter=1
	for i in range(0, n):
		#n decides what fibbioli u wanna go to
		#if n>10000000000000000:
			#"Achievement Earned: Computer Explosion"
		temp=a+b
		a=b
		b=temp
		print("Fibonacceroni number ", counter, " is ", a)
		print("And the local ratio at ", counter, " is ", b/a)
		counter+=1