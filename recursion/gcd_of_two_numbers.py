# As per Euclidean algorithm
def gcd(a,b):
    assert int(a) == a and int(b) == b, "The number should be an integer."

    if a < 0:
        a = -1 * a

    if b < 0:
        b = -1 * b

    if b == 0:
        return a

    else:
        return gcd( b, a % b )


a = int(input())
b = int(input())
print(gcd(a, b))


