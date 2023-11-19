word1 = "adamxq"
word2 = "madaxqw"
dic1 = {}
dic2 = {}
word1 = word1.replace(" ", "")
word2 = word2.replace(" ", "")
for letter in word1:
    if letter not in dic1:
        dic1[letter] = 1
    else:
        dic1[letter] += 1
print(dic1)
for letter in word2:
    dic2[letter] = dic2.get(letter, 0) + 1
print(dic2)

anagram = True
if len(dic1.keys()) != len(dic2.keys()):
    anagram = False
for letter, count in dic1.items():
    if letter in dic2:
        if count != dic2[letter]:
            anagram = False
    else:
        anagram = False
print(anagram)
