from NumberTests import isPrime
from NumberTests import getFactors

def main():
     number = 13195
     factors = getFactors(number)
     print(factors)

     for f in factors:
         if isPrime(f):
             print(f)

if __name__ == '__main__':
  main()