import re

s = '2023'
pattern = '\d{4}'
result = re.fullmatch(pattern, s)
print(result) #output: <re.Match object; span=(0, 4), match='2023'>

x = 'Today is 28 July 2023'
result = re.fullmatch(pattern, x)
print(result) #output: None