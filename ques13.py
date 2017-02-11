import sys
n=int(raw_input()) #number of elements
d=int(raw_input()) #number of digits in each element
a=[]
for i in range(n):
	b=list(raw_input()) #element
	b=[int(x) for x in b]
	a.append(b)
t=int(raw_input()) #first t digits of the sum
ans=[]
sum=0
for j in range(d-1,-1,-1):
	for k in range(n):
		sum+=a[k][j]
#		print a[k][j]
#		print sum
	if j!=0:
		ans.insert(0,sum%10)	
		sum=sum/10
#		print sum
		
	else:
		y=list(str(sum))
		y=[int(x) for x in y]
		for i in range(len(y)-1,-1,-1):
			ans.insert(0,y[i])

for i in range(t):
	sys.stdout.write(str(ans[i]))
