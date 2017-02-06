#c*c=a*a+b*b
#a+b+c=1000
for a in range(1,1000/3+1):
	for b in range(a+1,1000/2+1):
		c=1000-a-b
		if a*a+b*b==c*c:
			print a*b*c
