import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = "World"  

print(f"Hello, {name}! Welcome to the minimal Python app.")
