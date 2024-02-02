python notes
_______________________________________________
print formatting it is the process of combining variables and strings toger to display the formatted output

1).format method: example: i need to dispaly statement as : my emplyoee name is aa and employeid is 111 name="aa" id=111 print("my employee name is {} and employeid is {}".format(name,id))

2)f-method print(f"my employee name is {name} employeid is {id}")

input method

f-method and format method in input string-group of characters in python indexing allows the user to grab paratial values from any data indexing starts from 0 to n-1

-Why python is required for DevOps even though we have shell scripting 1.python supports reverse indexing . it will start display from last character. for last character index is -1 python has advance/adavantage features compare to shell scripting 2.It is independent of OS. where as bash scripting works only on Linux OS 3.For writing more complex logic which we can't do it in shell scripting 4.Python provides better error handling compared with shell scripting 5.number of lines of code will be reduced compared with shell scripting 6.Easy to learn and understand

string
a group of characters. 
1)in pyhon indexing allows the user to grab partial values from any data indexing starts from 0 to n-1
  python has advance/adantages features compare to shell scripting
2) python also support reverse indexing. it will start display from last character. for last character index is -1

input:Used to input data from user
#input data
name=input(f"enter the name\n")
dob=input(f"enter the dob\n")
place=input(f"enter the place name\n")
print(f"my name is {name} and my dob is {dob} and place is {place}")

len: It is used to find the length of the string
example:to find the length of the string
	count=len(test)

List
list is group of elements with different type or same type and it is created using a pair of [].
using index, the elements of list can be accessed
SYNTAX with examples:
	var=[] #emptylist

	to append an element to a list
	var=["hello"]
	var.append("hi")
	print(var)

	using index values to print
	list=[1, 2, 3, 4, 5, "int", "float", "string", "dictionaries"]
	print(list[0], list[6], list[0:4])
	print(list[-1], list[-2])#for reverse index

	to add a list to another list
	var=["hello", "hi"]
	list=[1, 2, 3, 4, 5, "int", "float", "string", "dictionaries"]
	print(list[0], list[6], list[0:4])
	list.extend(var)
	print(list)

	list.pop(6)#to remove specific element from the list using the index values

	list.pop("int")# to remove specific element from list by providing the element

	to replace element in the list with new element
	list[0]="one"
	list[1]="two"

Dictionary 
Is key-value pair, it is created pair of {} using key-value of dictionary can be accessed
mydict={} #empty dictionary

mydict={"fruits": "apple", "car": ["petrol", "desil", "battery"], "company" : ["swift", "tesla", "renault", "tata", "bmv"] }

print(mydict["company"][2]) #to print element in list of key in a dictionary
mydict={"details": {"name": "tarun", "id": 123, "place": ["bzj", "vizag", "ogl"]}, "fruits": "apple", "car": ["petrol", "desil", "battery"], "company" : a", "renault", "tata", "bmw"]}
print(mydict["details"])#to print the values of specific key
print(mydict["details"]["id"])#to print a specific key value

sub= {"birds": ["sparrow", "kingfisher", "parrot", "macaw", "hummingbird"], "types": {"intigers": [1, 2, 3, 4, 5],
    "floats": None, "alphabets": {"vowels": ['a', 'e', 'i', 'o', 'u'], "consonants": "bcdfghjklmnpqrstvwxyz"}},
      "mydict" :{"avengers": ["hulk", "antman", "spiderman"], "xmen": ["raven", "wovelirin"]}}
for s in sub:
    print(s) # it will print all the keys of dictionary
for index, keys in enumerate(sub):
    print(keys,index) # it will print keys and index values
for key in sub.keys():
    print(key) # it will print all keys one by one
for value in sub.values():
    print(value) # it will print all values 
for key, value in sub.items():
    print(key,value)# it will print both all keys and values


fruits= ["dragonfruit", "orange", "mango", "grapes"]
val= "orange"
1)SIMPLEIF
if condition:
	statment
example:
if "grapes" in fruits:
    print("element grapes is there in the list")

2)IFELSE
if condition:
	statment1
else:
	statment2

example:
#to search for a specific element in the list
if "grapes" in fruits:
    print("element grapes is there in the list")
else:
    print("element grapes is not there in the list")

3)NESTEDIF or If-elif
if condition:
     print()
elif condition:
     print()
else:
     print()

example:
if "grapes" in fruits:
	print("grapes are fruits")
elif "mango" in fruits:
	print("mango are fruits")
else:
	print("not avaliable")



#Boolean first letter in uppercase"
flag= False
if flag:
    print("flag is true")
else:
    print("flag is false")
if not flag: #not to check the false condition
    print("if condition entered")

#to check weather a list is empty or not
test_list= [1, 2, 3]
if test_list:
    print(f"the list is not empty {test_list}")
else:
    print(f"the list is empty {test_list}") 
#to check weather a list is empty 
if not test_list:
        print(f"the list is empty {test_list}")

stat= {"A": None, "b": ["ball", "bat", "brain"], "c": "cut"}
#to check a specific key in a dictionary
if "A" in stat:
    print("keyfound")
else:
    print("key not found")

#to check a specific value in a dictionary
if "cut" in stat.values():
    print("value found")
else:
    print("value not found")
#to check a value is persent inside a key or not
if stat['c'] == "cut":
    print("value found")
if "c" in stat and stat["c"] == "cut":
    print("value found")
else:
    print("value not found")

#to check a key is persent or not and the specific value is persent or not
if "b" in stat and "bat" in stat["b"]:
    print("contains value")
else:
    print("dosent contain value")

 
