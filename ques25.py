def fib(n):
    a = 1
    b = 0
    while n > 1:
        a, b = a+b, a
        n = n - 1
    return a
		
i=1
while True:
	a=fib(i)
	b=str(a)
	if len(b)==1000:
		print i
		break
	i+=1

