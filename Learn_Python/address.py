Book = {}

Book['Tom'] = {
    'name': 'Tom',
    'address': '1 red Street, NY',
    'phone' : '555-555-5555',
}

Book['Jane'] = {
    'name': 'Jane',
    'address': '1 blue Street, NY',
    'phone' : '524-363-3392',
}

import json

s = json.dumps(Book)

with open("D://DATA SCIENCE ROADMAP//Data//book.txt","w") as f:
    f.write(s)
    

