list_1 = [1 , 2, 3, 5 , 6 ,"hi", "hello"]
list_2 = ["hi", 5 , 1 , "ali"]

list_3=[]

for i in list_1:
    if i in list_2:
        list_3.append(i)
print(list_3)
