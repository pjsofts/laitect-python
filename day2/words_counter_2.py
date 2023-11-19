str = "ali javad ali hello chitsaz chitsaz chitsaz chitsaz chitsaz chitsaz chitsaz chitsaz chitsaz rasool rasool"
count = {}
for word in str.split(" "):
    count[word]= count.get(word,0) + 1

print(count)
