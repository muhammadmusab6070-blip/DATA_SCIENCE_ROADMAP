Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
items = ["fruit","pasta","pizza"]
items
['fruit', 'pasta', 'pizza']
items[1]
'pasta'
items[0:]
['fruit', 'pasta', 'pizza']
items[-1]
'pizza'
>>> items.append("butter")
>>> items
['fruit', 'pasta', 'pizza', 'butter']
>>> items.insert(1,"soap")
>>> items
['fruit', 'soap', 'pasta', 'pizza', 'butter']
>>> find something
SyntaxError: invalid syntax
>>> //to find something
SyntaxError: invalid syntax
>>> "soap" in items
True
>>> "burger" in items
False
>>> s = "shampoo"
>>> 
>>> 
>>> items + s
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    items + s
TypeError: can only concatenate list (not "str") to list
