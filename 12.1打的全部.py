Python 3.9.0a4 (tags/v3.9.0a4:6e02691, Feb 25 2020, 23:23:54) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = input()
user
>>> user
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    user
NameError: name 'user' is not defined
>>> name = input()
hello
>>> name
'hello'
>>> name = input()
user
>>> name
'user'
>>> print(name)
user
>>> name = input()
prnt("hello",name)
>>> name
'prnt("hello",name)'
>>> name = input()
user
>>> print("hello",name)
hello user
>>> name = input()
user
>>> name = input("plese enter your name:")
plese enter your name:root
>>> print("hello",name)
hello root
>>> print(1024*768)
786432
>>> 'I\'m\"OK\"!'
'I\'m"OK"!'
>>> "I\'m\"OK\"!"
'I\'m"OK"!'
>>> I'm"OK"
SyntaxError: EOL while scanning string literal
>>> print('I\'m ok.')
I'm ok.
>>> print('I\'m lerning\nPython.')
I'm lerning
Python.
>>> print('\\\n\\')
\
\
>>> ptint('\\\t\\')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    ptint('\\\t\\')
NameError: name 'ptint' is not defined
>>> print('\\\t\\')
\	\
>>> print('''line1
... line2... line3''')
line1
... line2... line3
>>> print('''line1
... line2
... line3''')
line1
... line2
... line3
>>> print('''line1
...line2
...line3''')
line1
...line2
...line3
>>> 
>>> print('''line1
... line2
... line3''')
line1
... line2
... line3
>>> print('''line1\nline2\nline3\n
''')
line1
line2
line3


>>> print('''line1 \n
line2 \n
line3 \n''')
line1 

line2 

line3 

>>> print('''line1
line2
line3
''')
line1
line2
line3

>>> ('''line1
... line2
... line3''')
'line1\n... line2\n... line3'
>>> print('''line1 ... line2 ... line3''')
line1 ... line2 ... line3
>>> print(r'''hello,\n
world''')
hello,\n
world
>>> True
True
>>> False
False
>>> 3>2
True
>>> 3>5
False
>>> a=123
>>> print(a)
123
>>> a='abc'
>>> print(a)
abc
>>> n =123
>>> f=456.789
>>> s1 ='hello,world'
>>> s2='hello,\'Adam\''
>>> s3= r'hello,"bart"'
>>> s4=r'''hello,
Lisa!'''
>>> print(n,f,s1,s2,s3,s4)
123 456.789 hello,world hello,'Adam' hello,"bart" hello,
Lisa!
>>> print(n
      f
      
SyntaxError: invalid syntax
>>> print(n\n f\n s1\n s2\n s3\n s4\n)
SyntaxError: unexpected character after line continuation character
>>> 
>>> 
>>> print('包含中文的str')
包含中文的str
>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'
>>> '\u4e2d\u6587'
'中文'
>>> x=b'ABC'
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> '中文'.encode('ascii')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    '中文'.encode('ascii')
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87.decode('utf-8')
SyntaxError: invalid syntax
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
>>> len('ABC')
3
>>> len('中文')
2
>>> 
>>> 'hello,%s'%'world'
'hello,world'
>>> 'hi,%s,you have $%d.'%(michael',1000000)
		       
SyntaxError: EOL while scanning string literal
>>> 'Hi,%s,you have $%d.'%('michael',1000000)
'Hi,michael,you have $1000000.'
>>> int a=1
SyntaxError: invalid syntax
>>> int b = 1
SyntaxError: invalid syntax
>>> int a=1;
SyntaxError: invalid syntax
>>> int a = 123;
SyntaxError: invalid syntax
>>> print(a);
abc
>>> print(f)
456.789
>>> int o =123;
SyntaxError: invalid syntax
>>> print(o)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    print(o)
NameError: name 'o' is not defined
>>> int num = 213;
SyntaxError: invalid syntax
>>> 'age:%s.Gender:%s'%(25,true)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    'age:%s.Gender:%s'%(25,true)
NameError: name 'true' is not defined
>>> int a;
SyntaxError: invalid syntax
>>> int a
SyntaxError: invalid syntax
>>> 