sub= {"birds": ["sparrow", "kingfisher", "parrot", "macaw", "hummingbird"], "types": {"intigers": [1, 2, 3, 4, 5],
    "floats": None, "alphabets": {"vowels": ['a', 'e', 'i', 'o', 'u'], "consonants": "bcdfghjklmnpqrstvwxyz"}},
      "mydict" :{"avengers": ["hulk", "antman", "spiderman"], "xmen": ["raven", "wovelirin"]}}
#examples to check the values of keypairs of the dictionary inside a dictionary
if "o" in sub["types"]["alphabets"]["vowels"]:
    print("element exitst")
else:
    print("element dosent exist")
#to search a element of list of a key inside a dictionary
print(sub["types"]["alphabets"]["consonants"][10])


classes="DEVops"
class1= classes.lower()#to modify string characters to lower case
class2= classes.upper()#to modify string characters to upper case
#to compare a pattern that starts with inside a varible string data
if class1.startswith('dev'):
    print("true")
else:
    print("false")

#to compare a pattern that ends with inside a varible string data
if class2.endswith('OPS'):
    print("true")

#editing a string data type
countries="India.Russia.Usa.Uk.Egypt.Canada"
print(countries.replace('.','/'))# to a string or a character
print(countries.split('.'))#to split a string based on a character or a string and store it in list
print(countries.split('.', 3))#to split a string based on a character or a string in the first three occurances and store it in list
print(countries.rsplit('.', 3))#to split a string based on a character or a string in the last three occurances and store it in list





python modules Modules:

SYS module : This is a module which is used to print the system related values. Using this module we can access variables maintained by the python interpreter and functions that interact with the interpreter.To use this module need to import sys module. syntax: import sys
a) sys.argv :(argv-argument vector) It is a list in python which contains the command line arguments passed to the script. The first element is the script name. example: import sys print(sys.argv) - It will print the name and argument passed print(sys.argv[1]) - It will print the first command line argument passed

b) sys.path : It will print the current system path import sys print(sys.path) c) sys.exit : It is used to exit from the python interpreter by raising the exception. import sys sys.exit(0) sys.exit(f"Execution stopped")

 OS module : This module provides the way for interacting with the OS.
 
 - os.getcwd() - Display the current working directory
 - os.makedirs() - It is used to create the directory
    os.makedirs("pythondir", exist_ok=True) -
 - os.listdir() - It will list all the files and directories
    print(os.listdir("D:\\Drives\\DRC\\python\\pythonProject"))
 - os.chdir() - It is used to change the directory
    os.chdir("pythondir")
    print(os.getcwd())
 - os.path.isfile() - It will check whether it is a file or not and return true if it exists.
    print(os.path.isfile("1.txt")) - checks file exist
    print(os.path.exists("pythondir")) - checks directory exist
 - os.path.join() - It is used to join the path
 - os.path.basename() - It will return the base name of the file.
 - os.walk() - It is used to walk through all the directory and sub directoy and in each iteration it returns the current path, all the files and 
               directories.

#read, write and appending a file
we can create files in 3 different modes
-read
-write
-append
write: 	If the file exist then it will over write otherwise it will create a new file add content
example:
with open("filename", 'w') as timer:
    timer.write(f"welcome to python\ntoday we are discussing the file editing ")

read:Here the file will be opened for only reading purpose. We cannot modify the file contents
example:
with open("filename", 'r') as ti:
    content = ti.read()
    print(content)

Append: If the file exists it will add the contents at the end of the file, if the file not exists then it will create a new file and add the content
example:
mylist= ["hi", "hello", "welcome"]
with open("filename", 'a') as mr:
    for lt in mylist:
        mr.write(f"\n {lt}")

#combining read and write
with open("filename", 'r') as ti:
    content = ti.read()
    print(content)
with open("filename", 'w') as timer:
    timer.write(content)

#to read and write at same time
with open("checkmode.txt", "r+") as time:
    content= time.read()
    time.seek(0)#it will take to pointer to the starting of first line
    time.write("testing seek\nand its use\n")
    time.write(content)
    time.close()#to close a file
note: Here we are appending some content at the beginging of a file 

import re
email_name="sham <sham.xyz@gmail.com>, xyz <abc.axy@gmail.com> alex <alex.gmai.com>"
search_value=re.search("alex", email_name) # to search pattern if present it will show first occurence
print(search_value) #<re.Match object; span=(51, 55), match='alex'>
found_values=re.findall("alex", email_name) # it will find all occurencees of pattern and store inside list
print(found_values) #['alex', 'alex']

#script to read the notice, license file and add the content of each file a noticelicense.txt file. The noticelicense file may be started with notice or license. Before appending the content to noticelicense.txt file add relative path and file name.
import os
pattern=["notice", "license"]
path_dir= os.getcwd()
file_name= "/home/ubuntu/no_license.txt"
for pat in pattern:
        time.write(f"{pat}\n")
    for root, dir, files in os.walk(path_dir):
        for file in files:
            if file.lower().startswith(pat):
                filepath= os.path.join(root, file)
                with open(filepath, 'r') as time:
                    content = time.read()
                    print(f"{file}\n{content}")
                with open(file_name, 'a') as time:
                    time.write(f"{filepath}\n{content}")
    with open(file_name, 'a') as time:
            time.write('*' * 30)
            time.write("\n")

#To check all the notice and license files are present in the file that we appended data in previous script
import os, re
pattern=["notice", "license"]
for pat in pattern:
    for root, dir, files in os.walk(os.getcwd()):
        for file in files:
            if file.lower().startswith(pat):
                with open ("/home/ubuntu/no_license.txt", 'r') as data:
                    content= data.read()
                    fetch=re.search(file, content)
                    print(fetch)
