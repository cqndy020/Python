import re

p = re.compile('\d')
x = "Tomorrow, July 27 is my father's birthday."

#findall() returns a list of single digits in x
result = p.findall(x)

print(result) #output: ['2', '7']

p1 = re.search('\d{2}',x)
print(p1)#output: <re.Match object; span=(15, 17), match='27'>