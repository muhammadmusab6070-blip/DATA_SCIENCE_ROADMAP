import math
import calendar
# import function before moving to module directory

# import sys
# sys.path.append("C:\DirectoryName")
# import moduleName as f


import Modules.functions as f # importing our own module

print(math.floor(math.sqrt(5)))

print(math.pow(5,8))

print(dir(math))

cal = calendar.month(2007,7)

print(cal)

print(calendar.month(2007,7))

print(dir(calendar))

print(calendar.isleap(2007))

""" Create yor own module.Take Your existing file as a module """

exp = [2300,3394,293]

print(exp)
# print(function.total_exp(exp))  before moving to module directory
print(f.total_exp(exp))

