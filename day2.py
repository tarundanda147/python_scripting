var="hello, good morning"
print(f"the string is\n {var}")
count=len(var)
print(f"length of the string is {count}")
print(var[0], var[7], var[12], var[7:11], var[12:19])
print(var[-1], var[-5])
mylist = []
ourlist = [10, 15, 30, "hello"]
print(f"{ourlist}")
print(ourlist[2], ourlist[0])
ourlist.append("thankyou")
ourlist.append(35)
print(ourlist)
ourlist.pop()
print(ourlist)
ourlist.pop(2)
print(ourlist)
ourlist[1] ="nice"
print(ourlist)
content=["one", 2]
ourlist.extend(content)
print(ourlist)
ourlist.pop("one")
