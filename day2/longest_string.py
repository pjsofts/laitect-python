words = [  'this',  'is',  'a',  'list',  'of',  'words'  ]

longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)