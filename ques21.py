def divisors(n):
	a=[]
	for i in range(1,n/2+1):
		if n%i==0:
			a.append(i)
	return sum(a)
	
x=[]
for i in xrange(1,10000):
	if i==divisors(divisors(i)) and divisors(i)!=i:
		x.append(divisors(i))
		x.append(i)
				
print sum(list(set(x)))
