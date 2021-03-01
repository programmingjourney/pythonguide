import sys

#exceptions

try:
    x = int(sys.argv[1])
    k = 1 / x
except ZeroDivisionError:
    print("Division to 0 not allowed, please input again")
except IndexError:
    print("No argument")
except ValueError:
    print("Please specify an integer")

# recursion

# n! = 1 * 2 * .... * n
# 1 2 3 4 5 6 7
# 1! = 0! * 1
# 2! = 1! * 2
# 3! = 2! * 3
# 4! = 3! * 4

# n! = (n - 1)! * n
# 0! = 1
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def factorial_iterative(n):
    mul = 1
    for i in range(1, n + 1):
        mul *= i
    return mul

# 2 * 1 * 1
print(factorial(5), factorial_iterative(5))