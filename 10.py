# Debugging with print statements
def divide(x, y):
    result = x / y
    print("Result:", result)
    return result

divide(10, 2)

# Testing with assert statements
def square(x):
    return x * x

assert square(2) == 4
assert square(3) == 9
