def is_prime(num):
    if num <= 1:
        return "Not a Prime Number"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Not a Prime Number"
    return "Prime Number"

n = int(input("Enter a number: "))
print(is_prime(n))
