# > **Write a nested function:**
# > - Outer function takes a number
# > - Inner function checks if it's prime
# > - Outer function prints first N prime numbers

def find_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2,num):
            if num%i == 0:
                return False
        return True

    count = 0
    num = 2
    primes = []
    while count < n:
        if is_prime(num):
            primes.append(num)
            count += 1
        num += 1
    print(f"First {n} prime numbers are: ")
    primes = " ".join(str(x) for x in primes)
    print(primes)
find_primes(5)
    