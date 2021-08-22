def fib(n, memo={}):
    if n<=2:
        return 1

    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        return memo[n]


print(fib(2))
print(fib(6))
print(fib(10))
print(fib(30))
print(fib(20))
print(fib(35))
print(fib(40)) # starts to takes long time
print(fib(45))
print(fib(50)) # starts to run forever



