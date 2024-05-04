def bezout_recursive(a, b):
    if not b:
        return (1, 0, a)
    y, x, g = bezout_recursive(b, a % b)
    return (x, y - (a // b) * x, g)


print('a)',bezout_recursive(291,252))
print("b)",bezout_recursive(16261, 85652))
print("c)",bezout_recursive(139024789, 93278890))
print("d)",bezout_recursive(16534528044, 8332745927))