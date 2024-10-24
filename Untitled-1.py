def prime_factors(number):
    
    a = 2
    Factors = []
    while a*a <= number:
        if number % a == 0:
            Factors.append(a)
            number //= a
        elif number % a != 0:
            a += 1
    if number > 1:
            Factors.append(number)
    return(Factors)

number = int(input())
A = prime_factors(number)

print(*A, sep = ' * ')
