from NumberTests import isPrime
from NumberTests import getFactors

def isPrime(p):
  """Returns boolean (True/False) if the value given is prime."""
  if p <= 1:
    return False
  if p == 2:
    return True
  for i in range(3, int(p**0.5) + 1, 2):
    if p % i == 0:
      return False
    
  return True

def primesunder(limit):
    primes = []
    for num in range(2, limit):
        if isPrime(num):
            primes.append(num)
    return primes

limit = 2000000
primes = primesunder(limit)

sumofprimes = sum(primes)

print(f"Number of primes below {limit}: {len(primes)}")
print(f"Sum of all primes below {limit}: {sumofprimes}")