from NumberTests import isPrime
from NumberTests import getFactors

def isPrime(p):
  """Returns boolean (True/False) if the value given is prime."""
  if p == 1:
    return False
  if p == 2:
    return True
  if p % 2 == 0:
    return False
  for i in range(3, int(p**0.5) + 1, 2):
    if p % i == 0:
      return False
    
  return True

primes = []
current = 2
target = 10001

while len(primes) < target:
  if isPrime(current):
    primes.append(current)

  current += 1 if current == 2 else 2 

print ("The 10001st prime number is:", (primes[-1]))