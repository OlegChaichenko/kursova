def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print('a)',gcd(291,252))
print("b)",gcd(16261, 85652))
print("c)",gcd(139024789, 93278890))
print("d)",gcd(16534528044, 8332745927))