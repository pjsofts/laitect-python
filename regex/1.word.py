import re

text = "Call me at 123-456-7890 or 987-654-3210."
pattern = r"\b\d{3}-\d{3}-\d{4}\b"
groups = re.findall(pattern, text)
print(groups)
