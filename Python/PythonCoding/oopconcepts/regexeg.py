#27/04/2026

import re

'''
txt = input('enter a text')
bpat = input('enter begining patter')
epat = input('enter endign pattern')
bpat = '^' +bpat
epat = epat + '$'


if re.search(pattern=bpat, string=txt):
    print('begining pattern available')
else:
    print('begining not available')
'''

# digit matching
'''
mbno = input('enter a text ')
pat =  #r"" '[0-9]'
if re.fullmatch(pattern=pat, string=mbno):
    print('only digits')
else:
    print('other chars')
'''

'''
#username

un = input('enter a UN ')
pat = r"^[a-z_]{8,}$"

if re.match(pattern=pat, string=un):
    print('valid')
else:
    print('invalid')
'''
'''
#emailid
emailadd = input('enain ')
pat=r"^[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"
if re.match(pattern=pat, string=emailadd):
    print('valid')
else:
    print('invalid')
'''
'''
#pwd
pwdtxt=input('pwd ')
pat = r"^(?=.*[A-Z])(?=[a-z])(?=.*[0-9])(?=.*[@_-]).{8,}$"
if re.match(pattern=pat, string=pwdtxt):
    print('valid')
else:
    print('invalid')
'''
txt = input('txt ')
pat = r"\s+"
#print(re.sub(pattern=pat, string=txt, repl='*'))
print(re.split(pattern=pat, string=txt))

