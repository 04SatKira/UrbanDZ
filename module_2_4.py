numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(numbers [1], len(numbers) + 1):
    primes_flag = True
    for j in range (2, i+1):
        if i % j == 0 and i != j and i != 2:
            primes_flag = False
            break
    if primes_flag:
        primes.append (i)
    else:
        not_primes.append (i)   
print (primes)
print (not_primes)

          
          