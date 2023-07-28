import re

ph_no = '+(95)987-654-321'
match = re.findall(r'\D', ph_no)

for x in match:
    print(x)
#output: + ( ) - -


#using sub() function
result = re.sub(r'\D', '', ph_no)
print(result)
#output: 95987654321

#using word boundary
s = 'I eat three meals in a day: breakfast, lunch, and dinner.'
match = re.search(r'\blunch\b', s)
print(match.group())
#output: lunch