file = open("D://DATA SCIENCE ROADMAP//data//book.txt","r")

s = file.read()
# Here s is string
print(s)
print(type(s))

file.close()

import json
Book = json.loads(s)
# Here Book is a dictionary containing json objects
print(Book)
print(type(Book))

print(Book["Tom"])
print(Book['Tom']['address'])
print(type(Book["Tom"]))

print(Book["Jane"])
print(type(Book["Jane"]))

for person in Book:
    print(person)
    print(Book[person])

