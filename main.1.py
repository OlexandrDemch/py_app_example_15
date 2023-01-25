a = int(input("Введіть значення a : "))
b = int(input("Введіть значення b : "))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n + 1):
        if n % i == 0 and n != i:
            return False
    return True
for k in range(a,b):
    if a > b:
        print ("a не може бути більшим за b")
    if is_prime(k):
        print(k)