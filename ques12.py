def num_divisors(n):
    if n % 2 == 0: n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors

 
def find_triangular_index(factor_limit):
    n = 1
    l, r = num_divisors(n), num_divisors(n+1)
    while l * r < 500:
        n += 1
        l, r = r, num_divisors(n+1)
    return n
 
index = find_triangular_index(500)
triangle = (index * (index + 1)) / 2

 
print triangle
print num_divisors(30)
