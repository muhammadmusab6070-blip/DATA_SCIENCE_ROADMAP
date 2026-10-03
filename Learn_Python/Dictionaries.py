dict = {
    "a":1,
    "b":2,
    "c":3
}

print(dict)

dict["d"] = 1
dict["e"] = 2
dict["f"] = 3

print(dict)

del dict["d"]
print(dict)


for key in dict:
    print(f"Key : {key} , Value :  {dict[key]} ")

if "a" in dict:
    print(f"a : {dict['a']}")


dict.clear()

print(dict)

""" list of vales group together is called tuple """
""" Dictionary are like Maps, Hashtable, and associate Lists """


points = (5,8)

print(points)

print(points[0],points[1])

""" All values have same meaning = List  """
""" All Values have different meaning = tuple  """

""" Remember! we can change the value of List bt donot change the value of tuple """