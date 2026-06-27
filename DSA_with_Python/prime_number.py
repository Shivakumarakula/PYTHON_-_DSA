# def primeNumber(n):
#     count=0
#     if n>2:
#         for i in range(2,n+1):
#             if n%i==0:
#                 count+=1
        
#         if count==2:
#             print(n, " is prime number")
#         else:
#              print(n, " is not a prime number")
#     else:
#         print("enter number greater than 1 and 0")
        
# primeNumber(11)

def primeNumber(n):
    if n <= 1:              # 1 or below are not prime
        return False
    if n == 2:              # 2 is the only even prime
        return True
    if n % 2 == 0:          # any other even number is not prime
        return False

    # check only odd numbers up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:      # if divisible, not prime
            return False
    return True             # no divisors found → prime



print(primeNumber(3))