import re

#Example 1
s = "The world's fastest land animal, the cheetah, can accelerate from 0 to 60 mph in just 3 seconds."
result = re.search('\d', s)

print(result.group()) #match string      - > 0 (the first digit in s)
print(result.start()) #starting position - > 66
print(result.end())   #ending position   - > 67
print(result.span())  #Position          - > (66, 67)

print('\n')

#Example 2
x = "The circumference of the Earth at the equator is about 40,075 kilometers."
result = re.search('\d', x)

print(result.group()) #match string      - > 4
print(result.start()) #starting position - > 55
print(result.end())   #ending position   - > 56
print(result.span())  #Position          - > (55, 56)
