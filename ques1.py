a=[2*i for i in range(1,334)]
for i in range(1,000):
	a.append(4*i)
print sum(list(set(a)))

