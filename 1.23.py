def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def chinese_remainder_theorem(a1, m1, a2, m2):
    _, inv1, _ = extended_gcd(m1, m2)
    return (a1 + m1 * ((a2 - a1) * inv1 % m2)) % (m1 * m2)
def chinese_remainder_theorem_for3(a1, m1, a2, m2, a3, m3):
    _, inv1, _ = extended_gcd(m1, m2)
    _, inv2, _ = extended_gcd(m1 * m2, m3)
    x = (a1 + m1 * ((a2 - a1) * inv1 % m2) + m1 * m2 * ((a3 - a1 - m1 * ((a2 - a1) * inv1 % m2)) * inv2 % m3)) % (m1 * m2 * m3)
    return x

solution_a = chinese_remainder_theorem(3, 7, 4, 9)
print("Розв'язок рівняння a)x ≡ 3 (mod 7) and also x ≡ 4 (mod 9): x ≡", solution_a)

solution_b = chinese_remainder_theorem(13, 71, 41, 97)
print("Розв'язок рівняння b)x ≡ 13 (mod 71) and also x ≡ 41 (mod 97): x ≡", solution_b)

solution_c = chinese_remainder_theorem_for3(4, 7, 5, 8, 11, 15)
print("Розв'язок рівняння c)x ≡ 4 (mod 7) , x ≡ 5 (mod 8) and also x ≡ 11 (mod 15) : x ≡", solution_c )