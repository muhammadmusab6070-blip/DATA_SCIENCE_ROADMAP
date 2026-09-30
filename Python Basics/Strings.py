Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1 = "ice cream"
s2 = "Cake"
s1[0]
'i'
s1[0:]
'ice cream'
s1[1:3]
'ce'
s1[:8]
'ice crea'
s1+" "+s2
'ice cream Cake'
s1[1] = "w"
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s1[1] = "w"
TypeError: 'str' object does not support item assignment
>>> a = 24
>>> s1 + a
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s1 + a
TypeError: can only concatenate str (not "int") to str
>>> str(a)
'24'
>>> s1 + a
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s1 + a
TypeError: can only concatenate str (not "int") to str
>>> s1+a
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s1+a
TypeError: can only concatenate str (not "int") to str
>>> s1 + str(a)
'ice cream24'
