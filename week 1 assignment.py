# WEEK 1 ASSIGNMENT BY ADARSH DUBEY
# Create lower triangular, upper triangular and pyramid containing the "*" character.

def lower_triangular(n):
    for i in range(1, n + 1):
        print("*" * i)
lower_triangular(5)

def upper_triangular(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)
upper_triangular(5)

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
pyramid(5)
