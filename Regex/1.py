import re

p = re.compile('\d')
x = "Tomorrow, July 27 is my father's birthday."

#findall() returns a list of single digits in x
result = p.findall(x)

print(result) #output: ['2', '7']


