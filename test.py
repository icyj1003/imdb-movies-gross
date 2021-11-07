import re

text = 'November 6, 2015 (Vietnam)'
s = text.split(',')[1]
s = re.sub(r'[^0-9]', '', s)
print(s)
