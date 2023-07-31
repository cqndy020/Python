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

#More examples of sets:
#[\d\s] - a digit or a space character
#[\d_]  - a digit or an underscore


#Sets+Ranges
x = "example1234.com"

match = re.findall(r"[0-9]", x)
print(match)
#output: 
#['1', '2', '3', '4']