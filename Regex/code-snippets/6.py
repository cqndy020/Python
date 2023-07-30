#Sets and Ranges

#Sets- []
import re

s = "A analyze or analyse"

matches = re.finditer(r"analy[sz]e", s)
for match in matches:
    print(match.group())
    #output:
    #analyze
    #analyse

