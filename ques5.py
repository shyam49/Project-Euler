from fractions import gcd 
def lcm(p,q):
	return (p*q)/gcd(p,q)

n=1
for i in range(2,21):
	n=lcm(n,i)	
print n
