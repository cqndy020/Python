#using lookbehind => ?<=
import re

s = 'This ticket costs $15 for 1 person.'
matches = re.finditer(r"(?<=\$)\d+",s)
for match in matches:
    print(match.group())
    #output: 15

#using Negative lookbehind => ?<!

matches = re.finditer(r"(?<!\$)\d+",s)
for match in matches:
    print(match.group())
    #output: 1