def square_and_multiply(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result


result_a = square_and_multiply(17, 183, 256)
print("17^183 (mod 256) =", result_a)
result_b = square_and_multiply(2, 477, 1000)
print("2^477 (mod 1000) =", result_b)
result_c = square_and_multiply(11, 507, 1237)
print("2^477 (mod 1000) =", result_c)