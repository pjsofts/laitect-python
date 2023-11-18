numbers = [1,3,4,7,9,44]
for number in numbers:
    print(number**2)

squares = [number**2 for number in numbers]
print(squares)