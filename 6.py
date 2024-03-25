# Handling division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Handling file not found error
try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
