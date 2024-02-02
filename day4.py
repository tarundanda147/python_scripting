fruits= ["dragonfruit", "orange", "mango", "grapes"]
val= "orange"

if "grapes" in fruits:
    print("element grapes is there in the list")
else:
    print("element grapes is not there in the list")
flag= False
#Boolean first letter in uppercase"
if flag:
    print("flag is true")
else:
    print("flag is false")
if not flag: #not to check the false condition
    print("if condition entered")

test_list= [1, 2, 3]
if test_list:
    print(f"the list is not empty {test_list}")
else:
    print(f"the list is empty {test_list}")
if not test_list:
        print(f"the list is empty {test_list}")

stat= {"A": None, "b": ["ball", "bat", "brain"], "c": "cut"}
if "A" in stat:
    print("keyfound")
else:
    print("key not found")

if "cut" in stat.values():
    print("value found")
else:
    print("value not found")

if stat['c'] == "cut":
    print("value found")
if "c" in stat and stat["c"] == "cut":
    print("value found")
else:
    print("value not found")

if "b" in stat and "bat" in stat["b"]:
    print("contains value")
else:
    print("dosent contain value")
sub= {"birds": ["sparrow", "kingfisher", "parrot", "macaw", "hummingbird"], "types": {"intigers": [1, 2, 3, 4, 5],
    "floats": None, "alphabets": {"vowels": ['a', 'e', 'i', 'o', 'u'], "consonants": "bcdfghjklmnpqrstvwxyz"}},
      "mydict" :{"avengers": ["hulk", "antman", "spiderman"], "xmen": ["raven", "wovelirin"]}}
if "o" in sub["types"]["alphabets"]["vowels"]:
    print("element exitst")
else:
    print("element dosent exist")
print(sub["types"]["alphabets"]["consonants"][10])
