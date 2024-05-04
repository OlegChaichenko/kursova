def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return (gcd, x, y)

def mod_inverse(a, p):
    gcd, x, y = extended_gcd(a, p)
    if gcd != 1:
        return None  # Modular inverse does not exist
    else:
        return x % p

def fast_power(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result


p = 47
a = 11
inverse1 = mod_inverse(a, p)
print('A)')
print("Method (i): Using Extended Euclidean Algorithm")
print("Inverse of", a, "mod", p, "is:", inverse1)
inverse2 = fast_power(a, p - 2, p)
print("\nMethod (ii): Using Fast Power Algorithm and Fermat's Little Theorem")
print("Inverse of", a, "mod", p, "is:", inverse2)


p = 587
a = 345
inverse1 = mod_inverse(a, p)
print('B)')
print("Method (i): Using Extended Euclidean Algorithm")
print("Inverse of", a, "mod", p, "is:", inverse1)
inverse2 = fast_power(a, p - 2, p)
print("\nMethod (ii): Using Fast Power Algorithm and Fermat's Little Theorem")
print("Inverse of", a, "mod", p, "is:", inverse2)

p = 104801
a = 78467
inverse1 = mod_inverse(a, p)
print('C)')
print("Method (i): Using Extended Euclidean Algorithm")
print("Inverse of", a, "mod", p, "is:", inverse1)
inverse2 = fast_power(a, p - 2, p)
print("\nMethod (ii): Using Fast Power Algorithm and Fermat's Little Theorem")
print("Inverse of", a, "mod", p, "is:", inverse2)