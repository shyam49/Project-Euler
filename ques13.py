import sys
n=int(raw_input())
d=int(raw_input())
a=[]
for i in range(n):
	b=list(raw_input())
	b=[int(x) for x in b]
	a.append(b)
#print a
t=int(raw_input())
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
