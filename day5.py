sub= {"birds": ["sparrow", "kingfisher", "parrot", "macaw", "hummingbird"], "types": {"intigers": [1, 2, 3, 4, 5],
    "floats": None, "alphabets": {"vowels": ['a', 'e', 'i', 'o', 'u'], "consonants": "bcdfghjklmnpqrstvwxyz"}},
      "mydict" :{"avengers": ["hulk", "antman", "spiderman"], "xmen": ["raven", "wovelirin"]}}
for s in sub:
    print(s)
for index, s in enumerate(sub):
    print(s,index)
for key in sub.keys():
    print(key)
for value in sub.values():
    print(value)
for key, value in sub.items():
    print(key,value)
classes="DEVops"
class1= classes.lower()
class2= classes.upper()
print(class1,class2)
if class1.startswith('dev'):
    print("true")
else:
    print("false")
if class2.endswith('OPS'):
    print("true")
countries="India.Russia.Usa.Uk.Egypt.Canada"
print(countries.replace('.','/'))
print(countries.split('.', 3))
print(countries.rsplit('.', 3))
