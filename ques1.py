a=[3*i for i in range(1,334)]
for i in range(1,200):
	a.append(5*i)
print sum(list(set(a)))

