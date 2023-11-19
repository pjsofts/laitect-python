numbers2 = [1,4,7,8,20]
numbers1 = [2,3,5]
numbers3 = []
i = 0
j = 0 
while i < len(numbers1) and j < len(numbers2):
    if numbers1[i] < numbers2[j]:
        numbers3.append(numbers1[i])
        i+=1
    else:
        numbers3.append(numbers2[j])
        j+=1
while i < len(numbers1):
    numbers3.append(numbers1[i])
    i+=1
while j < len(numbers2):
    numbers3.append(numbers2[j])
    j+=1
print(numbers3)