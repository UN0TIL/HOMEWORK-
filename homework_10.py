from keyword import kwlist
from string import punctuation


text = input()
contains = False
upp = False

for i in text:
    if i in punctuation and i != '_' or i == ' ' and i != '_':
        contains = True
        break
for i in text:
    if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        upp = True
        break

if text in kwlist:
    print(False)
elif text[0] in '0987654321':
    print(False)
elif text.isdigit():
    print(False)
elif contains:
    print(False)
elif upp:
    print(False)
else:
    print(True)