#using negative lookahead => ?!
import re

s = 'I am 5 feet and 11 inches tall'
matches = re.finditer(r"\d+(?!\s*feet)",s)
for match in matches:
    print(match.group())
    #output: 11