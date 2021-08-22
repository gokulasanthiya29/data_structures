def sum_of_digits(n):
    if n in range(0,10):
        return n
    else:
        n = (n%10) + sum_of_digits(n//10)
        return n

n = int(input())
print(sum_of_digits(n))