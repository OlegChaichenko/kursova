def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def solve_congruence(a, b, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError('No solution exists')
    else:
        return (x * b) % m

def legendre_symbol(a, p):
    ls = pow(a, (p-1)//2, p)
    return ls

def solve_quadratic_congruence(a, p):
    solutions = []
    if legendre_symbol(a, p) == 1:
        for x in range(p):
            if (x**2) % p == a:
                solutions.append(x)
    if len(solutions)==0:
            return "Немає розв'язків"
    else:
            return solutions
def solve_polynomial_congruence(polynomial, p):
    solutions = []
    for x in range(p):
        value = sum(coeff * pow(x, power, p) % p for power, coeff in enumerate(polynomial[::-1])) % p
        if value == 0:
            solutions.append(x)
    return solutions

def chinese_remainder_theorem(a1, m1, a2, m2):
    _, inv1, _ = extended_gcd(m1, m2)
    return (a1 + m1 * ((a2 - a1) * inv1 % m2)) % (m1 * m2)


solution_a = solve_congruence(1, 23-17, 37)
print("Розв'язок рівняння a)x + 17 ≡ 23 (mod 37) : x ≡", solution_a)
solution_b = solve_congruence(1, 19-42, 51)
print("Розв'язок рівняння b)x + 42 ≡ 19 (mod 51) : x ≡", solution_b)
solution_c = solve_quadratic_congruence(3, 11)
print("Розв'язок рівняння c)x^2≡ 3 (mod 11) : x ≡", solution_c)
solution_d = solve_quadratic_congruence(2, 13)
print("Розв'язок рівняння d)x^2≡ 2 (mod 13) : x ≡", solution_d)
solution_e = solve_quadratic_congruence(1, 8)
print("Розв'язок рівняння e)x^2≡ 1 (mod 8) : x ≡", solution_e)
solutions_f = solve_polynomial_congruence([1, -1, 2, -2] , 11)
print("Розв'язок рівняння f)x^3 - x^2 + 2x - 2 ≡ 0 (mod 11) : x ≡", solutions_f)
solution_g = chinese_remainder_theorem(1, 5, 2, 7)
solutions_g = [solution_g + 35 * k for k in range(35) if solution_g + 35 * k <= 34]
print("Розв'язок рівняння g)x ≡ 1 (mod 5) and also x ≡ 2 (mod 7): x ≡", solutions_g)
