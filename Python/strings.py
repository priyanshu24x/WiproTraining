Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1 = 'hello'
s1
'hello'
type(s1)
<class 'str'>
s1.capitalize()
'Hello'
s1.upper()
'HELLO'
s1.lower()
'hello'
s1='hELLO'
s1.casefold()
'hello'
s1='HellO'
s1.casefold()
'hello'
s1.count(l)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s1.count(l)
NameError: name 'l' is not defined
s1.count('l')
2
s1.count('h')
0
s1.endswith('o')
False
s1.endswith('O')
True
s1.find('l')
2
s1.find('O')
4
s1.find('0')
-1
s1.index('O')
4
s1.index('0')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s1.index('0')
ValueError: substring not found
s1.istitle(s1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s1.istitle(s1)
TypeError: str.istitle() takes no arguments (1 given)
s1.isalpha()
True
is.istitle()
SyntaxError: invalid syntax
s1.istitle()
False
s1.isdigit()
False
s1.join(' world')
' HellOwHellOoHellOrHellOlHellOd'
s1.replace('l','L')
'HeLLO'
s1
'HellO'
s1='Hello there how are you'
s1
'Hello there how are you'
s1.split(' ')
['Hello', 'there', 'how', 'are', 'you']
KeyboardInterrupt
s1='hello there - how are you'
s1.split('-')
['hello there ', ' how are you']
s1
'hello there - how are you'
s1.swapcase()
'HELLO THERE - HOW ARE YOU'
s1='hello there!!'
len(s1)
13
s1='hello there !!!'
len(s1)
15
s1[1]
'e'
s1[0]
'h'
s1[10]
'e'
s1[14]
'!'
s1[-3]
'!'
s1[-5]
'e'
s1[-6]
'r'

s1[0:5]
'hello'
s1[0:10]
'hello ther'
s1[0:]
'hello there !!!'
s1[]
SyntaxError: invalid syntax
s1[:]
'hello there !!!'
s1[2:12:2]
'lotee'
s1[::2]
'hlotee!!'
s1[::3]
'hltr!'
s1[-15:-10]
'hello'
s1[-10:-15]
''
s1[-15::2]
'hlotee!!'
s1[-15::-2]
'h'
s1[-10::-2]
' le'
s1[::-2]
'!!eetolh'

=================================================== RESTART: C:/Wipro Training/Python/str1ex.py ===================================================
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

=================================================== RESTART: C:/Wipro Training/Python/str1ex.py ===================================================
h
e
l
l
o
 
t
h
e
r
e
 
!
!
!
>>> 
=================================================== RESTART: C:/Wipro Training/Python/str1ex.py ===================================================
h
e
l
l
o
>>> 
=================================================== RESTART: C:/Wipro Training/Python/str1ex.py ===================================================
h
e
l
l
>>> 
=================================================== RESTART: C:/Wipro Training/Python/str1ex.py ===================================================
h
e
l
l
o
