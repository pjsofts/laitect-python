str = "ali javad ali hello chitsaz chitsaz chitsaz chitsaz chitsaz chitsaz chitsaz chitsaz chitsaz rasool rasool"
count = {}
for word in str.split(" "):
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)
