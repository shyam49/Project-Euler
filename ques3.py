def primes(n):
    prime = []
    i = 2
    while i*i <= n:
        while (n % i) == 0:
            prime.append(i) 
            n /= i
        i += 1
    if n > 1:
       prime.append(n)
    return prime

print max(primes(600851475143))
