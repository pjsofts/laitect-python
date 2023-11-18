words = ["salam", "hi", "hello", "hi", "yes","salam", "no"]
words2 = []
for word in words:
    if word not in words2:
        words2.append(word)
print(words2)