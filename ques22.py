def score(name):
	x=sum(ord(i)-64 for i in name)
	return x

f=open('p022_names.txt','r')
a=f.read()
b=a.replace('"','')
c=b.split(',')
c.sort()
x=0
for i in range(len(c)):
	 x+=(score(c[i])*(i+1))
print x
