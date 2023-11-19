import re
text = "I have a cat. My cat is cute."
pattern= r"cat"
replace = "dog"

new_text = re.sub(pattern, replace, text)
print(new_text)
