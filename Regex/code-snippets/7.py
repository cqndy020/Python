import re

s = "Python Python is easy"
#\1 references the (\w+) capturing group
new_s = re.sub(r"(\w+)\s+\1", r"\1", s)
print(new_s)