# numbers = [12,3,42,33,35,36]
# numbers2 = []
# for number in numbers:
#     if number %2 ==0:
#         numbers2.append(number)
# print(numbers2)

def even_numbers(numbers):
    numbers2 = []
    for number in numbers:
        if number %2 ==0:
            numbers2.append(number)
    return numbers2

print(even_numbers([1,2,3,4]))
print(even_numbers([10,20,30,40]))