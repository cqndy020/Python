import re

s = "Python Python is easy"
#\1 references the (\w+) capturing group
new_s = re.sub(r"(\w+)\s+\1", r"\1", s)
print(new_s)

#using lookahead syntax->>  ?=
x = "I am 5 feet and 11 inches tall."
matches = re.finditer(r"\d+(?=\s*feet)", x)
for match in matches:
    print(match.group())
    #output: 5

y = "I love apple pie, but not apple sauce."
matches = re.findall(r"\w+(?=[,.])", y)
for match in matches:
    print(match)
    #output: pie\nsauce