import re

s = "I like blue colour/ color."

#?u matches 0 or 1 character u 
matches = re.finditer(r'colou?r', s)

for match in matches:
    print(match)
    #output:
    #<re.Match object; span=(12, 18), match='colour'>
    #<re.Match object; span=(20, 25), match='color'>

#Another example 
html = '<button type="submit" class="btn">Send</button>'
result = re.findall(r'".+?"', html)
print(result) 
#output: ['"submit"', '"btn"']