from parse import parse
from converter import convert

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])
print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Child height is not suitable for this ride.")
else:
    print("Child height is suitable for this ride.")