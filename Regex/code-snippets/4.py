import re

ph_no = '+(95)987-654-321'
match = re.findall('\D', ph_no)

for x in match:
    print(x)
#output: + ( ) - -


#using sub() function
result = re.sub('\D', '', ph_no)
print(result)
#output: 95987654321