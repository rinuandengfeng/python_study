Python 3.9.0a4 (tags/v3.9.0a4:6e02691, Feb 25 2020, 23:23:54) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L=['Michael','Sarah','Tracy','Bob','Jack']
>>> r=[]
>>> n=3
>>> f
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    f
NameError: name 'f' is not defined
>>> for i in range(n):
	r.append(L[i])

	
>>> r
['Michael', 'Sarah', 'Tracy']
>>>  L = list(range(100))
 
SyntaxError: unexpected indent
>>> L = list(range(100))
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> L[-10:]
[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> L[:10}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> L[:10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> (0,1,2,3,4,5)[:3]
(0, 1, 2)
>>> 'abcdefg'[:3]
'abc'
>>> 'abcdefg[::2]
SyntaxError: EOL while scanning string literal
>>> 'abcdefg'[::2]
'aceg'
>>> 
>>> 
>>> [x*x for x in range (1,11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> [x*x for x in range(1,11) if x%2=0]
SyntaxError: invalid syntax
>>> [x*x for x in range(1,11) if x%2==0]
[4, 16, 36, 64, 100]
>>> 
>>> [m+n for m in 'abc ' for n in 'xyz']
['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz', ' x', ' y', ' z']
>>> 