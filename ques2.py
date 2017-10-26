a=[1,2]
for i in range(2,10000):
	if a[i-1]+a[i-2]<400000:
		a.append(a[i-1]+a[i-2])
	else:
		break
sum=0
for i in range(0,len(a)):
	if a[i]%2==0:
		sum+=a[i]
		
print sum
