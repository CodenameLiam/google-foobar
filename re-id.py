# Return whether a number is prime by ensuring it is not already in the set of existing primes, 
# or divisible by any of the existing primes
def isPrime(primeChecker, primes):
    for prime in primes:
        if not (primeChecker == prime or primeChecker % prime):
            return False
    primes.add(primeChecker)
    return True 

# Generate string of primes with a length greater than n
def genPrimes(n):
    primes = set([2])
    primeString = ''
    primeChecker, counter = 2, 0
    while True:
        if isPrime(primeChecker, primes):
            counter += 1
            primeString += str(primeChecker)
            if len(primeString) >= n:
                return primeString
        primeChecker += 1

def solution(i):
    # Generate prime string up to i (+5 for the next 5 digits)
    primeString = genPrimes(i+5)
    # Return the minion's new ID number
    return(primeString[i:i+5])


print(solution(3))