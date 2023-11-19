list=["hi","ali","chitsaz","ali","rasoul"]

for i  in range(len(list))  :
    for j in range(i,len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)        